class Subscription:
    """A subscription belonging to a particular client connection.

    Contains one subscription string and one callback reference. The object is handed
    to the client connection when subscribing and is readonly."""