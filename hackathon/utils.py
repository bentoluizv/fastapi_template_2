from ulid import ULID


def generate_ulid_as_str():
    ulid = ULID()
    return str(ulid)
