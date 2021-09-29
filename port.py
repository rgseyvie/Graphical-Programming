class Port():

    def __init__(self, name, value, type, node):
        self.name = name
        self.value = value
        self.type = type    # input, output
        self.node = node
        self.flag = False   # dirty flag

    def update(self, value):
        self.value = value
        self.flag = True

    def check_dirty(self):
        return self.flag

    def connect(self, node):
        self.node = node
        node.connect(self)

    def disconnect(self, node):
        if self.node == node:
            self.node = None
            node.disconnect(self)
            return True
        else:
            return False

    def serialize(self):
        return {'name': self.name,
                'value': self.value,
                'type': self.type,
                'node': self.node}

    def deserialize(self, port_dict):
        de_port = Port(port_dict['name'],
                       port_dict['value'],
                       port_dict['type'],
                       port_dict['node'])
        return de_port

    def check_illegal(self):
        # 子类继承后具体实现
        return False