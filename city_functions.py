# test unittest
def get_city_country(city, country, *population):
    if population:
        city_attr = city.title() + ", " + country.title() + ' - ' + population[0].split('=')[0] + ' ' + \
                    population[0].split('=')[1]
    else:
        city_attr = city.title() + ", " + country.title()
    return city_attr
