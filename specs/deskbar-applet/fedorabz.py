from gettext import gettext as _

import deskbar
import gnomevfs

HANDLERS = {
	"FedoraBZHandler" : {
		"name": _("Fedora Bugzilla Entries"),
		"description": _("Open a Fedora Bugzilla entry by typing its number."),
	}
}

bzurl="https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=%s"

class FedoraBZMatch(deskbar.Match.Match):
	def __init__(self, backend, **args):
		deskbar.Match.Match.__init__(self, backend, **args)
				
	def action(self, text=None):
		gnomevfs.url_show(bzurl % self.name)
	
	def get_category(self):
		return 'websearch'
		
	def get_verb(self):
		return _("Open Fedora Bugzilla report <b>#%(name)s</b>")
				
class FedoraBZHandler(deskbar.Handler.Handler):
	def __init__(self):
		deskbar.Handler.Handler.__init__(self, "fedorabz.png")
		
	def query(self, query, max=5):
		if query.isdigit():
			return [FedoraBZMatch(self, name=query)]
		else:
			return []
