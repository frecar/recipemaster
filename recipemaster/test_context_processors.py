# -*- coding: utf-8 -*-
from django.test import TestCase, override_settings


class AnalyticsProcessorTest(TestCase):
    @override_settings(DEBUG=True)
    def test_debug_is_true(self):
        response = self.client.get('/accounts/login/?next=/recipes/')
        self.assertNotContains(response, 'analytics', status_code=200)

    @override_settings(DEBUG=False)
    @override_settings(ANALYTICS_ID='some code')
    def test_debug_is_false(self):
        response = self.client.get('/accounts/login/?next=/recipes/')
        self.assertContains(response, 'analytics', status_code=200)

    @override_settings(DEBUG=False)
    @override_settings(ANALYTICS_ID=None)
    def test_debug_false_no_code(self):
        response = self.client.get('/accounts/login/?next=/recipes/')
        self.assertNotContains(response, 'analytics', status_code=200)
