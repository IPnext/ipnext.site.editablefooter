import unittest2 as unittest

import transaction

from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.testing.z2 import Browser

from Products.CMFCore.utils import getToolByName

from ipnext.site.editablefooter.testing import EDITABLEFOOTER_INTEGRATION_TESTING

class TestSetup(unittest.TestCase):

    layer = EDITABLEFOOTER_INTEGRATION_TESTING

    def test__verify_installation(self):
        """Check if installed"""
        portal = self.layer['portal']
        tool = getToolByName(portal, 'portal_quickinstaller')
        self.assertTrue(tool.isProductInstalled('ipnext.site.editablefooter'))

    def test__registry_item_present(self):
        portal = self.layer['portal']
        tool = getToolByName(portal, 'portal_quickinstaller')
        self.assertTrue(False)

    def test__control_panel_configlet(self):
        import pdb; pdb.set_trace()
        self.assertTrue(False)
