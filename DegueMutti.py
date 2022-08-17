# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 20:24:19 2022

@author: Everton SSD
"""
from re import findall

def StringToNumber(valor):
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
    if isinstance(n1, int):
        return True
    else:
        return False

def VerificaFloat(n1):
    if isinstance(n1, float):
        return True
    else:
        return False

def VerificaNumero(n1):
    return VerificaFloat(n1) or VerificaInt(n1)

def AumentaPorc(n1, porc = 1):
    porc = porc / 100
    porc = 1 + porc
    n1 = n1 * porc
    return n1

def DiminuiPorc(n1, porc = 0):
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



    