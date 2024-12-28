import pytest
from employee import Employee

@pytest.fixture
def employee_data():
    """Esta fixture serve para que não seja necessário criar uma instância nova de Employee a cada teste. Obs.: função tem que ter o mesmo nome do valor de retorno + o @pytest.fixture antes dela."""
    employee_data = Employee('Henrique', 'Bisetto', 2000)
    return employee_data

def test_give_default_raise(employee_data):
    """ Testa a função give_raise() com valor default"""
    mensagem = employee_data.give_raise()
    assert mensagem == 'O novo salário de Henrique Bisetto é 7000'
    
def test_give_custem_raise(employee_data):
    """ Testa a função give_raise() com valor digitado"""
    mensagem = employee_data.give_raise(2000)
    assert mensagem == 'O novo salário de Henrique Bisetto é 4000'
