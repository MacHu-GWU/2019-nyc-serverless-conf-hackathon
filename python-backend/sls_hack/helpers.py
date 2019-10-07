from uszipcode import SearchEngine

zipcode_search_engine = SearchEngine(simple_zipcode=True)


def find_zipcode_by_lat_lng(lat, lng):
    res = zipcode_search_engine.by_coordinates(lat, lng)
    zipcode = res[0].zipcode
    return zipcode


if __name__ == "__main__":
    lat, lng = 40.702962, -74.011626
    print(find_zipcode_by_lat_lng(lat, lng))
