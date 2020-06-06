import socket
import sys

PORT = 80

try:
    HOST = socket.gethostbyname('www.facebook.com')
    print("Host resolved successfully")
except socket.gaierror:
    print("There was an error resolving the host")
    sys.exit()

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket created successfully")
except socket.error as err:
    print(err)

s.connect((HOST, PORT))
print('Successfully connected to IP Address == ', HOST)
