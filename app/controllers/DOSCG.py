import googlemaps

from flask import jsonify, current_app, render_template
from flask_caching import Cache

cache = Cache()


@cache.cached(timeout=600)
def func1():
    """
    Returns the value of X, Y and Z from series
    X, Y, 5, 9, 15, 23, Z
    Returns:
        ans (dict): The dictionary contains value of X, Y and Z
    """

    series = {}
    n = 7
    for i in range(1, n + 1):
        series[i] = (i * i) - 3 * i + 5

    ans = {}
    ans["X"] = series[1]
    ans["Y"] = series[2]
    ans["Z"] = series[7]
    return jsonify(ans)


@cache.cached(timeout=600)
def func2():
    """
    Returns the value of B and C when
    A = 21
    B = 23 - A
    C = -21 - A

    Returns:
        ans (dict): The dictionary contains value of B and C
    """
    A = 21

    ans = {}
    ans["B"] = 23 - A
    ans["C"] = -21 - A
    return jsonify(ans)


@cache.cached(timeout=60)
def func3():
    """
    Returns the best way to go to Central World from SCG Bangsue
    Returns:
        ans (dict): The dictionary contains the best way to go to Central World from SCG Bangsue
                    and the data from Google Direction API
    """
    origin = "SCG สำนักงานใหญ่ บางซื่อ 1 Siam Cement Alley, Bang Sue, Bangkok 10800"
    dest = "centralwOrld, 999/9 Rama I Rd, Pathum Wan, Pathum Wan District, Bangkok 10330"

    gmaps = googlemaps.Client(key=current_app.config["GOOGLE_CREDENTIAL"])
    modes = ["transit", "driving"]
    link = "https://www.google.com/maps/dir/?api=1&origin=scg+bangsue&origin_place_id=ChIJe5WIpnOc4jARoEQ-IqXo9HA&destination=Central+World+Thailand&destination_place_id=ChIJ4VX0ws-e4jARBGaQ2IACrcQ&travelmode="

    ans = {}
    duration = None
    for mode in modes:
        distance_res = gmaps.distance_matrix(origin, dest, mode=mode)

        element = distance_res["rows"][0]["elements"][0]
        if element.get("status") != "OK":
            continue

        duration = element["duration"]["value"]
        if not ans.get("duration") or duration < ans.get("duration"):
            ans["mode"] = mode
            ans["duration"] = duration
            ans["link"] = link + mode

    return jsonify(ans)


@cache.cached(timeout=600)
def resume():
    return render_template("resume.html")


@cache.cached(timeout=600)
def index():
    return render_template("index.html")
