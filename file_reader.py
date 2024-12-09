from pathlib import Path

# path  = Path('text_files/pi_digits.txt')
# contents = path.read_text()
# # contents = contents.rstrip() # remover o espaço em branco da última linha
# # print(contents)

# lines = contents.splitlines()
# for line in lines:
#     print(line)

path = Path('text_files/pi_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''

for line in lines:
    pi_string += line

print(pi_string)
print(len(pi_string))