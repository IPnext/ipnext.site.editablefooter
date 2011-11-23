from zope.component import queryUtility

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from plone.app.layout.viewlets.common import ViewletBase

from plone.registry.interfaces import IRegistry

from ipnext.site.editablefooter.browser.interfaces import IFooterSettings
from ipnext.site.editablefooter import _


class EditableFooterViewlet(ViewletBase):
    """
    An viewlet that reads the editable footer structured text from the
    registry, and renders it.
    """
    index = ViewPageTemplateFile('templates/footer.pt')
    
    def contents(self):
        """
        Retrive the structured contents from the Registry
        """
        registry = queryUtility(IRegistry)
        footer_text = u""
        if registry is None:
            pass
        else:
            settings = registry.forInterface(
                IFooterSettings, check=False
            )
            footer_text = getattr(settings, 'footer', footer_text)
        return footer_text