from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from pyftpdlib import filesystems
import sys, os

pasta = "share/"

authorizer = DummyAuthorizer()
authorizer.add_anonymous(pasta)
handler = FTPHandler
handler.authorizer = authorizer
address = ("127.0.0.1", 2121)
ftpd = FTPServer(address, handler)
ftpd.serve_forever()

print(filesystems.os.listdir(pasta))
