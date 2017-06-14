import http.client, urllib.request, urllib.parse, urllib.error, base64, json
import cognitive_face as CF

from db import KEY, person2Id

photoDir = './photo/'
def postRequest(service, body={}, params="", contentType="json", method="POST", getResponse=True):
    headers = {
        # Request headers
        'Content-Type': 'application/' + contentType,
        'Ocp-Apim-Subscription-Key': KEY,
    }
    body = json.dumps(body) if (contentType == "json") else body
    try:
        conn = http.client.HTTPSConnection('westcentralus.api.cognitive.microsoft.com')
        conn.request(method, '/face/v1.0/{}{}'.format(service, params), body, headers)
        response = conn.getresponse()
        if getResponse:
            data = response.read().decode('utf-8')
            data = json.loads(data)
            conn.close()
            return data
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

def detect(filename):
    f = open(photoDir+filename, 'rb')
    data = postRequest('detect', f, contentType="octet-stream")
    return data[0]['faceId']

# faceId: str
def identify(groupId, filename):
    faceId = detect(filename)
    body = {    
        "personGroupId":str(groupId),
        "faceIds":[
            faceId
        ],
        "maxNumOfCandidatesReturned":1,
        "confidenceThreshold": 0.5
    }

    data = postRequest('identify', body)    
    # return data
    return data[0]['candidates'][0]['personId']

def createGroup(groupId, name):
    print('Create group with id {}'.format(groupId))
    body = { "name": name }
    params = '/' + str(groupId)
    data = postRequest('persongroups', body, params, method="PUT", getResponse=False)
    
def deleteGroup(groupId):
    print('Delete group with id {}'.format(groupId))
    params = '/' + str(groupId)
    data = postRequest('persongroups', params=params, method="DELETE", getResponse=False)

def createPerson(groupId, nameList):
    personId = {}
    for name in nameList:
        print('Create person with name {} in group id {}'.format(name, groupId))
        body = { "name": name }
        params = '/{}/persons'.format(groupId)
        data = postRequest('persongroups', body, params)
        personId[name] = data['personId']
    return personId

def addFace(groupId, personId, person, filenameList):
    for filename in filenameList:
        print('Photo {} add to {}\'s database in group {}'.format(filename, person, groupId))   
        f = open(photoDir+filename, 'rb')
        params = '/{}/persons/{}/persistedFaces'.format(groupId, personId[person])
        data = postRequest('persongroups', f, params, contentType='octet-stream')

def trainGroup(groupId):
    print('Train group {}'.format(groupId))
    params = '/{}/train'.format(groupId)
    data = postRequest('persongroups', params=params, getResponse=False)

if __name__ == '__main__':
    createGroup(888, 'test')
    personId = createPerson(888, ['lian', 'chin', 'tom'])
    addFace(888, personId, 'lian', ['lian1.jpg', 'lian2.jpg'])
    addFace(888, personId, 'chin', ['chin1.jpg', 'chin2.jpg'])
    addFace(888, personId, 'tom', ['tom1.jpg', 'tom2.jpg'])
    trainGroup(888)
    print(identify(888, 'lian3.jpg'))
    print(personId['lian'])
    print(identify(888, 'chin3.jpg'))
    print(personId['chin'])
    print(identify(888, 'tom3.jpg'))
    print(personId['tom'])
    deleteGroup(888)
