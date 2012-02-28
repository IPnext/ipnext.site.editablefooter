from zope.interface import Interface
from zope import schema

from ipnext.site.editablefooter.config import TMPL_YEAR
from ipnext.site.editablefooter import _


class IFooterSettings(Interface):
    """Describes registry records
    """
    footer = schema.Text(
        title=_(u"Footer text"),
        description=_(
            u'Your footer text. You may also use the template variable %s' % TMPL_YEAR
        ),
        required=False,
    )
    
class IEditableFooterLayer(Interface):
    """A layer specific for this add-on product.

    This interface is referred in browserlayers.xml.
    """
