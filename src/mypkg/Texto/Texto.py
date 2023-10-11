class Texto:
    def formatarTextoMinusculo(self, texto):
        return texto.lower()
    
    def formatarTextoMaiusculo(self, texto):
        return texto.upper()
    def inverterLetras(self, texto):
        return texto[::-1]
    def inverterPalavras(self, texto):
        return ' '.join(texto.split()[::-1])
    def inverterPalavrasELetras(self, texto):
        return ' '.join([palavra[::-1] for palavra in texto.split()[::-1]])
    