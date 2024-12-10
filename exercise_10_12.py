from pathlib import Path
import json

def get_stored_number(path):
    if path.exists():
        contents = path.read_text()
        number = json.loads(contents)
        return number
    else:
        return None

def create_and_store(path):
    number = input(f"What is your favorite number? ")
    contents = json.dumps(number)
    path.write_text(contents)
    
path = Path("favorite_number.json")
number = get_stored_number(path)

if number:
    print(f"Your favorite number is {number}")
else:
    create_and_store(path)
    print(get_stored_number(path))
