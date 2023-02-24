import requests

# Set the base URL for the API
base_url = 'http://localhost:8000/api/'

# Set the login endpoint URL
login_url = base_url + 'login/'

# Set the username and password for the login request
data = {
    'username': 'john_doe',
    'password': 'password123'
}

# Make the login request
response = requests.post(login_url, data=data)

# Check if the login was successful
print(response)
