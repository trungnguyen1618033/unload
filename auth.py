import urllib3
import json
import urllib.request
import requests
import urllib.parse

url_auth = 'https://sync.admicro.vn/api2/auth-token/'
login_credential = {
    'username': 'tuyennguyenthanhanh@admicro.vn',
    'password': 'Kh0ngbietnua@123'
}


def get_auth_token():
    response = requests.post(url_auth, login_credential)
    the_page = response.content.decode('utf-8')
    token = json.loads(the_page)['token']
    return token
