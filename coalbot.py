import socket
import re 

server = "XXXXX.irc.slack.com"
channel = "TEST_CHANNEL"
bochannel ="CHANNEL"
botnick = "coalbot" 
password = "PASSWORD"
port = "6667"
jpattern = "([A-Z]{1,}-\d{1,})"

def ping(): 
  ircsock.send("PONG :pingis\n")  

def sendmsg(chan , msg):
  ircsock.send("PRIVMSG "+ channel +" :"+ msg +"\n") 

def joinchan(chan):
  ircsock.send("JOIN "+ channel +"\n")

def hello():
  ircsock.send("PRIVMSG "+ channel +" :Hello User!\n")

def isJira():
  ircsock.send("PRIVMSG "+ channel +" :thats a Jira Issue!\n")
                  
ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ircsock.connect((server, 6667))
ircsock.send("PASS "+ password + "\n") 
ircsock.send("USER "+ botnick +" "+ botnick +" "+ botnick +" :notification bot\n")
ircsock.send("NICK "+ botnick +"\n")

joinchan(channel)
joinchan(bochannel)

while 1:
  ircmsg = ircsock.recv(2048) 
  ircmsg = ircmsg.strip('\n\r') 
  print(ircmsg)

  #integrations went here. They are removed for reasons.  
  if ircmsg.find(":Hello") != -1: 
    hello()
  
  if re.search(jpattern, ircmsg): #!= -1:
    jiraString = re.search(jpattern, ircmsg)
    isJira()
  

