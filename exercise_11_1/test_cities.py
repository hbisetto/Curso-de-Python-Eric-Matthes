from city_functions import city_country

def test_city_country():
    santi = city_country('santiago', 'chile')
    assert santi == 'Santiago, Chile'
    
