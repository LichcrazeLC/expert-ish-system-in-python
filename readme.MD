# Expert-ish system in Python 

This is an expert system coded in python. It takes a rules List in Reverse Polish Notation and a facts dictionary (Both in storage.py file) and generates a graph. And it asks questions. And it gives answers. And it's great. 

## Installation

You can just clone it and run it if you have python installed on your machine, after navigating to the project folder.

```bash
git clone https://github.com/LichcrazeLC/expert-ish-system-in-python.git
python main.py
```
## Usage

If you want to generate a graph and use the expert system with other rules and facts, just change these in storage.py

```python
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
  "N": "Has a big furry nose",
  "Q": "Is a member of this town",
  "R": "Is someone you can see on the streets daily",
  "S": "Is a Looney living here",
  "T": "Has a MOVING OUT truck outside of his house",
  "U": "Is a Looney that is moving out of the town",
  "Y": "Is pretty beastly",
  "V": "Is recognized by other townsfolk",
  "Z": "Has big long ears"
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
  "TYV+U=",
  "ZN|Y"
]

```

## Contributing
Pull requests are NOT welcome. Please don't contact me about it.

## License
No license yet :( 
