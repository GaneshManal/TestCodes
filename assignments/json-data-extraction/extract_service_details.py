import os
import json


def extract_unhealthy_services(cluster):
    print("\n" + "-" * 80 + "\n")
    with open(os.getcwd() + os.path.sep + 'service-status-{}.json'.format(cluster)) as fh:
        data = json.load(fh)

    unhealthy_services = []
    for service in data:
        if service.get('status') != 'healthy':
            print(service.get('service'), ": ", service.get('status'))
            unhealthy_services.append(service.get('service'))

    print("\nServices not healthy: {}".format(len(unhealthy_services)))

if __name__ == "__main__":
    clusters = ['38']
    for cluster in clusters:
        extract_unhealthy_services(cluster)
