import Texto

def test_formatarTextoMinusculo():
    texto = Texto.Texto()
    assert texto.formatarTextoMinusculo('TEXTO') == 'texto'

def test_formatarTextoMaiusculo():
    texto = Texto.Texto()
    assert texto.formatarTextoMaiusculo('texto') == 'TEXTO'

def test_inverterLetras():
    texto = Texto.Texto()
    assert texto.inverterLetras('texto') == 'otxe' # esse falha pois falta t no final   
 
def test_inverterPalavras():
    texto = Texto.Texto()
    assert texto.inverterPalavras('texto invertido') == 'invertido texto'

def test_inverterPalavrasELetras():
    texto = Texto.Texto()
    assert texto.inverterPalavrasELetras('texto invertido') == 'oditrevni otxet'