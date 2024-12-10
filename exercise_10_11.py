from pathlib import Path
import json

path = Path("favorite_number.json")
number = input("What is your favorite number? ")
contents = json.dumps(number)
path.write_text(contents)