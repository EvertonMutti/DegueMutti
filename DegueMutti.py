# -*- coding: utf-8 -*-
"""
Funções facilitadoras

Este módulo possui funções que visam melhorar e deixar mais prático o desenvol-
vimento de códigos rápidos, como funções para transforma números strings em nú-
meros como float e int, verificadores de tipo de número e aumento e diminuição
de porcentagem
"""
from re import findall

def StringToNumber(valor):
    """
    A função converterá o número string pro tipo que mais convém, podendo ser 
    int ou float
    ----------
    
    Parameters
    ----------
    valor : STRING
        
    Raises
    ------
    TypeError
        Ocorrerá um erro de tipo caso a string passada venha com "," ao invés
        de "." e caso seja passado outro tipo que não seja string.

    Returns
    -------
    Int or Float
        Será retornado a depender da string passada, se for uma string com pon
        to flutuante, será retornado float e Vice-versa.
        
    False
        Será retornado false caso não ocorra corretamente

    """
    try:
        if not valor.isnumeric() and findall(r'[.]', valor):
            valor = float(valor)
            return valor
        elif valor.isnumeric() and not findall(r'[.]', valor) :
            valor = int(valor)
            return valor
    except TypeError:
        raise TypeError('Não é possível converter o sua string para número, verifique o tipo')
        return False
     
def VerificaInt(n1):
    """
    Faz a mesma função do isinstance, só que sem o segundo parâmetro

    Parameters
    ----------
    n1 : Int
        O valor que será verificado.

    Returns
    -------
    bool
        Retornará True caso seja int e falso caso não seja.

    """
    if isinstance(n1, int):
        return True
    else:
        return False

def VerificaFloat(n1):
    """
    Faz a mesma função do isinstance, só que sem o segundo parâmetro.

    Parameters
    ----------
    n1 : Float
        O valor que será verificado.

    Returns
    -------
    bool
        Retornará True caso seja float e falso caso não seja.

    """
    if isinstance(n1, float):
        return True
    else:
        return False

def VerificaNumero(n1):
    """
    
    Parameters
    ----------
    n1 : Int or Float
    
    Returns
    -------
    bool
        True caso seja Float ou Int e falso caso não seja número.

    """
    return VerificaFloat(n1) or VerificaInt(n1)

def AumentaPorc(n1, porc = 1):
    """
    

    Parameters
    ----------
    n1 : TYPE
        DESCRIPTION.
    porc : TYPE, optional
        DESCRIPTION. The default is 1.

    Returns
    -------
    n1 : TYPE
        DESCRIPTION.

    """
    porc = porc / 100
    porc = 1 + porc
    n1 = n1 * porc
    return n1

def DiminuiPorc(n1, porc = 0):
    """
    

    Parameters
    ----------
    n1 : TYPE
        DESCRIPTION.
    porc : TYPE, optional
        DESCRIPTION. The default is 0.

    Returns
    -------
    n1 : TYPE
        DESCRIPTION.

    """
    porc = porc / 100
    porc = n1 * porc
    n1 = n1 - porc
    return n1



if __name__ == '__main__':
    print(round(AumentaPorc(100, 10)))
    print(round(DiminuiPorc(100, 15)))
    print(StringToNumber('2.5'))
    print(StringToNumber('2'))
    print(VerificaNumero(10))
    print(VerificaFloat(2.5))
    print(VerificaInt(5))



    