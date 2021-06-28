from .algo1 import strcmp

# Check both lengths of strings equals before use strcmp from algo1.py

def strcmpAlt(t, p):
    result = False
    if len(t) == len(p):
        result = strcmp(t, p)
    return result