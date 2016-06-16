# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 13:48:05 2016

@author: gregormcewan
"""

class ServerClient:
    """
    Representation of a client on the server side
    """

    def __init__(self, hostname, port):
        self.hostname = hostname
        self.port = port

    def send(self, transport, pickled_notification):
        """
        Sends a notification to this client.
        """
        transport.write(pickled_notification, (self.hostname, self.port))
