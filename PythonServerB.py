#!/usr/bin/env python

port = 9080

import sys
# your gen-py dir
sys.path.append('gen-py')

# MultiServer files
from MultiServer import *
from MultiServer.ttypes import *

# Thrift files
import os
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

# Server implementation
class MultiServerHandler:
    def ServerB(self, s):
        f = open('b.txt')
        content = f.read()
        f.close()
        f = open('b.txt','w')
        f.write(s)
        f.write(content)
        f.close()
        return "Server B Done"
        

# set handler to our implementation
handler = MultiServerHandler()

processor = MultiServer.Processor(handler)
transport = TSocket.TServerSocket(port = port)
tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

# set server
server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)

print 'Starting server'
server.serve()