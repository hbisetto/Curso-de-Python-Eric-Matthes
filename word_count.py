from pathlib import Path

def count_words(path):
    """ Conta o número aproximado de palavras em um arquivo """
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        # print(f'Sorry, the file {path} does not exist.')
        pass # fail silently
    else:
        # Conta o número aproximado de palavras no arquivo
        words = contents.split()
        num_words = len(words)
        print(f'The file {path} has about {num_words} words.')
        
filenames = ['alice.txt', './text_files/siddhartha.txt', 'moby_dick.txt', './text_files/little_women.txt']

for filename in filenames:
    path = Path(filename)
    count_words(path)