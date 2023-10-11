from Dificuldade import Dificuldade
path = 'FakeNameGenerator.csv'
csv = Dificuldade.read_csv(path)
def test_dificuldade():
    read_csv1 = Dificuldade.read_csv(path)
    assert read_csv1 is not None
    assert len(read_csv1) > 0

def test_removeNulos():
    remove_null_values1 = Dificuldade.remove_null_values(csv)
    assert remove_null_values1 is not None
    assert len(remove_null_values1) > 0

def test_remove_colunas():
    remove_columns = Dificuldade.remove_columns(csv, ['Password'])
    #printa o csv sem a coluna password
    assert remove_columns is not None
    assert len(remove_columns) > 0
    assert remove_columns.columns[5] == 'Password' # vai falhar pois a coluna password foi removida