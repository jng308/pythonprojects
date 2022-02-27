
from socket import *



def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect(mailserver, port)
    
    recv = clientSocket.recv(1024).decode()
    #print(recv)
    #if recv[:3] != '220':
        #print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1)
    #if recv1[:3] != '250':
        #print('250 reply not received from server.')

    # Send MAIL FROM command and print server response.

    MailfromCommand = 'MAIL FROM: <alice@crepes.fr> \r\n'
    clientSocket.send(MailfromCommand.encode())
    recv2 = clientSocket.recv(1024).decode()
    #print(recv1)
    #if recv1[:3] != '250':
        #print('250 reply not received from server.')


    # Send RCPT TO command and print server response.

    RCPTCommand = 'RCPT TO: <> \r\n'
    clientSocket.send(RCPTCommand.encode())
    recv3 = clientSocket.recv(1024).decode()
    #print(recv1)
    #if recv1[:3] != '250':
        #print('250 reply not received from server.')


    # Send DATA command and print server response.

    DATACommand = 'DATA'
    clientSocket.send(DATACommand.encode())
    recv4 = clientSocket.recv(1024).decode()
    #print(recv1)
    #if recv1[:3] != '250':
        #print('250 reply not received from server.')


    # Send message data.

    MessageCommand = 'Sending Message JG \r\n'
    clientSocket.send(MessageCommand.encode())
    recv5 = clientSocket.recv(1024).decode()
    #print(recv1)
    #if recv1[:3] != '250':
        #print('250 reply not received from server.')


    # Message ends with a single period.

    PeriodCommand = '.'
    clientSocket.send(PeriodCommand.encode())
    recv6 = clientSocket.recv(1024).decode()
    #print(recv1)
    #if recv1[:3] != '250':
        #print('250 reply not received from server.')


    # Send QUIT command and get server response.
    # Fill in start
    QuitCommand = 'QUIT'
    clientSocket.send(QuitCommand.encode())
    recv7 = clientSocket.recv(1024).decode()
    #print(recv1)
    #if recv1[:3] != '250':
       # print('250 reply not received from server.')
    # Fill in end
    
    

if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
SMTP_Server_skeleton.py
Displaying SMTP_Server_skeleton.py.


