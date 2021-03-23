import socket
import datetime

def ler():
    data = None
    while not data:
        data = client.recv(4096).decode('utf8')                                     #read function
    return data

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 1236))                                                         #bind to ipv4 loopback address in a specific port
s.listen(0)

client, porta = s.accept()

done = False
state = 0

while (done == False):
    if(state == 0):
        client.send("Start".encode('utf-8'))                                        #allows the client to start transmitting
        state = 1
    if(state == 1):
        inicio = datetime.datetime.now()
        state = 2 
        x = True
        count = 0
        while (x == True):
            data = client.recv(4096)
            if (data.decode('utf8') == "End"):                                      #says to the client to stop transmitting
                x = False
            if data:
                count += len(data)
                del data
                continue

    if (state == 2):
        fim = datetime.datetime.now()
        print("Beginning: ", inicio)
        print("Ending: ", fim)
        delta = fim - inicio                                                        #time that took to transmit
        delta = delta.seconds + delta.microseconds / 1000000.0
        print(f"Time difference: {delta}s")
        if (delta < 3):
            state = 3
            print("Not enough! Need more data\n")                                         #ITS EXPECTING ATLEAST 3 SECONDS OF DATA FROM THE CLIENT SIDE
        else: state = 4
    
    if (state == 3):
        client.send("Again".encode('utf8'))
        state = 0

    if (state == 4):
        client.send("Thanks".encode('utf8'))
        client.send(str(delta).encode('utf8'))
        velocidade = count*8 / 1000000000 / delta                                   #transmission speed -> byte/ssecond to gigabits/second
        client.send(str(velocidade).encode('utf8'))
        print(f'Time used: {delta}s')
        print(f'Speed: {velocidade} Gb/s')
        done = True

s.close()
