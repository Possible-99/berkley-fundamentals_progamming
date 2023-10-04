from math import sqrt

    
def make_city(name , lat , lon):
    return [name , lat , lon]

def get_lat(city):
    return city[2]

def get_lon(city):
    return city[1]

def get_name(city):
    return city[0]


def distance(city_1, city_2):
    """
    >>> city1 = make_city('city1', 0, 1)
    >>> city2 = make_city('city2', 0, 2)
    >>> distance(city1, city2)
    1.0
    """
    "*** YOUR CODE HERE ***"
    lat1, lon1 = get_lat(city_1) , get_lon(city_1)
    lat2, lon2 = get_lat(city_2) , get_lon(city_2)

    return sqrt((lat1 - lat2) ** 2 +  (lon1 + lon2) ** 2)


def closer_city(lat, lon, city1, city2):
    """ Returns the name of either city1 or city2, whichever is closest
        to coordinate (lat, lon).

        >>> berkeley = make_city('Berkeley', 37.87, 112.26)
        >>> stanford = make_city('Stanford', 34.05, 118.25)
        >>> closer_city(38.33, 121.44, berkeley, stanford)
        'Stanford'
        >>> bucharest = make_city('Bucharest', 44.43, 26.10)
        >>> vienna = make_city('Vienna', 48.20, 16.37)
        >>> closer_city(41.29, 174.78, bucharest, vienna)
        'Bucharest'
    """
    "*** YOUR CODE HERE ***"
    city3 = make_city("city3" , lat , lon)
    dis1 = distance(city1 , city3)
    dis2 = distance(city2 , city3)
    if dis1 < dis2:
        return get_name(city1)
    return  get_name(city2)


def make_politician(name, party , age):
    return {"name": name , "party":party , "age": age}

def get_name(politician):
    return politician["name"]

def get_party(politician):
    return politician["party"]

def get_age(politician):
    return politician["age"]

    
p = make_politician("Frida" , "repub" , 22)
print(get_name(p))
print(get_party(p))
print(get_age(p))