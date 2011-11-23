from zope.i18nmessageid import MessageFactory

_ = editablefooterMessageFactory = MessageFactory('ipnext.site.editablefooter')

def initialize(context):
    """Initializer called when used as a Zope 2 product."""
