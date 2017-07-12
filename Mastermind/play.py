#!/usr/bin/python3
import sys
from mastermind import client
from mastermind import player

if sys.version_info < (3,0):
    sys.exit('Python version < 3.0 does not support modern TLS versions. You will have trouble connecting to our API using Python 2.X.')

client = client.Client('insert_email_here@gmail.com')
client.reset()
player = player.Player(client)
player.play()
