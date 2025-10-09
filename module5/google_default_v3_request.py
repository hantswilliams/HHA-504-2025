import requests 

url = "https://hants-pythontest-507-714433739872.europe-west1.run.app"

## these argument keys, must match the source code of where you deployed the application
arguments = {
    "first_name": "Hants",
    "last_name": "Williams",
    "age": 30,
    "wbc": 5.5
}

# Make the GET request with the arguments
response = requests.get(url, params=arguments)

# Print the response from the server
print(response.text)