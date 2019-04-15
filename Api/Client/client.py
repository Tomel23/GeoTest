import requests

print("\tREST Api CLI\t")
print('sing in to app')

login = input("Login: ")
psw = input("Password: ")

def all_locations():
    result = requests.get("http://127.0.0.1:8000/",auth=(login, psw))

    print(result.text)


def create_location():
    name = input("Location name :")
    lon = float(input("longitude: "))
    lat = float(input("Latitude: "))
    result = requests.post(f"http://127.0.0.1:8000/add/{name}/{lon}/{lat}/",auth=(login, psw))
    print(result.text)


def find_closest_location():
    lon = float(input("longitude: "))
    lat = float(input("Latitude: "))
    result = requests.get(f"http://127.0.0.1:8000/closest_location/{lon}/{lat}/",auth=(login, psw))
    print(result.text)


def find_fixed_location():
    lon = float(input("longitude: "))
    lat = float(input("Latitude: "))
    dist = float(input("Distance: "))
    result = requests.get(f"http://127.0.0.1:8000/fixed_location/{lon}/{lat}/{dist}/",auth=(login, psw))
    print(result.text)


def controls(method_nr, **kwargs):
    methods = {
        0: all_locations,
        1: create_location,
        2: find_closest_location,
        3: find_fixed_location,
    }
    return methods.get(method_nr, 'wrong number, try again')()




response = requests.get('http://127.0.0.1:8000/', auth=(login,psw))

if response.ok:
    while True:
        print('Press 0 to print all location \n '
              'Press 1 to add location\n '
              'Press 2 to find closest location\n'
              'Press 3 to find all location in fixed distance')
        option=int(input("Selected option: "))
        controls(option)
else:
    print(response.raise_for_status())