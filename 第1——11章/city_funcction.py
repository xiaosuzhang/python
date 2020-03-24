# coding=utf-8

def city_country(city,country,population=""):
    if population:
        name = city + "," + country + " - population " + str(population)
    else:
        name = city + "," + country
    
    return name
