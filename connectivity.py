import socket

def can_connect(url):
    print(url)
    try:
        socket.create_connection((url, 443), 5)
        return True
    except socket.gaierror:
        return False
    except ConnectionRefusedError:
        return False


def is_connected_to_internet():
    reliable_addresses = [
        "www.google.com",
        "www.microsoft.com",
        "www.yahoo.com",
    ]
    return any(can_connect(a) for a in reliable_addresses)
