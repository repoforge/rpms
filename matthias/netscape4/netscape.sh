#!/bin/sh

netscape=""

prefdir=$HOME/.netscape
prefcpck=$prefdir/nswrapper.copy_defs
pref=$prefdir/preferences.js
lipref=$prefdir/liprefs.js
b_opt="openBrowser"

prefix=$(dirname $(dirname $0))
sysname=`uname -m | sed "s|sparc64|sparc| ; s|^i[0-9]|i3|"`
if [ "$sysname" = "alpha" ]; then
   defs=""
else
   defs="-irix-session-management"
fi
defsrem="$defs -noraise -remote"

if echo $0 | grep 'navigator' >/dev/null; then
    netscape=$prefix/lib/netscape/netscape-navigator
elif echo $0 | grep 'communicator' >/dev/null ; then
    netscape=$prefix/lib/netscape/netscape-communicator
elif [ -x $prefix/lib/netscape/netscape-communicator ]; then
    netscape=$prefix/lib/netscape/netscape-communicator
elif [ -x $prefix/lib/netscape/netscape-navigator ]; then
    netscape=$prefix/lib/netscape/netscape-navigator
else
    echo "You don't seem to have netscape installed."
    exit 1

fi

procname=$netscape

if [ "$LANG" = "ja_JP.eucJP" -o "$LANG" = "ja_JP.ujis" -o "$LANG" = "ja_JP" -o "$LANG" = "ja" -o "$LANG" = "ko" -o "$LANG" = "ko_KR" -o "$LANG" = "ko_KR.eucKR" ]; then
   [ "$LD_PRELOAD" ] && NS_LD_PRELOAD="$LD_PRELOAD:"
   export NS_LD_PRELOAD="$LD_PRELOAD/usr/lib/netscape/ns_bogus_locale.so"
fi

if [ "$sysname" = "sparc" ]; then
   [ "$NS_LD_PRELOAD" ] && NS_LD_PRELOAD="$NS_LD_PRELOAD:"
   export NS_LD_PRELOAD="$NS_LD_PRELOADlibBrokenLocale.so.1"
fi

# This couldn't hurt.
export MOZILLA_LINUX_INSERT_LINK_FIX=1
export LD_ASSUME_KERNEL=2.2.5

# Exterminate zombie netscapes, and wipe stale lock file.
killstale () {

	user="`whoami`"
	ourpids="`/sbin/pidof $procname`"
	[ "$ourpids" != "" ] && ourpids=`ps u $ourpids | sed -n "s/^$user[ ]*\([^ ]*\)[ ].*/\1/p"`
	
	for p in $ourpids; do
		[ "$p" = "" ] && continue
		# int, quit, term, kill
		{ kill -2 $p && kill -3 $p && kill -15 $p && sleep 2 && kill -9 $p ; } >/dev/null 2>&1
	done

	[ -L "$HOME/.netscape/lock" ] && rm "$HOME/.netscape/lock"
	
	return 0
}

# Look for the correct index.html page
findlangfile() {
	if [ -z $1 ]; then
     		return
	fi
       
	LANGFILE=$1
	 
	if [ -z $LANG ]; then
		echo $LANGFILE
      		return 0
	fi
		 
	# Exact match: ex) ja_JP.eucJP -> ja_JP.eucJP
	MATCHEDFILE=$LANGFILE.$LANG
	if [ -e $MATCHEDFILE ]; then
		LANGFILE=$MATCHEDFILE
		echo $LANGFILE
		return 0
	fi
				 
	# No codeset match: ex) ja_JP.eucJP -> ja_JP
	MATCHEDFILE=$LANGFILE.`echo $LANG | sed 's/\.[^\.]*$//'`
	if [ -e $MATCHEDFILE ]; then
		LANGFILE=$MATCHEDFILE
		echo $LANGFILE
		return 0
	fi
					       
	# language name only match: ex) ja_JP.eucJP -> ja
	MATCHEDFILE=$LANGFILE.`echo $LANG | cut -b 1-2`
        if [ -e $MATCHEDFILE ]; then
		LANGFILE=$MATCHEDFILE
		echo $LANGFILE
		return 0
	fi
	echo $LANGFILE
	return 0
}							     


