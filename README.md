SmokeSignals
============

Send encrypted text messages through Twitter.

To use text the google voice number in the following format:
 - ACTION KEY MESSAGE

where ACTION is either encode (to encrypt a message and post to Twitter) or decode (to recieve a text back that decrypts a message). KEY is the cipher's key used for encryption or decryption. MESSAGE is the message you want to encrypt or decrypt.

In all cases, the program will text the user back with the success or failure of the program.

Dependencies:
  - python googlevoice API.
  - no-swag toolkit: personal Java toolkit that includes wrapping classes for encryption and decryption.
  - twitter4j: Twitter API used for posting to Twitter.

NOTE: The googlevoice python API used in this code had to be modified to compile. Good luck. lib/googlevoice contains the modified version of the API.
