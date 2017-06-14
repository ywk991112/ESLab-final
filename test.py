import http.client, urllib.request, urllib.parse, urllib.error, base64, json
import cognitive_face as CF

from db import KEY, person2Id

photoDir = './photo/'
def createGroup():
    headers = {
        # Request headers
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': KEY,
    }
    body = {"name": "test"}
    body = json.dumps(body)
    # try:
    conn = http.client.HTTPSConnection('westcentralus.api.cognitive.microsoft.com')
    conn.request("PUT", '/face/v1.0/persongroups/244', body, headers)
    response = conn.getresponse()
    # data = response.read().decode('utf-8')
    # data = json.loads(data)
    # conn.close()
    # print(data)

if __name__=='__main__':
    createGroup()
