import requests

TENANT_ID = "4051366b-71d7-4355-b106-f85aa6c41c1f"
CLIENT_ID = "062fc81e-ba05-44c1-8cd3-33c3b8d22b46"
SCOPE = "api://f098827d-9521-4250-beda-f18963f1b624/.default"
CLIENT_SECRET = "Jh57Q~4DPdVipgT0cP6J9UD~6B0TFg4OI5Q9M"

# build out response to get access token from api
body = {
    'client_id': CLIENT_ID,
    'scope': SCOPE,
    'client_secret': CLIENT_SECRET,
    'grant_type': 'client_credentials'
}
uri = 'https://login.microsoftonline.com/'+TENANT_ID+'/oauth2/v2.0/token'
response = requests.post(uri, data=body).json()
access_token = response['access_token']

# build out response from local API, given the token above
localuri = 'http://localhost:5000/WeatherForecast'
headers = {
    'Accept': 'application/json',
    'Authorization': 'Bearer '+access_token
}
localresp = requests.get(localuri, headers=headers)
print(localresp.text)