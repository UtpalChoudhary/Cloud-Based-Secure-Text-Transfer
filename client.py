import socket
from cryptography.fernet import Fernet

HOST = '13.232.156.81'  # The remote host
PORT = 1234  # The same port as used by the server
BUFFER_SIZE = 1024

# Establish connection to server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
print("Connected to server")

# Receive encryption key from server
key = s.recv(BUFFER_SIZE)

# Create Fernet object for encryption/decryption
f = Fernet(key)

# Send and receive messages with server
while True:
    # Encrypt and send message to server
    message = input("Enter your message: ")
    encrypted_message = f.encrypt(message.encode())
    s.sendall(encrypted_message)

    # Receive and decrypt the reply from the server
    data = s.recv(BUFFER_SIZE)
    decrypted_data = f.decrypt(data)
    print('Encrypted message:', data.decode())
    print('Decrypted message:', decrypted_data.decode())

    # print("Server reply:", decrypted_data.decode())

# Close the socket
s.close()