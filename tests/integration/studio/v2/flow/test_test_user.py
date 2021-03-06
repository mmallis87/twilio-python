# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base import serialize
from twilio.base.exceptions import TwilioException
from twilio.http.response import Response


class FlowTestUserTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.studio.v2.flows("FWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .test_users().fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://studio.twilio.com/v2/Flows/FWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/TestUsers',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "sid": "FWaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "test_users": [
                    "user1",
                    "user2"
                ],
                "url": "https://studio.twilio.com/v2/Flows/FWaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TestUsers"
            }
            '''
        ))

        actual = self.client.studio.v2.flows("FWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .test_users().fetch()

        self.assertIsNotNone(actual)

    def test_update_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.studio.v2.flows("FWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .test_users().update(test_users=['test_users'])

        values = {'TestUsers': serialize.map(['test_users'], lambda e: e), }

        self.holodeck.assert_has_request(Request(
            'post',
            'https://studio.twilio.com/v2/Flows/FWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/TestUsers',
            data=values,
        ))

    def test_update_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "sid": "FWaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "test_users": [
                    "user1",
                    "user2"
                ],
                "url": "https://studio.twilio.com/v2/Flows/FWaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TestUsers"
            }
            '''
        ))

        actual = self.client.studio.v2.flows("FWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .test_users().update(test_users=['test_users'])

        self.assertIsNotNone(actual)
