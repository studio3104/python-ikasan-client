import unittest
import requests
import httpretty
from ikasanclient import IkasanClient

@httpretty.activate
class IkasanClientTest(unittest.TestCase):
    __ikasan = { 'host': 'test.ikasan.com', 'port': 80, }
    __client = IkasanClient(__ikasan['host'], __ikasan['port'])

    def test_notice(self):
        httpretty.register_uri(httpretty.POST, "%s/%s" % (self.__client.url, 'notice'))
        r = self.__client.notice('#studio3104', 'hello')
        self.assertEqual(r.status_code, requests.codes.ok)

    def test_privmsg(self):
        httpretty.register_uri(httpretty.POST, "%s/%s" % (self.__client.url, 'privmsg'))
        r = self.__client.privmsg('#studio3104', 'hello')
        self.assertEqual(r.status_code, requests.codes.ok)
