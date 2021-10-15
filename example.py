from backend.node import Node, AdderNode, SquareNode
from backend.port import Port
# 测试样例，node中计算并输出信息
# 两输入一输出的加法器node，连接一输入一输出的平方node，用control link连接

node1 = AdderNode('node1')
node2 = SquareNode('node2')
node1.inputs = []
node1.outputs = []
port1 = Port('port1', 0, 'input', None, None)
port2 = Port('port2', 0, 'input', None, None)
port3 = Port('port3', 0, 'output', None, None, 2)
port4 = Port('port4', 0, 'input', None, None)
port5 = Port('port5', 0, 'output', None, None)
node1.successors = [node2]
node2.predecessors = [node1]

port1.connect(node1)
#port1.node = node1
#node1.inputs.append(port1)
port2.connect(node1)
port3.connect(node1)
port4.connect(node2)
port5.connect(node2)
port3.link(port4)

port1.update(1)
port2.update(2)
node1.add()
node2.square()


