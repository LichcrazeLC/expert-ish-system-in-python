import re, random
from storage import rules_list, facts_dictionary
from queue import Queue

q = Queue(maxsize = 100)
graph = []

#GRAPH PARSING ##################################################################################################

class Node: 
    def __init__(self):
        self.parents = []
        self.visited = False
        self.state = False

    def resolveNode(self):
        pass


class DataNode(Node): 
    def __init__(self, key, value):
        super().__init__()
        self.key = key
        self.value = value

    def nodeEvaluated(self, evaluation):
        if self.visited == False:
            self.state = evaluation
            self.visited = True
            if evaluation == True: 
                if not self.parents:
                    print("Final deduction: " + self.value)
                    quit()
                else:
                    self.resolveParentOperator()
            else:
                print("Node state set to false or Pruned, Node Key: " + self.key)
                for parent in self.parents:
                    if parent.type == "AND" or parent.type == "IMPLIES":
                        parent.resolveUpperNode(False)

            self.pruneChildren()

    def resolveParentOperator(self):
        for parent in self.parents:
            parent.resolveNode()

    def pruneChildren(self):
        connector_nodes = list(filter(lambda x: x.key == None, graph))
        for node in connector_nodes:
            for parent in node.parents:
                if parent.key == self.key:
                    node.pruneChildren()
    
    def resolveNode(self):
        if self.state == True:
            return True
        else:
            print("Proceeding to evaluate Data Node... ")
            val = input(self.value + "?\n") 
            if val == "yes":
                self.nodeEvaluated(True)
                return True
            else:
                self.nodeEvaluated(False)
                return False


class ConnectorNode(Node): 
    def __init__(self, operands, operator):
        super().__init__()
        self.operands = operands
        self.type = operator
        self.state = None
        self.key = None

    def resolveUpperNode(self, evaluation):
        for parent in self.parents:
            parent.nodeEvaluated(evaluation)
    
    def pruneChildren(self):
        for op in self.operands:
            if len(op.parents) == 1 and op.visited == False:
                op.nodeEvaluated(False)
            elif self.type == "OR" or self.type == "IMPLIES":
                op.nodeEvaluated(False)

    def resolveNode(self):
        self.visited = True
        if self.type == "AND":
            print("Proceeding to Evaluate multiple Data Nodes connected by an And operator... ")
            for operand in self.operands:
                if (operand.state == False and operand.visited == True) or operand.resolveNode() == False:
                    self.pruneChildren()
                    print("One of the Operator Nodes returned False, setting the AND Result to False...")
                    self.resolveUpperNode(False)
                    break
            else:
                if len(self.parents[0].parents) != 0:
                    print("Intermediary Assessment concluded that..." + self.parents[0].value)
                self.resolveUpperNode(True)
                for operand in self.operands:
                    operand.nodeEvaluated(True)
      
        elif self.type == "OR":
            print("Proceeding to Evaluate multiple Data Nodes connected by an Or operator... ")
            for operand in self.operands:
                if operand.state == True:
                    self.resolveUpperNode(True)
                    for operand in self.operands:
                        if (len(operand.parents) == 1):
                            operand.nodeEvaluated(True)
                        print("Intermediary Assessment concluded that..." + self.parents[0].value)
                    break
                elif operand.visited == False:
                    if operand.resolveNode() == True:
                        operand.nodeEvaluated(True)
                        self.resolveUpperNode(True)
                        print("Intermediary Assessment concluded that..." + self.parents[0].value)
                        break
            
            if all(operand.state == False for operand in self.operands):
                print("Both of the Operator Nodes returned False, setting the OR Result to False...")
                self.resolveUpperNode(False)             

        
        elif self.type == "IMPLIES":
            print("Found Implies Operator, proceeding to evaluate operand... ")
            for operand in self.operands:
                if operand.state == True or operand.resolveNode() == True:
                    print("Implies that " + self.parents[0].value)
                    operand.nodeEvaluated(True)
                    self.resolveUpperNode(True)
                    break

#GRAPH GENERATION ##################################################################################################
def appendDataNodeParents(data_nodes, parent_nodes):
    for dn in data_nodes:
        dn.parents += parent_nodes

for r in rules_list:
    charlist = list(r)
    rule_data_nodes = []
    rule_connector_nodes = []
    print ("Found new rule, proceeding to generate graph structure...")
    for char in charlist:
        existingNode = None
        if char.isalpha():
            for n in graph:
                if n.key == char:
                    existingNode = n
                    break
            if existingNode == None: 
                #DATA NODE          
                print("Proceeding to instantiate data node and linking it to the graph... Node Key: " + char + ", Node Value: " + facts_dictionary.get(char))
                n = DataNode(char, facts_dictionary.get(char))
                graph.append(n)
                q.put(n)
                rule_data_nodes.append(n) 
                print("Graph size = ", len(graph))         
            else:
                rule_data_nodes.append(existingNode)
            if (len(rule_connector_nodes) != 0):
                for cn in rule_connector_nodes:
                    cn.parents = [n]
                    print ("Appended parent to connector node: " + cn.type + ", Operands:", [op.key for op in cn.operands], "Parents:", cn.parents[0].key)
        if not char.isalnum(): 
            #CONNECTOR NODE  
            if char != "=":
                children_keys=[n.key for n in rule_data_nodes]  
                if char == "+":
                    print("Found AND Operator, Creating Node... Node Operands: ", children_keys, ", Node Operator: " + char)
                    n = ConnectorNode(list(rule_data_nodes), "AND")
                    appendDataNodeParents(rule_data_nodes, [n])
                elif char == "|":
                    print("Found OR Operator, Creating Node... Node Operands: ", children_keys, ", Node Operator: " + char)
                    n = ConnectorNode(list(rule_data_nodes), "OR")
                    appendDataNodeParents(rule_data_nodes, [n])
                elif char == ">":
                    print("Found IMPLIES Operator, Creating Node... Node:", rule_data_nodes[0].key, " Implies:", rule_data_nodes[1].key ,"Node Operator: " + char)
                    n = ConnectorNode([rule_data_nodes[0]], "IMPLIES")
                    n.parents = [rule_data_nodes[1]]
                    rule_data_nodes[0].parents = [n]
                graph.append(n)
                q.put(n)
                rule_connector_nodes.append(n) 
                print("Graph size = ", len(graph))

### ACTION

def getAQuestion(graph):
    for node in graph:
        if node.visited == False and node.key != None and len(node.parents) != 0:
            print ("New Node Chosen for Evaluation, Node Key: " + node.key)
            node.resolveParentOperator()
            break
    else:
        print("All posibilities have been exhausted. Sorry :(")
        quit()

#while any(len(node.parents) == 0 and node.visited != True for node in graph):
random.shuffle(graph)

while not any(len(node.parents) == 0 and node.visited == True and node.state == True for node in graph):
    getAQuestion(graph)
 










