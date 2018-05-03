import socket



ip=raw_input("[=>>]Enter the target IP: ")
port=21

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect((ip,port))


print client.recv(4096)


user=raw_input("[=>>]Enter the USERNAME: ")
client.send("user %s\n"%user)

print client.recv(4096)


passw=raw_input("[=>>]Enter the PASSWORD: ")
client.send("pass %s\n"%passw)

print client.recv(4096)

ch=raw_input("[=>>]Want to enter the PASSIVE mode(Y/n): ")

if(ch=="Y" or ch =="y"):
    client.send("pasv\n")
    r = client.recv(4096)
    print r 
    
dp = r.split(',')
no = dp[5].split(')')
d_port = int(dp[4])*256 + int(no[0])



d_client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

d_client.connect((ip,d_port))


com=raw_input("[=>>]Enter the command to run: ") 
client.send("%s\n"%com)

print d_client.recv(4096)


