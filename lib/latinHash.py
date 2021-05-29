
def latinHash(caracter):
    '''
    # Esta funcion básicamente limita la funcion de python ord(), solo retornando valores numéricos...
    # ...cuando correspondan al conjunto de caracteres del Latin Básico y extendido (A) [Unicode code points]
    # https://en.wikipedia.org/wiki/List_of_Unicode_characters
    # En el caso de las letras, siempre devuelve el correspondiente a la Mayúscula
    # Esta funcion retorna valores entre [0,125], o None cuando es un input inválido
    '''
    # Calcular primeramente el codigo unicode
    codigoOriginal = ord(caracter)

    # Definir el codigo hash resultante
    codigoFinal = None

    # Definir una variable correctora
    corrector = 33

    # Casos especiales (ÿ & ÷)
    if codigoOriginal == 255:
        codigoFinal = 124
    elif codigoOriginal == 247:
        codigoFinal = 125
    else:
        # Verificar caso dentro del Latin Basico
        if codigoOriginal >= 33 and codigoOriginal <= 126:
            if codigoOriginal >= 97:
                corrector += 32
        # Caso latin extendido
        elif codigoOriginal >= 161 and codigoOriginal < 255:
            corrector += 66
            if codigoOriginal >= 224:
                corrector += 32
        
        # Calcular el codigo final
        codigoFinal = codigoOriginal - corrector

    # Retornar el codigo final
    return codigoFinal
