# frontend/client.py

import yaml

class Client:
    def __init__(self, config_file='../config.yaml'):
        with open(config_file, 'r') as file:
            self.config = yaml.safe_load(file)
    
    def print_server_ip(self):
        print(f"Server IP Address: {self.config['ServerIPAddress']}")

    def check_run_localhost(self):
        if self.config.get('RunLocalhost', False):
            print("Running on localhost. Please update configurations if necessary.")

if __name__ == "__main__":
    client = Client()
    client.print_server_ip()
    client.check_run_localhost()
