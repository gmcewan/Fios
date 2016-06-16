import cPickle

from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor

from ServerClient import ServerClient


class SusbaintServer(DatagramProtocol):
    """
    Server for Susbaint. Servers manage subscriptions and route messages to
    clients.
    """

    def __init__(self):
        """

        """
        # the next client id to use
        self._current_client_id = 0
        # dictionary: {client_id: ServerClient}
        self._clients = {}
        # list of tuples: (subscription, client_id)
        self._subscription_list = []

    def datagramReceived(self, data, addr):
        """
        A client is sending information.

        Data is pickled.
        If data is an integer, it's a port number to send messages to a new
        client.
        If data is a dictionary, it is a notification to send on to clients.
        """
        # unencode the data
        print("received %r from %s" % (data, addr))
        unpickled_data = cPickle.loads(data)
        print("unpickled: " + str(unpickled_data))
        data_type = type(unpickled_data)
        print "type is " + str(data_type)
        if data_type == int:
            # new client connection - add to clients
            print "new client"
            client = ServerClient(addr[0], addr[1])
            self._clients[self._current_client_id] = client
            self._current_client_id += 1
            print self._clients
            print "------"
        elif data_type == dict:
            # notification
            print "notification"
            matched_clients = self.match_clients(unpickled_data)
            for client in matched_clients:
                client.send(self.transport, data)
        elif data_type == str:
            # subscription
            print "subscription"

    def match_clients(self, notification):
        return self._clients.values()


if __name__ == "__main__":
    # default port
    port_default = 2016
    reactor.listenMulticast(port_default, SusbaintServer(),
                            listenMultiple=True)
    reactor.run()
