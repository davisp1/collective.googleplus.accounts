# -*- coding: utf-8 -*-

import unittest2 as unittest

from plone.app.testing import TEST_USER_ID
from plone.app.testing import setRoles

from plone.registry.interfaces import IRegistry

from zope.component import getUtility

from collective.googleplus.accounts.config import PROJECTNAME
from collective.googleplus.accounts.testing import INTEGRATION_TESTING


class InstallTest(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']

    def test_installed(self):
        qi = getattr(self.portal, 'portal_quickinstaller')
        self.assertTrue(qi.isProductInstalled(PROJECTNAME))

    def test_registry_not_lost_on_reinstall(self):
        registry = getUtility(IRegistry)
        self.assertTrue('collective.googleplus.accounts' in registry)

        accounts = registry['collective.googleplus.accounts']
        self.assertEqual(accounts, None)

        accounts = {'test_key': "This is a test value"}
        registry['collective.googleplus.accounts'] = accounts

        qi = getattr(self.portal, 'portal_quickinstaller')
        qi.reinstallProducts(products=[PROJECTNAME])

        registry = getUtility(IRegistry)
        after_accounts = registry.get('collective.googleplus.accounts', None)
        self.assertEqual(accounts, after_accounts)


class UninstallTest(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.qi = getattr(self.portal, 'portal_quickinstaller')
        self.qi.uninstallProducts(products=[PROJECTNAME])

    def test_uninstalled(self):
        self.assertFalse(self.qi.isProductInstalled(PROJECTNAME))
