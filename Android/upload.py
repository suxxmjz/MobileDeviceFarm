import requests


def uploadAd(fp, ip_address, latitude, longitude, epoch_time, source):
    url = "http://206.12.95.145:3000/ad"
    
    files = {'ad': open(fp, 'rb')}
    print(files)
    
    multipart_form_data = {
        'ad': ('ad.png', open(fp, 'rb')),
        'ip_address': (None, ip_address),
        'platform': (None, 'MOBILE'),
        'type': (None, 'STATIC'),
        'latitude': (None, latitude),
        'longitude': (None, longitude),
        'source': (None, source),
        'time_stamp':  (None, str(epoch_time))
    }

    
#     print(json.dumps(payload))

    response = requests.post(url, files=multipart_form_data)
#     response.raise_for_status()
#     print(response.error)
    print(response.json())
    print(response.text)