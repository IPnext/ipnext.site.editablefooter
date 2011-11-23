from zope.interface import Interface
from zope import schema

from ipnext.site.editablefooter import _


class IFooterSettings(Interface):
    """Describes registry records
    """
    footer = schema.Text(
        title=_(u"Footer text"),
        description=_(u"Your footer text"),
    )
