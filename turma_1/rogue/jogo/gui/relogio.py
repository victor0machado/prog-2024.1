import time

class Relogio:
    def iniciar(self):
        self.inicio = time.time()

    def medir_tempo(self):
        tempo_decorrido = time.time() - self.inicio
        minutos = int(tempo_decorrido // 60)
        segundos = int(tempo_decorrido - minutos * 60)
        return f"{minutos:02d}:{segundos:02d}"

    def exportar(self):
        return {
            "inicio": self.inicio,
            "atual": time.time()
        }

    def importar(self, dados):
        self.inicio = time.time() - (dados["atual"] - dados["inicio"])

relogio = Relogio()
