import socket
from cryptography.fernet import Fernet

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get the private IP address of the server
host = '172.31.44.162'

# set the port number
port = 1234

# bind the socket to the host and port
s.bind((host, port))

# set the server to listen for incoming connections
s.listen(5)

print(f"Server listening on {host}:{port}")

# accept incoming connections
conn, addr = s.accept()
print(f"Connected by {addr}")

# generate a new key for encryption/decryption
key = Fernet.generate_key()

# create a Fernet object with the key
f = Fernet(key)

# loop to send and receive messages
while True:
    # receive data from the client
    data = conn.recv(1024)

    # decrypt the data
    decrypted_data = f.decrypt(data)

    # convert the decrypted data to a string
    message = decrypted_data.decode()

    if not message:
        break
    print(f"Received encrypted message: {data}")
    print(f"Received decrypted message: {message}")

    # prompt the user to enter a response message
    response = input("Enter your response: ")

    # encrypt the response message
    encrypted_response = f.encrypt(response.encode())

    # send the encrypted response to the client
    conn.sendall(encrypted_response)

# close the connection
conn.close()
