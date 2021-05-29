import sys

# Leer los argumentos pasados por consola, verificar y ejecutar funciones

if len(sys.argv) == 3:
    if sys.argv[1] == '-create':
        # Ejecutar '-create'
        create()
    elif sys.argv[1] == '-search':
        # Ejecutar '-search'
        search()
    else:
        print(f'Los argumentos dados no son validos\nUse "-create <local_path>" o "-search <key_word>"')
else:
    print(f'Los argumentos dados no son validos\nUse "-create <local_path>" o "-search <key_word>"')


# Definir funciones principales

def create():
    return True


def search():
    return True

#test 123
#t

def hola():
    return False