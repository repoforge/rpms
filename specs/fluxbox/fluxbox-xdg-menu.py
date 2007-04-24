#!/usr/bin/env python
# vim: noexpandtab:ts=4:sts=4

"""Menu Generator for Fluxbox

Generates a menu for Fluxbox using the freedesktop.org standards

Usage: fluxbox-xdg-menu.py [options]

Options:
  -l ..., --lang=...      create the menu using a language. Default = $LANG
  -h, --help              show this help
  -f ..., --file=...      output the menu into a file. Default = ~/.fluxbox/menu
  -t ..., --theme=...     what icon theme you want to use
  --with-icons            put icons for applications in the menu
  --stdout                output the menu to standard output
  --submenu               output to be used as an include/submenu with fluxbox
  --with-backgrounds      creates a background menu. Default background_paths = 
                          ~/.fluxbox/backgrounds, /usr/share/wallpapers,
                          /usr/share/backgrounds
  --backgrounds-only      do not regenerate menu, only do the bg menu.
  --bg-path=              path to location to look for images 
                          example: --bg-path=~/pics  
			  may be used with --backgrounds-only but --bg-path= 
			  must be first: --bg-path=~/some/path --backgrounds-only

A nice example string to use: fluxbox-fdo-menugen.py --with-icons --with-backgrounds --bg-path=~/some/path
To update only the backgrounds: fluxbox-fdo-menugen.py --bg-path=~/some/path --backgrounds-only
"""

__author__ = "Rudolf Kastl , Antonio Gomes, Michael Rice"
__version__ = "$Revision: 1.2 $"
__date__ = "$Date: 2006/10/21 09:38:14 $"
__license__ = "GPL"


import os,re,sys,glob,getopt
import xdg.Menu,xdg.DesktopEntry,xdg.IconTheme
from os.path import isfile

def usage():
	print __doc__

def header(wm="fluxbox"):
	return """
[begin] (Fluxbox)
	[exec] (Web Browser) {htmlview}
	[exec] (Email) {evolution}
	[exec] (Terminal) {$TERM}
	[exec] (Irc) {xchat}
	[separator]\n"""

def footer(wm="fluxbox"):
	return """
	[submenu] (Fluxbox Menu)
		[config] (Configure)
		[submenu] (System Styles) {Choose a style...}
			[stylesdir] (/usr/share/fluxbox/styles)
			[stylesdir] (/usr/share/commonbox/styles/)
		[end]
		[submenu] (User Styles) {Choose a style...}
			[stylesdir] (~/.fluxbox/styles)
		[end]
		[workspaces]   (Workspace List)
		[submenu] (Tools)
			[exec] (Window name) {xprop WM_CLASS|cut -d \" -f 2|xmessage -file - -center}
			[exec] (Screenshot - JPG) {import screenshot.jpg && display -resize 50% screenshot.jpg}
			[exec] (Screenshot - PNG) {import screenshot.png && display -resize 50% screenshot.png}
			[exec] (Run) {fbrun }
			[exec] (Regen Menu) {fluxbox-generate_menu --with-icons}
		[end]
		[submenu] (Window)
			[restart] (kde) {startkde}
			[restart] (openbox) {openbox}
			[restart] (gnome) {gnome-session}
		[end]
		[exec] (Lock screen) {xscreensaver-command -lock}
		[commanddialog] (Fluxbox Command)
		[reconfig] (Reload config)
		[restart] (Restart)
		[separator]
		[exit] (Exit)
	[end]
[end]\n"""	

def checkWm(entry, wm="fluxbox"):
	if entry.DesktopEntry.getOnlyShowIn() != []:
		entry.Show = False
	if entry.DesktopEntry.getNotShowIn() != []:
		if isinstance(entry, xdg.Menu.MenuEntry):
			if wm in entry.DesktopEntry.getNotShowIn():
				entry.Show = False
			else:
				entry.Show = True 
	
def findIcon(icon, theme):
	"""Finds the path and filename for the given icon name
		e.g. gaim --> /usr/share/pixmaps/gaim.png
		e.g. fart.png --> /usr/share/pixmaps/fart.png
	"""
	retval=str(xdg.IconTheme.getIconPath(icon, 48, theme))
	if retval == "None":
		retval=""

	return (retval + "").encode('utf8')

def parseMenu(menu,wm,use_icons,theme,depth=1):
	if use_icons:
		print "%s[submenu] (%s) <%s> " % ( (depth*"\t"), menu.getName().encode('utf8'),  findIcon(menu.getIcon(), theme) )
	else:
		print "%s[submenu] (%s) " % ( (depth*"\t"), menu.getName().encode('utf8'), )
	depth += 1
	for entry in menu.getEntries():
		if isinstance(entry, xdg.Menu.Menu):
			parseMenu(entry,wm,use_icons,theme,depth)
		elif isinstance(entry, xdg.Menu.MenuEntry):
			checkWm(entry,wm)
			if entry.Show == False: continue
			if use_icons:
				print "%s[exec] (%s) {%s} <%s> " % ( (depth*"\t"), entry.DesktopEntry.getName().encode("utf8"), entry.DesktopEntry.getExec().split()[0], findIcon(entry.DesktopEntry.getIcon(), theme) )
			else:
				print "%s[exec] (%s) {%s} " % ( (depth*"\t"), entry.DesktopEntry.getName().encode("utf8"), entry.DesktopEntry.getExec().split()[0] )
		elif isinstance(entry,xdg.Menu.Separator):
			print "%s[separator]" % (depth*"\t")
		elif isinstance(entry.xdg.Menu.Header):
			print "%s%s" % ( (depth*"\t"), entry.Name )
	depth -= 1
	print "%s[end]" % (depth*"\t")

