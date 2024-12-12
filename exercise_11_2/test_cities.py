from city_functions import city_country_population

def test_city_country():
    info = city_country_population('santiago', 'chile')
    assert info == 'Santiago, Chile'
    
def test_city_country_population():
    info = city_country_population('santiago', 'chile', 5000000)
    assert info == 'Santiago, Chile - population 5000000'
    
    