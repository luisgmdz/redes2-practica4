import http.client
import urllib.parse as urlparse
import argparse
import json


headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
foo = {'text': 'Hello HTTP'}
json_data = json.dumps(foo)


'''port=input("ingresa el puerto: ")
host=input("ingresa el host")'''
''
conn = http.client.HTTPConnection('localhost',8080)

print("GET\nHEAD\nPOST\nPUT\nDELETE\nCONNECT\nOPTIONS\nTRACE")

while True:    
    print("Escribe la peticion HTTP a enviar (en minusculas):\nctrl+c para salir")
    peticion=input()
    if peticion == 'get':
        conn.request("GET", "/")
        response = conn.getresponse()
        print("Status: ",response.status, " reason: ", response.reason)
    
    if peticion == 'head':
        conn.request("HEAD", "/")
        response = conn.getresponse()
        print("Status: ",response.status, " reason: ", response.reason)
    
    if peticion == 'post':
        conn.request('POST', '/', json_data, headers)
        response = conn.getresponse()
        print(response.read().decode())
        print("Status: ",response.status, " reason: ", response.reason)
    
    if peticion == 'put':
        conn.request("PUT", "/", json_data, headers)
        response = conn.getresponse()
        print("Status: ",response.status, " reason: ", response.reason)
    
    if peticion == 'delete':
        conn.request("DELETE", "/")
        response = conn.getresponse()
        print("Status: ",response.status, " reason: ", response.reason)
        print(response.read(200))

    if peticion == 'connect':
        conn.request("CONNECT", "/")
        response = conn.getresponse()
        print("Status: ",response.status, " reason: ", response.reason)
        print(response.read(200))

    if peticion == 'options':
        conn.request("OPTIONS", "/")
        response = conn.getresponse()
        print("Status: ",response.status, " reason: ", response.reason)
        print(response.read(200))

    if peticion == 'trace':
        conn.request("TRACE", "/")
        response = conn.getresponse()
        print("Status: ",response.status, " reason: ", response.reason)
        print(response.read(200))

conn.close()