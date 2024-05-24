import time

tempo = 0

def iniciar_tempo():
    global tempo
    tempo = time.time()

def tempo_decorrido():
    total = time.time() - tempo
    minutos = int(total / 60)
    segundos = int(total - minutos * 60)
    return f"{minutos:02d}:{segundos:02d}"
