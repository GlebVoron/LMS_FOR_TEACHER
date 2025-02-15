def spn(json_response):
    l_p = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["boundedBy"]["Envelope"][
        "lowerCorner"]
    r_p = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["boundedBy"]["Envelope"][
        "upperCorner"]
    l_p = list(map(float, l_p.split()))
    r_p = list(map(float, r_p.split()))

    delta1 = str(abs(l_p[0] - r_p[0]))
    delta2 = str(abs(l_p[1] - r_p[1]))

    return ",".join([delta1, delta2])