# Check the netscape lock file
checklock () {
	lock=`ls -l $HOME/.netscape/lock | awk '{ print $NF }'`
	# Don't check the IP address; it may have changed.
	#ipaddr=`echo $lock | awk -F : '{ print $1 }'`
	pid=`echo $lock | awk -F : '{ print $2 }'`
	#/sbin/ifconfig | grep -q "inet addr:$ipaddr" && \
	pids=`/sbin/pidof $procname`
	for apid in $pids ; do
	  [ "$pid" = "$apid" ] && return 0
	done
	killstale
	return 1
}

# Try calling existing netscape process with functions, else start one.
newbrowser () {
	[ $# -gt 0 ] && url=`echo $@ | sed 's/\ -[^ ]*//g; s/\( |	\)*//'`
	if [ -L "$HOME/.netscape/lock" ] && checklock; then
		idstr=
		id=`xwininfo -tree -root | grep Netscape: | head -1 | awk '{ print $1 }'`
		if [ -n "$id" ]; then
		     idstr="-id $id"
		fi
		if [ "$url" = "" ]; then
			$netscape $idstr $defsrem "xfeDoCommand($b_opt)" "$@" 2>/dev/null || \
			{ killstale && LD_PRELOAD=$NS_LD_PRELOAD exec $netscape $defs $cl_opt "$@" ; }
		else
			$netscape $idstr $defsrem "openURL($url,new-window)" 2>/dev/null || \
			{ killstale && LD_PRELOAD=$NS_LD_PRELOAD exec $netscape $defs $cl_opt "$@" ; }
		fi
	else
		if [ "$sysname" = "alpha" ]; then
		    # Hello, we're on an alpha.  Running Tru64 binaires.
		    # Running them in 31 bit address space.  Why do I crash
		    # if the drag window is still around from the last run of
		    # Netscape?  I'd better remove it...
		    OLDID=`xprop -root _MOTIF_DRAG_WINDOW | cut -d' ' -f 5`
		    xkill -id $OLDID > /dev/null 2>&1
		    xprop -root -remove _MOTIF_DRAG_WINDOW > /dev/null 2>&1 
		fi
		if [ "$url" = "" ]; then
			[ ${rerun:=0} -eq 1 ] && { sleep 3; $netscape $defsrem "openURL(,new-window)" '$@' 2>/dev/null ; } &
			    sleep 1
			    LD_PRELOAD=$NS_LD_PRELOAD exec $netscape $defs $cl_opt "$@"
		else
			    LD_PRELOAD=$NS_LD_PRELOAD exec $netscape $defs $cl_opt "$@"
		fi	
	fi
}

newopt () {
opt="$1"
shift
	case "$opt" in
		"+news"|"+discussions") b_opt="openNewsgroups"	; cl_opt="-discussions" ;;
		"+mail"|"+messenger")	b_opt="openInbox"	; cl_opt="-messenger"	;;
		"+edit"|"+composer")	b_opt="openEditor"	; cl_opt="-composer"	;;
		"+addr"|"+addresses")	b_opt="openAddrBook"	; cl_opt="-messenger -iconic"	; rerun=1	;;
		"+hist"|"+history")	b_opt="openHistory"	; cl_opt="-iconic"		; rerun=1	;;
		"+book"|"+bookmarks")	b_opt="openBookmarks"	; cl_opt="-iconic"		; rerun=1	;;
		"+mailto")		b_opt="composeMessage"	; cl_opt="-messenger -iconic"	; rerun=1	;;
		"+component-bar")	b_opt="toggleTaskbar"	; cl_opt="-component-bar";;
	esac
	newbrowser "$@"
}

