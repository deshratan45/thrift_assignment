#!/usr/bin/env python

port = 9090
host = "localhost"

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

def callB(lines):
    try:
        # Init thrift connection and protocol handlers
        transportA = TSocket.TSocket( host , 9080)
        transportA = TTransport.TBufferedTransport(transportA)
        protocolA = TBinaryProtocol.TBinaryProtocol(transportA)

        # Set client to our MultiServer
        clientA = MultiServer.Client(protocolA)

        # Connect to server
        transportA.open()

        s = clientA.ServerB(lines)
        print s

        # Close connection
        transportA.close()

    except Thrift.TException, tx:
        print 'Something went wrong : %s' % (tx.message)
        return "Problem in calling server B"
    return "Server A Done"

# Server implementation
class MultiServerHandler:
    def ServerA(self):
        f = open('a.txt','r+')
        a = f.readlines()
        if len(a) < 9:
            return "text is small "
        else:
            b = a[len(a)-10:]
            callB(''.join(b))
            f.seek(len(a)-9)
            f.truncate()
            return "done"
    
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