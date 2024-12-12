def city_country_population(city, country, population=''):
    if population:
        info = f'{city}, {country}'
        pop = f'population {population}'
        return f'{info.title()} - {pop}'
    else: 
        info = f'{city}, {country}'
        return info.title()