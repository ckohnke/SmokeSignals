from googlevoice import Voice,util,settings
from googlevoice.util import input
import sys
import BeautifulSoup
from java.io import *
from java.lang import String
from no.swag.nsa.crypto import *

from twitter4j import *
from twitter4j.conf import *
import time

voice = Voice()
voice.login()

def encrypt(plainText, key):
    bf = Blowfish(key)
    return bf.encrypt(plainText)
  
def decrypt(cipherText, key):
    bf = Blowfish(key)
    return bf.decrypt(cipherText)

def postToTwitter(message):
    twitter = TwitterFactory.getSingleton()
    status = twitter.updateStatus(messge)
    #print "Successfully updated the status to [",status.getText(),"]."

def returnText(number, message):
    voice.send_sms(number, message)

def checkInbox():
    for message in voice.sms().messages:
        if not message.isRead:
            n=message.phoneNumber
            msgtxt = str(message.messageText)
            txtarray = msgtxt.split(" ")
            print txtarray
            
            if len(txtarray) > 2:
                e = String(txtarray[0])
                #print e
                key = txtarray[1]
                #print key
                code = ' '.join([str(x) for x in txtarray[2:len(txtarray)]])
                #print code
                if e.equalsIgnoreCase("encode"):
                    coded = encrypt(code, key)
                    #print "Coded message"
                    if len(coded) < 140:
                        postToTwitter(coded)
                        returnText(n, "Posted to Twitter: "+coded)
                    else:
                        returnText(n, "Coded message too long")
                elif e.equalsIgnoreCase("decode"):
                    uncoded = decrypt(code, key)
                    #print "Decoded message"
                    returnText(n, "Uncoded text: "+uncoded)
                else:
                    returnText(n, "Unable to parse input text message")
            message.delete()            
    time.sleep(10)

  
def main():
    while True:
        checkInbox()
        time.sleep(10)


if __name__ == '__main__':
  main()

