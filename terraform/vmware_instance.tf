## Configure the vSPhere Provider
provider "vsphere" {
  vsphere_server = "${var.vsphere_server}"
  user = "${var.vsphere_user}"
  password = "${var.vsphere_password}"
  allow_unverified_ssl = true
}

## Build VM
data "vsphere_datacenter" "dc" {
  name = "BangaloreDC"
}

data "vsphere_datastore" "datastore" {
  name = "datastore15"
  datacenter_id = "${data.vsphere_datacenter.dc.id}"
}

data "vsphere_resource_pool" "pool" {
  name = "TeamGaneshcluster/Resources"
  datacenter_id = "${data.vsphere_datacenter.dc.id}"
}

data "vsphere_network" "ES_Lan" {
  name = "VM Network"
  datacenter_id = "${data.vsphere_datacenter.dc.id}"
}

data "vsphere_host" "host" {
  name = "10.81.1.15"
  datacenter_id = "${data.vsphere_datacenter.dc.id}"
}

data "vsphere_virtual_machine" "template" {
  #name = "DC-UBUNTU-TEMPLATE-DND"
  name = "DC-ES-TEMPLATE-DND"
  #name = "template-ubuntu20lts"
  datacenter_id = "${data.vsphere_datacenter.dc.id}"
}

#data "http" "ip" {
#  url = "https://ifconfig.me"
#}

output "ip" {
  value = "${vsphere_virtual_machine.GAM-ES-TF-TEMPLATE.default_ip_address}"
}


resource "vsphere_virtual_machine" "GAM-ES-TF-TEMPLATE" {
  name = "GAM-ES-TF-TEMPLATE"
  resource_pool_id = "${data.vsphere_resource_pool.pool.id}"
  datastore_id = "${data.vsphere_datastore.datastore.id}"
  
  #count = 1
  num_cpus = 2
  memory = 4096
  wait_for_guest_net_timeout = 0
  guest_id = "ubuntu64Guest"
  scsi_type = data.vsphere_virtual_machine.template.scsi_type
  host_system_id = data.vsphere_host.host.id
  nested_hv_enabled = true
  network_interface {
    network_id = "${data.vsphere_network.ES_Lan.id}"
    adapter_type = "vmxnet3"
  }

  disk {
    size = 80
    label = "DC-ES-TF.vmdk"
    eagerly_scrub = false
    thin_provisioned = true
  } 

  clone {
    template_uuid = data.vsphere_virtual_machine.template.id
    customize {
      linux_options {
        host_name = "GAM-ES-TF-TEMPLATE"
        domain = "maplelabs.com"
      }
      # network_interface {}
      network_interface {
       ipv4_address = "10.81.1.225"
       ipv4_address = "192.168.1.100"
       ipv4_netmask = 24
      }
      #ipv4_gateway = "10.81.1.1"
      #ipv4_gateway = "192.168.1.1"
      timeout = 30
    }
  }

  connection {
    type = "ssh"
    agent = false
    #host = "10.81.1.225"
    #host = "192.168.1.100"
    #host = data.vsphere_host.host.id
    #host = "${self.public_ip}"
    #host = self.private_ip
    #host = data.http.ip.body
    #host = self.default_ip_address
    #host = self.ipv4_address
    #host = self.public_ip
    host = "${vsphere_virtual_machine.GAM-ES-TF-TEMPLATE.default_ip_address}"
    user = "maheshdc"
    private_key = file(pathexpand("~/.ssh/id_rsa"))
  }

  #provisioner "remote-exec" {
  #  inline = ["sudo apt update -y"]
  #}

#   provisioner "local-exec" {
#     #command = "sleep 120; ANSIBLE_HOST_KEY_CHECKING=False ansible-playbook -u maheshdc -i '10.81.1.225' /home/maheshdc/Development/Ansible/ES/SingleNode/es.yml -kK"
#     #command = "sleep 120; ANSIBLE_HOST_KEY_CHECKING=False ansible-playbook -u maheshdc -i '${data.http.ip.body}' /home/maheshdc/Development/Ansible/ES/SingleNode/es.yml -kK"
#     #command = "sleep 120; ANSIBLE_HOST_KEY_CHECKING=False ansible-playbook -u maheshdc -i '${self.default_ip_address}' /home/maheshdc/Development/Ansible/ES/SingleNode/es.yml -kK"
#     #command = "ANSIBLE_HOST_KEY_CHECKING=False ansible-playbook -u maheshdc -i '${data.vsphere_host.host.id}' /home/maheshdc/Development/Ansible/ES/SingleNode/es.yml -kK"
#     command = "ANSIBLE_HOST_KEY_CHECKING=False ansible-playbook -u maheshdc -i '${vsphere_virtual_machine.GAM-ES-TF-TEMPLATE.default_ip_address}' /home/maheshdc/Development/Ansible/ES/SingleNode/es.yml -kK"
#     #command = "ANSIBLE_HOST_KEY_CHECKING=False ansible-playbook -u maheshdc -i /home/maheshdc/Development/Ansible/ES/SingleNode/inventory.ini /home/maheshdc/Development/Ansible/ES/SingleNode/es.yml -kK"
#   }

}
