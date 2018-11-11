# minimalistic client example from 
# https://github.com/seprich/py-bson-rpc/blob/master/README.md#quickstart

import socket
from bsonrpc import JSONRpc
from bsonrpc.exceptions import FramingError
from bsonrpc.framing import (
    JSONFramingNetstring, JSONFramingNone, JSONFramingRFC7464)
import json
from node import *

# Cut-the-corners TCP Client:

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 50001))

rpc = JSONRpc(s, framing_cls=JSONFramingNone)
server = rpc.get_peer_proxy()

leaf1 = node("leaf1")
leaf2 = node("leaf2")

root = node("root", [leaf1, leaf1, leaf2])

print("graph before increment")
root.show()

# do this increment remotely:
increment(root)

print("graph after increment")
root.show()

# Get list from node class
print("Dictionary to send")
dictionaryToSend = listToSend(root)
print(dictionaryToSend)

# Grab dictionary form node class
dictionaryToSend = listToSend(root)
# Turn dictionary into json string
json_string = json.dumps(dictionaryToSend)
# Send over data using NOPs
server.nop(json_string)
print(server.nop(json_string))

# Execute in server:
result = server.swapper('Hello World!')
# "!dlroW olleH"

rpc.close()  # Closes the socket 's' also
