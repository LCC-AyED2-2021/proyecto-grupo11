
def latinHash(caracter):
    '''
    # Esta funcion básicamente limita la funcion de python ord(), solo retornando valores numéricos...
    # ...cuando correspondan al conjunto de caracteres del Latin Básico y extendido (A) [Unicode code points]
    # https://en.wikipedia.org/wiki/List_of_Unicode_characters
    # En el caso de las letras, siempre devuelve el correspondiente a la Mayúscula
    # Esta funcion retorna valores entre [0,125] cuando recibe caracteres del Latin extendido B en adelante.
    # Si recibe valores correspondientes a estos sets, no los corrige para coincidir mayusculas y minusculas [126, ...]
    '''
    # Calcular primeramente el codigo unicode
    codigoOriginal = ord(caracter)

    # Definir el codigo hash resultante
    codigoFinal = None

    # Casos especiales ÿ, ÷, Set superior
    if codigoOriginal == 255:
        codigoFinal = 124
    elif codigoOriginal == 247:
        codigoFinal = 125
    elif codigoOriginal > 255:
        # Esta fuera del latin basico y extendido A. Se mantiene code point original - corrector de todos los anteriores
        codigoFinal = codigoOriginal - 130
    else:
        # Definir una variable correctora
        corrector = 33

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
