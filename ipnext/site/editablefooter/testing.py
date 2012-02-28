from plone.app.testing import PloneSandboxLayer
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting

from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID, TEST_USER_NAME, login

from plone.testing import z2

from zope.configuration import xmlconfig

class EditableFooterTestingLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import ipnext.site.editablefooter
        self.loadZCML(package=ipnext.site.editablefooter)
        z2.installProduct(app, 'ipnext.site.editablefooter')

    def setUpPloneSite(self, portal):
        self.applyProfile(portal, 'ipnext.site.editablefooter:default')
        setRoles(portal, TEST_USER_ID, ['Manager'])
        login(portal, TEST_USER_NAME)
        setRoles(portal, TEST_USER_ID, ['Site Administrator']) 
       
    def tearDownZope(self, app):
        z2.uninstallProduct(app, 'ipnext.site.editablefooter')


EDITABLEFOOTER_FIXTURE = EditableFooterTestingLayer()
EDITABLEFOOTER_INTEGRATION_TESTING = IntegrationTesting(
    bases=(EDITABLEFOOTER_FIXTURE,),
    name="EditableFooterTestingLayer:Integration",
)