def get_bgimgs_and_parse(xPath):
    try:
        if isfile(os.path.expanduser("~/.fluxbox/bgmenu")) == True:
            os.unlink(os.path.expanduser("~/.fluxbox/bgmenu"))
    except OSError:
        pass
    h = {}
    bg_paths =["~/.fluxbox/backgrounds","/usr/share/wallpapers",
		"/usr/share/backgrounds","/usr/share/backgrounds/images"]
    try:
        if xPath == None:
           pass
        else:
            bg_paths.append(xPath)
    except(TypeError):
        pass
    for dir in bg_paths:
        for imgpth in bg_paths:
            try:
                imgs = os.listdir(os.path.expanduser(imgpth))
                for i in imgs:
                    h[i] = imgpth
            except (OSError):
                pass
    bgMenu = open(os.path.expanduser("~/.fluxbox/bgmenu"),'w+')
    num = len(h)
    countNum = 1
    bgPagCk = 1
    bgPgNum = 1
    bgMenu.write( "[submenu] (Backgrounds)\n" )
    bgMenu.write( "[submenu] (Backgrounds) {Set Your Background}\n" )
    bgMenu.write("\t[exec]  (Random Image)  {fbsetbg -r ~/.fluxbox/backgrounds}\n")
	types = ["png","jpg","jpeg","gif"]
    for i in h.keys():
	    try:
		    t = i.split(".")[-1].lower()
			if t in types:
			    print "Hello"
			    bgMenu.write( "\t[exec]\t("+ i +") {fbsetbg -f "+ h[i] + "/" + i +"}\n" )
				countNum = countNum + 1
				num = num - 1
				bgPagCk = bgPagCk + 1
				if bgPagCk == 26:
				    bgPgNum = bgPgNum + 1
					bgMenu.write("[end]\n[submenu] (Backgrounds " + str(bgPgNum) +") \
						{Set Your Background}\n")
					bgPagCk = 1
				if num == 0:
				    bgMenu.write( "[end]\n[end]\n" )
					bgMenu.close()
		except(KeyError):
		    print h[i]
		    pass

def main(argv):
# Setting the default values
	wm = "fluxbox"
	file = "~/.fluxbox/menu"
	use_icons = False
    use_bg = False
    bg_Xpath = False
	theme = "gnome"
	lang = os.getenv("LANG","C")
	file = os.path.expanduser("~/.fluxbox/menu")
	do_submenu = False
	use_stdout = False
	
	try:
		opts, args = getopt.getopt(argv, "hf:dl:d", ["help","lang=","file=","with-icons","stdout",\
			"theme=","submenu","with-backgrounds","backgrounds-only","bg-path="])

	except getopt.GetoptError:
		usage()
		sys.exit(2)
	for opt, arg in opts:
		if opt in ("-h", "--help"):
			usage()
			sys.exit()
		elif opt in ("-l", "--lang"):
			lang = arg
		elif opt in ("-f", "--file"):
			file = os.path.expanduser(arg)
		elif opt == '--with-icons':
			use_icons = True
		elif opt in ("-t", "--theme"):
			theme = arg
		elif opt == '--stdout':
			use_stdout = True
		elif opt == '--stdout':
			file = sys.stdout
		elif opt == '--bg-path':
		    bg_Xpath = True
			xPath = os.path.expanduser(arg)
		elif opt == '--with-backgrounds':
		    use_bg = True
		elif opt == '--backgrounds-only':
		    if bg_Xpath:
			    get_bgimgs_and_parse(xPath)
			else:
			    get_bgimgs_and_parse(None)
				raise SystemExit
			  
		elif opt == '--submenu':
			do_submenu = True

	if not use_stdout:
		fsock = open(file,'w')
		saveout = sys.stdout
		sys.stdout = fsock

	menu=xdg.Menu.parse()
# is done automatically now
#	menu.setLocale(lang)

	if not do_submenu:
        print header()
	parseMenu(menu,wm,use_icons,theme)
	if not do_submenu and use_bg and bg_Xpath:
	    get_bgimgs_and_parse(xPath) 
	    print "[include] (~/.fluxbox/bgmenu)"
	if not do_submenu and use_bg and not bg_Xpath:
	    print "[include] (~/.fluxbox/bgmenu)"
		get_bgimgs_and_parse(None)
    if not do_submenu:
        print footer()
	if not use_stdout:
		sys.stdout = saveout

#	print menu
if __name__ == "__main__":
	main(sys.argv[1:])
