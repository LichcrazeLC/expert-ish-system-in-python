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
  "J": "Is a patrolling policeman",

  "K": "Wears Pink",
  "O": "Is a member of the BluePink Rock Band",
  "P": "Is a singer",
  "L": "Looks like a cartoon animal",
  "M": "Has fur",
  "N": "Is pretty beastly",
  "Q": "Is a member of this town",
  "R": "Is someone you can see on the streets daily",
  "S": "Is a Looney living here",
  "T": "Has a MOVING OUT truck outside of his house",
  "U": "Is a Looney that is moving out of the town"
}

#RULES
rules_list = [
    #RPN
  "AB+E=",
  "CD|F=",
  "EG>",
  "FG+H=",
  "FI+J=",
  "KI|O=",
  "OP>",
  "MN>",
  "LN+Q=",
  "QR>",
  "RS>",
  "TQ+U="
]

def evaluate_and(operandNodes, resultNode):
  if all(operandNodes) :
      resultNode.state = True 

def evaluate_or(operandNodes, resultNode):
  if any(operandNodes) :
      resultNode.state = True 