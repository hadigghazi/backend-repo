import yaml

class Server:
    def __init__(self, config_file):
        with open(config_file, 'r') as file:
            self.config = yaml.safe_load(file)
        self.server_ip = self.config['ServerIPAddress']
        self.run_localhost = self.config['run_localhost']

    def check_localhost(self):
        if self.run_localhost:
            print("Error: run_localhost is set to True")

    def get_server_ip(self):
        return self.server_ip
#test 3
if __name__ == "__main__":
    server = Server('../config.yaml')
    server.check_localhost()
    print(server.get_server_ip())
