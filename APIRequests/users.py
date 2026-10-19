# https://pypi.org/project/requests/
# pip install requests

import requests

response = requests.get('https://jsonplaceholder.typicode.com/users/1')

# print(r.status_code)

if response.status_code == 200:
    data = response.json()
    # print(data)

    print(data['id'])
    print(data['name'])
    print(data['email'])