oldopt () {
          LD_PRELOAD=$NS_LD_PRELOAD exec $netscape $defs "$@"
}

usage () {
	echo ""
	echo "Netscape Wrapper $ver, $ts"
	echo "        (c) 1998,1999 Dave Cinege, H. Peter Anvin, and Red Hat, Inc."
	echo ""
	echo "usage: netscape [ option ]"
	echo "  options:"
	echo ""
	echo "    [none]                Open new browser"
	echo "    [URL]                 Open new browser with URL"	 
	echo "    +news | +discussions  Show Collabra Discussions"
	echo "    +mail | +messenger    Show Messenger Mailbox (INBOX)"
	echo "    +edit | +composer     Open Composer"		
	echo "    +addr | +addresses    Show Address Book"
	echo "    +hist | +history      Open History window"
	echo "    +book | +bookmarks    Open Bookmarks windowsBook"
	echo "    +mailto               Open New Message window" 
	echo "    +component-bar        Show (detach) Component Lauch Bar"
	echo "    -[option]             Passed directly to Netscape binary"
	echo ""
	echo "The wrapper first attempts to open the option in a running"
	echo "netscape. If no netscape is running, one is executed with"
	echo "the option as the starting window."
	echo ""
	echo "Edit the top of this file to set default paths."
	echo ""
	echo ""
	echo "Netscape binary help:"
	echo ""
	exec $netscape "-help"
}

#
# Fix "locale" problems when printing to postscript
#
# If the locale uses a decimal separator other than a point printf 
# will return something other than 1.0
#

pnt=`printf "%1.1f" 1 2>/dev/null`
if [ "$pnt" != "1.0" ]; then
	export LC_NUMERIC=C		# Try a "safe" value for LC_NUMERIC.

	pnt=`printf "%1.1f" 1 2>/dev/null`
	if [ "$pnt" != "1.0" ]; then	#  LC_ALL is bad.
	 	LC_COLLATE=$LC_ALL	#  Set $LC_ALL for every category except
		LC_CTYPE=$LC_ALL	#  LC_NUMERIC, and then unset LC_ALL.
		LC_MESSAGES=$LC_ALL
		LC_MONETARY=$LC_ALL
		LC_TIME=$LC_ALL
		unset LC_ALL
		export LC_ALL LC_COLLATE LC_CTYPE LC_MESSAGES LC_MONETARY LC_CTIME
	fi
fi


# Make user copy of default files unless they already exist

if [ ! -f $prefcpck ]; then
	[ ! -d $prefdir ] && mkdir -p $prefdir
	pwd=`pwd`
	
	for pdir in $prefskel; do
		[ ! -d $pdir ] && continue
		cd $pdir
		for i in *; do
			[ ! -f $prefdir/$i ] && cp $i $prefdir/$i
   		done
	done
	
	touch $prefcpck		#safer, slower then this?   #echo -n "" >>$prefcpck 
    	cd $pwd
fi

# set up home page
HOMEPAGE=`findlangfile /usr/share/doc/HTML/index.html`
if [ -f $pref ]; then
    if egrep "\"browser.startup.(homepage|page)\"" \
    $pref > /dev/null; then
        HOMEPAGE=""
    fi
fi

# Hack the locale. This is so wrong. Netscape should really fix their crap.
for file in $pref $lipref ; do
   if grep -q "pab.locale" $file 2>/dev/null ; then
       cat $file | grep -v "pab.locale" > $file.new
       mv -f $file $file.old
       mv -f $file.new $file
   fi
done

# main

case "$1" in
	+*)	newopt "$@"; exit	;;
	-h|-help|--help) usage; exit	;;
	-*)	oldopt "$@"; exit	;;
	*)	[ -z "$*"  -a -n "$HOMEPAGE" ] && newbrowser "$HOMEPAGE" || newbrowser "$@"; exit	;;
esac	

echo "An error occurred running $netscape."
