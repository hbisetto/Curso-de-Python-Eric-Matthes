from pathlib import Path

def ler(path):
    """ Recebe um parâmetro path que é  localização do arquivo a ser lido """
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f'Me desculpe, o caminho {path} não foi encontrado.')
        
    else:
        names = contents.split()
        for name in names:
            print(name)
            
gatos = Path('cats.txt')
cachorros = Path('dogs.txt')
print("Nomes de gatos:")
ler(gatos)
print("Nomes de cachorros:")
ler(cachorros)