#!/usr/bin/env python

host = "localhost"
port = 9090

import sys

# your gen-py dir
sys.path.append('gen-py')

# MultiServer files
from MultiServer import *
from MultiServer.ttypes import *

# Thrift files 
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

try:

    # Init thrift connection and protocol handlers
    transport = TSocket.TSocket( host , port)
    transport = TTransport.TBufferedTransport(transport)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)

    # Set client to our MultiServer
    client = MultiServer.Client(protocol)

    # Connect to server
    transport.open()

    s = client.ServerA()
    print s

    # Close connection
    transport.close()

except Thrift.TException, tx:
    print 'Something went wrong : %s' % (tx.message)