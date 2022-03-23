import os
from orchestrator_state import SecretsDB

TA_CA_DIR = '/opt/tetration/ta_ca'
TA_CA_FILES = [ 'cakey.pem', 'cacert.pem', 'openssl-ca.cnf', 'serial.txt', 'index.txt']
TA_CA_VAULT_KEY= 'ta_ca'

if __name__ == "__main__":
    secrets_db = SecretsDB()
    secrets_db.initialize_vault()

    for file in TA_CA_FILES:
        if not os.path.exists(os.path.join(TA_CA_DIR, file)):
            data = secrets_db.vault.read_secret(
                "{0}/{1}/{2}".format("secret", TA_CA_VAULT_KEY, file)
            )
            if not data:
                raise "Certs secret {0} is not present on disk or vault".format(file)
            continue
        try:
            with open(os.path.join(TA_CA_DIR, file), "r") as f:
                data = f.read()
                secrets_db.vault.enable_secret_engine('kv', mount_point='secret')
                secrets_db.vault.write_secret("{0}/{1}/{2}".format("secret", TA_CA_VAULT_KEY, file),data,)
        except Exception as e:
            print("Unable to save key {0} to vault".format(file))
            raise e
