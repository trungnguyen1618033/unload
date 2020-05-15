import urllib3
import json
import urllib.request
import requests
from auth import get_auth_token

repo_id = 'd2dcd681-4a32-4a9d-a6e8-fe41340e4193'
url_upload = 'https://sync.admicro.vn/api2/repos/{0}/upload-link/'.format(repo_id)


def upload(token, upload_file, upload_dir):
    headers = {
        'Authorization': 'Token {token}'.format(token=token)
    }
    # get upload link
    upload_link = requests.get(url_upload, headers=headers).json()

    # upload
    upload_data = {
        'filename': upload_file[upload_file.rfind('/') + 1:],
        'parent_dir': upload_dir
    }
    response = requests.post(
        upload_link,
        data=upload_data,
        files={'file': open(upload_file, 'rb')},
        headers=headers
    )

    print('Upload result: ', response)


if __name__ == "__main__":
    token = get_auth_token()

    upload(token, '/storage/gender_cls/celeb_ntt/dnb-facerecognition-aivivn/datasets/aligned.tar',
           '/DataSet/celeb_ntt/')
