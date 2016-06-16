import cPickle

from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor



class Susbaint(DatagramProtocol):
    """
    Susbaint client. Create an instance of this class to send notifications and
    to subscribe.
    """
    
    def startProtocol(self):
        self.sendNotification()
        
    def stopProtocol(self):
        pass

    def sendNotification(self):
        """
        Sends a notification message.
        :param notification: Dictionary (key-value pairs) that is the message
        to send.
        """
        print("sending")
        # try sending a port number
        self.transport.write(cPickle.dumps(4096, -1), ('127.0.0.1', 2016))

        # try sending a notification dict
        notification = {3: 'yes', 5: 'no'}
        self.transport.write(cPickle.dumps(notification, -1),
                             ('127.0.0.1', 2016))

    def subscribe(self, subscription, callback):
        """
        Subscribes to content of notification messages. If a notification that
        matches the pattern is sent to the server, then the callback function
        will be called.
        :param subscription: The subscription pattern string
        :param callback: Function to call with the matching subscription. Must
        take a single dictionary argument
        :return: Returns a readonly Subscription object for reference
        """
        pass
    
    def datagramReceived(self, data, addr):
        print("received %s from %s" % (cPickle.loads(data), addr))

if __name__=="__main__":
    reactor.listenMulticast(4096, Susbaint(), listenMultiple=True)
    reactor.run()