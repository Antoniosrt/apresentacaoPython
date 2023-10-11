
class TesteCalculo:
    def test_soma(self):
        def soma(a, b):
            return a + b
        assert soma(2, 2) == 4
    
    def test_subtracao(self):
        def subtracao(a, b):
            return a - b
        assert subtracao(2, 2) == 0
    
    def test_multiplicacao(self):
        def multiplicacao(a, b):
            return a * b
        assert multiplicacao(2, 2) == 4
    
    def test_divisao(self):
        def divisao(a, b):
            return a / b
        assert divisao(2, 2) == 1
    
    def test_potencia(self):
        def potencia(a, b):
            return a ** b
        assert potencia(2, 2) == 4
        