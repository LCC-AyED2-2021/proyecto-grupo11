from lib import mymath
import sys, os

# https://docs.python.org/3/tutorial/modules.html#executing-modules-as-scripts ''executing-modules-as-scripts''

# Verify arguments from console to execute corresponding task
if len(sys.argv) == 3:
    if sys.argv[1] == '-create':
        # Execute create fn
        create()
    elif sys.argv[1] == '-search':
        # Execute search fn
        search()
    else:
        print(f'Invalid argument.\nUse "-create <local_path>" or "-search <key_word>"')
else:
    print(f'Invalid argument.\nUse "-create <local_path>" or "-search <key_word>"')


# Define functions

def create():
    return True


def search():
    return True

#hola Lucas

#xd si son en tiempo real

#otro test xd