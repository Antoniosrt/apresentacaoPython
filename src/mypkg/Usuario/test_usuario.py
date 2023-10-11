
from Usuario import Usuario
def testar_email_valido():
    
    assert Usuario.validarEmail('email@test.com') == True
    assert Usuario.validarEmail('aa@aa.com') == True
    assert Usuario.validarEmail('sapdla') == True # Teste falha aqui
    assert Usuario.validarEmail('sapdla') == False
