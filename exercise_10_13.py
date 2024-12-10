from pathlib import Path
import json

def get_stored_username(path):
    """Obtém dados do usuário armazenado, se disponível"""
    if path.exists():
        contents = path.read_text()
        info = json.loads(contents)
        return info
    else:
        return None

def get_new_username(path):
    """Solicita dados do usuário"""
    name = input("What is your name?")
    age = input(f"What is your age {name}? ")
    fav_number = input("What is your favorite number? ")
    dictio = {"name" : name, "age": age, "number": fav_number}
    contents = json.dumps(dictio)
    path.write_text(contents)
    return dictio

def is_you(info):
    answer = input(f"Are you {info["name"]}? [y / n]  ")
    if answer.lower() == "y":
        return True
    else:
        return False

def info_user():
    """ Exibe informações do usuário."""
    path = Path('info_user.json')
    info = get_stored_username(path)
    if is_you(info):
        print(f"Welcome back, {info["name"]}!")
        print(f"Your age is {info["age"]}.")
        print(f"Your favorite number is {info["number"]}")
    else:
        info = get_new_username(path)
        print(f"We'll remember you when you come back, {info["name"]}")
        
info_user()