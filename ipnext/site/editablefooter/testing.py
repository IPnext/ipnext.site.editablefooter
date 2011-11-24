from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting

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
        applyProfile(portal, 'ipnext.site.editablefooter:default')

    def tearDownZope(self, app):
        z2.uninstallProduct(app, 'ipnext.site.editablefooter')


EDITABLEFOOTER_FIXTURE = EditableFooterTestingLayer()
EDITABLEFOOTER_INTEGRATION_TESTING = IntegrationTesting(
    bases=(EDITABLEFOOTER_FIXTURE,),
    name="EditableFooterTestingLayer:Integration",
)

