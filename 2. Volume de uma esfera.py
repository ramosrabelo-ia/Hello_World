def volume_esfera(raio: float) -> float:
    pi = 3.14
    volume = (4 / 3) * pi * raio ** 3
    return volume


print(volume_esfera(5))