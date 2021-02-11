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
```

## Contributing
Pull requests are NOT welcome. Please don't contact me about it.

## License
No license yet :( 
