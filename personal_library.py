import sys

# Leer los argumentos pasados por consola, verificar y ejecutar funciones

if len(sys.argv) == 3 and False:
    if sys.argv[1] == '-create':
        # Ejecutar '-create'
        create()
    elif sys.argv[1] == '-search':
        # Ejecutar '-search'
        search()
    else:
        print(f'Los argumentos dados no son válidos.\nUtilice "-create <local_path>" o "-search <key_word>"')
else:
    print(f'Los argumentos dados no son válidos.\nUtilice "-create <local_path>" o "-search <key_word>"')


# Definir funciones principales

def create():
    return True


def search():
    return True

# Test
from lib import trie
T = trie.Trie
trie.insert(T,'hola')
for i in range(1123):
    print('hi')