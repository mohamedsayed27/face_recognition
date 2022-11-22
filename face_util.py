from urllib.request import urlopen
import requests

import face_recognition as fr


def fetch_photos(url: str):
    response = requests.request("GET", url)
    myjson = response.json()
    return myjson['data']


def compare_faces(photo: str, url: str):
    image2 = fr.load_image_file(urlopen(photo))
    image2_encoding = fr.face_encodings(image2)[0]
    photos = fetch_photos(url)
    for x in photos:
        image1 = fr.load_image_file(urlopen(x['url']))
        image1_encoding = fr.face_encodings(image1)[0]
        results = fr.compare_faces([image1_encoding], image2_encoding)
        if results[0]:
            return {'match': True, 'id': x['id']}
        else:
            continue
    return {'match': False}
