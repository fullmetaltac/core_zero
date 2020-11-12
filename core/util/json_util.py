def json_search_by_key_val(obj, key, val):
    """
    Recursively search json object by key value pair
    :param key: key to search
    :param val: value to search
    :return: json object that matches search criteria or empty array
    """

    arr = []

    def extract(obj, arr, key, val):
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    extract(v, arr, key, val)
                elif k == key and obj[key] == val:
                    arr.append(obj)
        elif isinstance(obj, list):
            for item in obj:
                extract(item, arr, key, val)
        return arr

    values = extract(obj, arr, key, val)
    return values


def json_search_by_key(obj, key):
    """
    Recursively search json object by key value pair
    :param key: key to search
    :return: json object that matches search criteria or empty array
    """

    arr = []

    def extract(obj, arr, key):
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    extract(v, arr, key)
                elif k == key:
                    arr.append(obj)
        elif isinstance(obj, list):
            for item in obj:
                extract(item, arr, key)
        return arr

    values = extract(obj, arr, key)
    return values
