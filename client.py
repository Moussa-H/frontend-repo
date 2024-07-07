# frontend-repo/client.py

import yaml

class Client:
    def __init__(self, config_file):
        with open(config_file, 'r') as file:
            self.config = yaml.safe_load(file)
    
    def print_server_ip(self):
        print(f"Server IP Address: {self.config['ServerIPAddress']}")

if __name__ == "__main__":
    client = Client('path/to/config.yaml')
    client.print_server_ip()
