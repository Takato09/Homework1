import requests  # pip install requests

url = input("Enter address: ")


def status_code(u):
    try:
        response = requests.post(u)
        return response.status_code
    except requests.ConnectionError:
        return "404"
    except requests.exceptions.MissingSchema:
        return "Wrong pattern"


print(status_code(url))
