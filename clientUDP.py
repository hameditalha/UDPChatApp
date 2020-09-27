from colorama import Fore, Style                                #for styling and coloring
import socket                                                   #for communication
soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)          #TCP socket initiation
port = 1025                                                     #defining port to connect on
ip = '127.0.0.1'                                                #defining ip to connect with
while True:
    sen = input(f'{Fore.WHITE}> ')                              #taking message in to send
    sen = sen.encode()                                          #encoding to send
    soc.sendto(sen, (ip, port))                                 #sending to desired port and ip
    if sen.decode() == 'quit':                                  #quiting app on condition
        break
    recv, add = soc.recvfrom(1024)                              #recieving message
    recv = recv.decode()                                        #decoding recieved message
    print(f'{Fore.YELLOW}', add[0], 'on', add[1], '> ', recv)
    if recv == 'quit':                                          #quiting app on condition
        break
soc.close()                                                     #closing socket after use
print(f'{Fore.RED}Chat ended{Style.RESET_ALL}')