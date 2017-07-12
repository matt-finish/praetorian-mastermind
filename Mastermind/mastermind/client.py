#!/usr/bin/python3
import requests
import json

class Client:
    base_uri = 'https://mastermind.praetorian.com'
    header = {'Content-Type':'application/json'}
    
    def __init__(self, email):
        self.email = email
        self.get_auth_token()
    
    def get_auth_token(self):
        auth = requests.post(self.base_uri+'/api-auth-token/' , data={'email':self.email})
        self.header.update(auth.json())
    
    def start_level(self, level):
        resp = requests.get(self.base_uri+"/level/{0}/".format(level), headers=self.header)
        print(resp.json())
        return resp.json()
    
    def solve_level(self, level, guess):
        resp = requests.post(self.base_uri+"/level/{0}/".format(level), data=json.dumps({'guess': guess}), headers=self.header)
        print(resp.json())
        return resp.json()
    
    def hash(self):
        return requests.get(self.base_uri+'/hash/', headers=self.header).json()

    def reset(self):
        return requests.post(self.base_uri+'/reset/', headers=self.header).json()
