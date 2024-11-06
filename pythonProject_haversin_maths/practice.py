import math

def haversine(lat1, lon1, lat2, lon2):
    R = 6371000  # Radius of the Earth in meters
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)

    a = math.sin(delta_phi / 2.0) ** 2 + \
        math.cos(phi1) * math.cos(phi2) * \
        math.sin(delta_lambda / 2.0) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return R * c


if __name__ == "__main__":
    lat1, lon1 = 6.910306, +79.903944
    lat2, lon2 = 6.909583, +79.906333
    distance = haversine(lat1, lon1, lat2, lon2)
    distance_rounded = round(distance, 2)

    print(f"The distance between the points is {distance_rounded} meters.")
    print("distance in km = ", distance_rounded/1000)

    speed = (distance_rounded/(50)) * (18/5)
    print("speed in km/h = ", speed)

