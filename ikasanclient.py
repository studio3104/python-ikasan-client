import requests

class IkasanClient:
    def __init__(self, host, port = 4969):
        self.host = host
        self.port = port
        self.url = "http://%s:%d" % (host, port)

    def notice(self, channel, message, color = None, message_format = None):
        self.__request('notice', channel, message, color, message_format)

    def privmsg(self, channel, message, color = None, message_format = None):
        self.__request('privmsg', channel, message, color, message_format)

    def __request(self, method, channel, message, color, message_format):
        r = requests.post(
            "%s/%s" % (self.url, method),
            data = {
                'channel': channel,
                'message': message,
                'color': color,
                'message_format': message_format
            }
        )
