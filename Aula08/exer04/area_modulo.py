from math import pi

def area_tri(base, altura):
    """
        Retorna área do triângulo
    """
    return (base * altura) / 2

def area_ret(lado1, lado2):
    """
        Retorna área do retângulo
    """
    return lado1 * lado2

def area_qua(lado):
    """
        Retorna área do quadrado
    """
    return lado ** 2

def area_cir(raio):
    """
        Retorna área do círculo
    """
    return pi * (raio ** 2)

if __name__ == '__main__':
    area_cir(2,2)