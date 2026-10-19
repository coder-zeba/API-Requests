import requests
response = requests.get('https://v2.jokeapi.dev/joke/Programming')
if response.status_code == 200:
    joke = response.json()
    # print(joke)
    print("-------------------------------------------------------")
    if joke['type'] == "single":
        print("Joke: ",joke['joke'])
    else:
        print("Setup:",joke['setup'])
        print("Delivery: ",joke['delivery'])
    print("-------------------------------------------------------")