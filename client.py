import socket

def ler():
    data = None
    while not data:
        data = c.recv(4096).decode('utf8')                              #read function
    return data

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(('127.0.0.1', 1236))                                          #bind to ipv4 loopback address in a specific port
testdata = b'k' * 4096                                                  #data to send

done = False
state = 0
x = 2000
j = 1

while (done == False):
    if (state == 0):
        data = ler()
        if (data == "Start"):                                           #if the server said start, send data
            print("Delivery", j)
            j += 1
            state = 1
    
    if (state == 1): 
        state = 2         
        for i in range(1, x):
            c.send(testdata)                                            #send the test data x times 
        c.send("End".encode('utf8'))
    
    if (state == 2):
        data = ler()
        if (data == "Again"):                                           #if server said "again"
            x = x*10                                                    #we'll try and send more data (the same payload, but in a longer period of time)
            state = 0
        if (data == "Thanks"):                                          #if server thanks client
            delta = float(c.recv(4096).decode('utf8'))
            velocidade = str(c.recv(4096).decode('utf8'))               #the next thing server says is the speed of the connection 
            print(f"The delivery {j-1} took {delta} seconds")
            print(f"The speed is {velocidade} Gb/s")
            print(data)
            done = True

c.close()
