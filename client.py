import requests

#Try GET for all
resp = requests.get('http://localhost:5050/api/v1/advs/').json()


#Try POST
resp = requests.post('http://localhost:5050/api/v1/advs/',
                          json={"author": "Test",
                                "title": "test",
                                "description": "test"})


# Try GET by id
resp = requests.get('http://localhost:5050/api/v1/adv/1').json()



#Try DELETE by id
response = requests.delete('http://localhost:5050/api/v1/adv/3')
