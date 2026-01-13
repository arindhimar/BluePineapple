import math

def calculate_distance(lat1, lon1, lat2, lon2):
    R = 6371.0

    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return R * c


lat1 = int(input("Enter latitude 1"))
lat2 = int(input("Enter latitude 2"))
lon1 = int(input("Enter longtitude 1"))
lon2 = int(input("Enter longtitude 20"))

print(calculate_distance(lat1,lon1,lat2,lon2))