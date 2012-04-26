from z3c.form import field

from five import grok

from plone.z3cform import layout
from plone.app.z3cform.wysiwyg import WysiwygFieldWidget

from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper

from ipnext.site.editablefooter.browser.interfaces import IFooterSettings
from ipnext.site.editablefooter import _


class FooterControlPanelForm(RegistryEditForm):
    grok.context(IFooterSettings)

    schema = IFooterSettings
    label = _(u"Footer control panel")

    #fields = field.Fields(IFooterSettings)
    def update(self):
        super(RegistryEditForm, self).update()


FooterControlPanelView = layout.wrap_form(
    FooterControlPanelForm, ControlPanelFormWrapper
)
