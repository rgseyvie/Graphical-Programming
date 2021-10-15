import time

class Port():

    def __init__(self, name, value, type, node, port, delay):
        self.name = name
        self.value = value
        self.type = type    # input, output
        self.node = node
        self.flag = False   # dirty flag
        self.port = port  # connected port
        self.delay = delay  # machine execution time of control link

    def __init__(self, name, value, type, node, port, delay = 0):
        self.name = name
        self.value = value
        self.type = type    # input, output
        self.node = node
        self.flag = False   # dirty flag
        self.port = port  # connected port
        self.delay = delay  # data link

    def update(self, value):
        time.sleep(self.delay)
        self.value = value
        self.flag = True
        if not self.port == None and self.type == 'output':
            self.port.update(self.value)

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

    def link(self, link_port):
        if self.port == None:
            if link_port.port == None:
                self.port = link_port
                link_port.port = self

    def unlink(self, link_port):
        if self.port == link_port:
            if link_port.port == self:
                self.port = None
                link_port.port = None

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