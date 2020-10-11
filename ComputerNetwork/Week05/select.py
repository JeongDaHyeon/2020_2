# from threading import Thread
import socket
import os
import select

def send_recv(client_socket):
    data = client_socket.recv(1024)
    print("client {}] {}".format(os.getpid(), data.decode()))
    response = "HTTP/1.1 200 OK\r\n"
    client_socket.send(response.encode('utf-8'))
    client_socket.send(data)
    client_socket.close()

def main(port):
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind(('', port))
    serversocket.listen(5)
    # start
    input_list= [serversocket]
    # end
    # th = None
    print("listening...")
    #serversocket.listen(5)

    # todo
    while True:
        input_ready, write_ready, except_ready = select.select(input_list, [], [])
        for ir in input_ready:
            if ir == serversocket:
                client, address = serversocket.accept()
                print("accept client from", address)
                input_ready.append(client)
                # send_recv(client)
            else:
                send_recv(ir)
                input_ready.remove(ir)
            #input_list.append(client)
            #ith = Thread(target = send_recv, args = (client,))
            #client_socket.append(client)
            #th.start()

if __name__=='__main__':
    port = 8888
    main(port)
