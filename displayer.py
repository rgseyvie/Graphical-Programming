class Displayer():
    def __init__(self, all_nodes, all_ports, current_nodes = [], current_ports = []):
        self.all_nodes = all_nodes
        self.all_ports = all_ports
        self.current_nodes = current_nodes
        self.current_ports = current_ports

    def list_nodes(self):
        return self.all_nodes

    def list_ports(self):
        return self.all_ports