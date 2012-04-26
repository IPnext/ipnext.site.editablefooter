from z3c.form import field

from plone.z3cform import layout
from plone.app.z3cform.wysiwyg import WysiwygFieldWidget

from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper

from ipnext.site.editablefooter.browser.interfaces import IFooterSettings
from ipnext.site.editablefooter import _


class FooterControlPanelForm(RegistryEditForm):
    schema = IFooterSettings
    label = _(u"Footer control panel")

    # Replace the standard field widget with a nicer one
    fields = field.Fields(IFooterSettings)
    fields['footer'].widgetFactory = WysiwygFieldWidget

    def update(self):
        super(RegistryEditForm, self).update()


FooterControlPanelView = layout.wrap_form(
    FooterControlPanelForm, ControlPanelFormWrapper
)
