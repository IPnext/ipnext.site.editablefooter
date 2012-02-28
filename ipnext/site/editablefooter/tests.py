from datetime import date

import unittest2 as unittest

import transaction

from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID, logout
from plone.testing.z2 import Browser

from AccessControl import Unauthorized
from Products.CMFCore.utils import getToolByName
from zope.component import getUtility
from plone.registry.interfaces import IRegistry

from ipnext.site.editablefooter.config import TMPL_YEAR
from ipnext.site.editablefooter.browser.interfaces import IFooterSettings
from ipnext.site.editablefooter.testing import EDITABLEFOOTER_INTEGRATION_TESTING

class TestSetup(unittest.TestCase):

    layer = EDITABLEFOOTER_INTEGRATION_TESTING

    def test__verify_installation(self):
        """Check if installed"""
        portal = self.layer['portal']
        tool = getToolByName(portal, 'portal_quickinstaller')
        self.assertTrue(tool.isProductInstalled('ipnext.site.editablefooter'))

    def test__registry_item_present(self):
        """Check if the registry setting is stored on installation"""
        portal = self.layer['portal']
        registry = getUtility(IRegistry)
        settings = registry.forInterface(IFooterSettings)
        self.assertTrue(TMPL_YEAR in settings.footer)
        
    def test__footer_controlpanel_view_protected(self):
        """The control panel view should be protected"""
        portal = self.layer['portal']
        logout()
        self.assertRaises(
            Unauthorized, portal.restrictedTraverse, '@@footer-controlpanel'
        )

    def test__footer_in_view(self):
        """Test the rendering of the custom footer"""
        portal = self.layer['portal']
        browser = Browser(portal)
        portalURL = portal.absolute_url()
        browser.open(portalURL)
        # Also test for template variable replacement
        test_fragment = "2000-%s" % date.today().year 
        self.assertTrue(test_fragment in browser.contents)
