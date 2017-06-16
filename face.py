import http.client, urllib.request, urllib.parse, urllib.error, base64, json
import cognitive_face as CF
import pickle

from db import KEY
from camera import path

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
    f = open(path+filename, 'rb')
    data = postRequest('detect', f, contentType="octet-stream")
    try:
        faceid = data[0]['faceId']
    except:
        faceid = 1234567
    return faceid


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
    try:
        id = data[0]['candidates'][0]['personId']
    except:
        return "none"
    with open('id2person.pickle', 'rb') as f:
        id2person = pickle.load(f)
    return id2person[id]

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
        f = open(path+filename, 'rb')
        params = '/{}/persons/{}/persistedFaces'.format(groupId, personId[person])
        data = postRequest('persongroups', f, params, contentType='octet-stream')

def trainGroup(groupId):
    print('Train group {}'.format(groupId))
    params = '/{}/train'.format(groupId)
    data = postRequest('persongroups', params=params, getResponse=False)

def addDb(groupId):
    createGroup(groupId, 'test')
    personId = createPerson(groupId, ['kwei', 'chou'])
    with open('personId.pickle', 'wb') as f:
        pickle.dump(personId, f)
    names = ['kwei', 'chou']
    for name in names:
        addFace(groupId, personId, name, 
                [(name+str(i)+'.jpg') for i in range(9)])
    trainGroup(groupId)
    print(identify(groupId, 'kwei9.jpg'))
    print(personId['kwei'])
    print(identify(groupId, 'chou9.jpg'))
    print(personId['chou'])
    
def db():
    id2person = {}
    personId = None 
    with open('personId.pickle', 'rb') as f:
        personId = pickle.load(f)
    for key in personId.keys():
        id2person[personId[key]] = key
    with open('id2person.pickle', 'wb') as f:
        pickle.dump(id2person, f)


if __name__ == '__main__':
    print(identify(0, 'kwei9.jpg'))
