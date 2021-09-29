class Node():

    def __init__(self, name, successors, predecessors, inputs, outputs, max_input, max_output):
        self.name = name
        self.successors = successors
        self.predecessors = predecessors
        self.inputs = inputs    #input ports
        self.outputs = outputs   #output ports
        self.flag = False   # dirty flag
        self.max_input = max_input
        self.max_output = max_output

    def __init__(self, name, successors=[], predecessors=[], inputs=[], outputs=[], max_input = -1, max_output = -1):
        self.name = name
        self.successors = successors
        self.predecessors = predecessors
        self.inputs = inputs    #input ports
        self.outputs = outputs   #output ports
        self.flag = False   # dirty flag
        self.max_input = max_input
        self.max_output = max_output

    def check_dirty(self):
    # 输入是否改变
        return self.flag

    def serialize(self):
        return {'name': self.name,
                'successors': self.successors,
                'predecessors': self.predecessors,
                'inputs': self.inputs,
                'outputs': self.outputs,
                'max_input': self.max_input,
                'max_output': self.max_output}

    def deserialize(self, node_dict):
        de_node = Node(node_dict['name'],
                       node_dict['successors'],
                       node_dict['predecessors'],
                       node_dict['inputs'],
                       node_dict['outputs'],
                       node_dict['max_input'],
                       node_dict['max_output'])
        return de_node

    def connect(self, port):
        if port.type == 'input':
            self.inputs.append(port)
        else:
            self.outputs.append(port)

    def disconnect(self, port):
        if port.type == 'input':
            if port in self.inputs:
                self.inputs.remove((port))
        else:
            if port in self.outputs:
                self.outputs.remove((port))

    def check_illegal(self):
        if self.max_input == -1 or len(self.inputs) <= self.max_input:
            if self.max_output == -1 or len(self.outputs) <= self.max_output:
                for p in self.inputs:
                    if p.check_illegal():
                        return True
                return False
        return True




