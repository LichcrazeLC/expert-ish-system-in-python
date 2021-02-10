#DATABASE
facts_dictionary = {
  "A": "Is able to see the top of everyone's head",
  "B": "Casts a big shadow",
  "C": "Has a Katana",
  "D": "Has a big axe",
  "E": "Is massive",
  "F": "Is a fighter",
  "G": "Is Heavy",
  "H": "Is a hired mafia goon",
  "I": "Wears blue",
  "J": "Is a patrolling policeman"
}

#RULES
rules_list = [
    #RPN
  "AB+E=",
  "CD|F=",
  "EG>",
  "FG+H=",
  "FI+J="
]

def evaluate_and(operandNodes, resultNode):
  if all(operandNodes) :
      resultNode.state = True 

def evaluate_or(operandNodes, resultNode):
  if any(operandNodes) :
      resultNode.state = True 