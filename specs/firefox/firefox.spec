# $Id$
# Authority: dag

### Builds on RH73, but doesn't work.
##DistExclude: rh73

# Tag: test

%{?dist: %{expand: %%define %dist 1}}

%{?rh7:%define _without_autoconf213 1}
%{?rh7:%define _without_freedesktop 1}
%{?rh7:%define _without_gtk2 1}
%{?el2:%define _without_autoconf213 1}
%{?el2:%define _without_freedesktop 1}
%{?el2:%define _without_gtk2 1}
%{?rh6:%define _without_autoconf213 1}
%{?rh6:%define _without_freedesktop 1}
%{?rh6:%define _without_gtk2 1}

Summary: Mozilla Firefox web browser
Name: firefox
Version: 0.9
Release: 1
License: MPL/LGPL
Group: Applications/Internet
URL: http://www.mozilla.org/projects/firefox/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/firefox-source-%{version}.tar.bz2
Patch2: mozilla-1.4-x86_64.patch
Patch3: mozilla-xremote.patch
Patch4: mozilla-xremote-0.5.patch
Patch5: mozilla-xremote-stfu.patch
Patch1001: firefox-0.8-gtk2xtbin.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: XFree86-devel, zlib-devel, zip, perl,
BuildRequires: libpng-devel, libmng-devel, libjpeg-devel
BuildRequires: ORBit-devel, gcc-c++
%{!?_without_autoconf213:BuildRequires: autoconf213}
%{?_without_autoconf213:BuildRequires: autoconf = 2.13}
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}
%{!?_without_gtk2:BuildRequires: gtk2-devel, libIDL-devel}
%{?_without_gtk2:BuildRequires: gtk+-devel}

Obsoletes: phoenix, MozillaFirebird, mozilla-firebird, mozilla-firefox

%description
Mozilla Firefox is an open-source web browser, designed for standards
compliance, performance and portability.

%prep
%setup -n mozilla
%ifarch x86_64
%patch2 -p1
%endif
%patch3 -p0
%patch4 -p0
%patch5 -p0
%patch1001

%{__cat} <<EOF >bookmarks.html
<!DOCTYPE NETSCAPE-Bookmark-file-1>
<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">
<TITLE>Bookmarks</TITLE>
<H1>Bookmarks</H1>

<DL><p>
    <DT><H3 PERSONAL_TOOLBAR_FOLDER="true" ID="NC:PersonalToolbarFolder">Personal Toolbar Folder</H3>
    <DL><p>
        <DT><A HREF="http://dag.wieers.com/apt/">Dag Apt Repository</A>
        <DT><A HREF="http://www.google.com/">Google</A>
        <DT><A HREF="http://www.mozilla.org/projects/firefox/">Firefox Project</A>
        <DT><A HREF="http://www.redhat.com/">Red Hat</A>
    </DL><p>
    <HR>
    <DT><H3 ID="NC:BookmarksRoot#$40f75202">RPMS</H3>
    <DL><p>
	<DT><A HREF="http://atrpms.physik.fu-berlin.de/">ATrpms</A>
        <DT><A HREF="http://dag.wieers.com/apt/">Dag Apt Repository</A>
        <DT><A HREF="http://freshrpms.net/">FreshRPMS</A>
	<DT><A HREF="http://newrpms.sunsite.dk/">NewRPMS</A>
        <DT><A HREF="http://rpm.pbone.net/">RPM PBone search</A>
	<DT><A HREF="http://www.rpmseek.com/">RPMSeek search</A>
    </DL><p>
    <DT><H3 ID="NC:BookmarksRoot#$40f75201">News</H3>
    <DL><p>
        <DT><A HREF="http://freshmeat.net/">Freshmeat.net</A>
        <DT><A HREF="http://news.google.com/">Google news</A>
        <DT><A HREF="http://linuxtoday.com/">LinuxToday news</A>
        <DT><A HREF="http://lwn.net/">Linux Weekly News</A>
        <DT><A HREF="http://slashdot.org/">Slashdot: News for nerds, stuff that matters</A>
        <DT><A HREF="http://www.theregister.co.uk/">The Register</A>
    </DL><p>
    <DT><H3 ID="NC:BookmarksRoot#$16f2309b">Mozilla Project</H3>
    <DL><p>
        <DT><A HREF="http://www.mozilla.org/">The Mozilla Organization</A>
        <DT><A HREF="http://www.mozilla.org/get-involved.html">Getting Involved</A>
        <DT><A HREF="http://www.mozilla.org/feedback.html">Feedback</A>
        <DT><A HREF="http://www.mozilla.org/docs/">Documentation</A>
        <DT><A HREF="http://www.mozillazine.org/">MozillaZine</A>
    </DL><p>
    <HR>
</DL><p>
EOF

### FIXME: Shouldn't the default firefox config be part of original source ?
%{__cat} <<EOF >.mozconfig
export MOZ_PHOENIX="1"
export PATH="$PATH"
mk_add_options MOZ_PHOENIX="1"
mk_add_options PATH="$PATH"
ac_add_options --host="%{_host}"
ac_add_options --build="%{_build}"
ac_add_options --target="%{_target_platform}"
ac_add_options --x-libraries="%{_prefix}/X11R6/%{_lib}"
ac_add_options --disable-composer
ac_add_options --disable-debug
ac_add_options --disable-debug-modules
ac_add_options --disable-dtd-debug
ac_add_options --disable-freetype2
ac_add_options --disable-freetypetest
ac_add_options --disable-gtktest
ac_add_options --disable-installer
ac_add_options --disable-jsd
ac_add_options --disable-ldap
ac_add_options --disable-mailnews
ac_add_options --disable-tests
ac_add_options --disable-xprint
ac_add_options --enable-crypto
ac_add_options --enable-extensions="default,-irc,-venkman"
#ac_add_options --enable-extansions="cookie,p3p,pref,transformiix,typeaheadfind,universalchardet,wallet,webservices,xmlextras,xml-rpc"
ac_add_options --enable-mathml
ac_add_options --enable-optimize="%{optflags}"
ac_add_options --enable-plaintext-editor-only
ac_add_options --enable-reorder
ac_add_options --enable-strip
ac_add_options --enable-strip-libs
ac_add_options --enable-xinerama
ac_add_options --with-pthreads
ac_add_options --with-system-jpeg
ac_add_options --with-system-mng
ac_add_options --with-system-png
ac_add_options --with-system-zlib
ac_add_options --without-system-nspr
%{?_without_gtk2:ac_add_options --disable-xft}
%{?_without_gtk2:ac_add_options --enable-default-toolkit="gtk"}
%{!?_without_gtk2:ac_add_options --enable-xft}
%{!?_without_gtk2:ac_add_options --enable-default-toolkit="gtk2"}
EOF

%{__cat} <<EOF >firefox.desktop
[Desktop Entry]
Name=Firefox Web Browser
Comment=Browse the Internet
Exec=firefox
Icon=firefox.png
Terminal=false
Type=Application
StartupNotify=true
MimeType=text/html;text/x-java;inode/directory;application/xhtml+xml;
Categories=Application;Network;
EOF

%{__cat} <<'EOF' >firefox.sh
#!/bin/sh

### Written by Dag Wieers <dag@wieers.com>
### Please send suggestions and fixes to me.

ulimit -c 0

MOZILLA_FIVE_HOME="%{_libdir}/firefox"
MOZ_PROGRAM="$MOZILLA_FIVE_HOME/firefox"

LD_LIBRARY_PATH="$MOZILLA_FIVE_HOME:$MOZILLA_FIVE_HOME/plugins:$LD_LIBRARY_PATH"
MOZ_PLUGIN_PATH="$HOME/.mozilla/plugins:$MOZILLA_FIVE_HOME/plugins:%{_libdir}/mozilla/plugins"
FONTCONFIG_PATH="/etc/fonts:$MOZILLA_FIVE_HOME/res/Xft"
export MOZILLA_FIVE_HOME LD_LIBRARY_PATH MOZ_PLUGIN_PATH FONTCONFIG_PATH

MOZARGS=""
MOZLOCALE="$(echo $LANG | sed 's|_\([^.]*\).*|-\1|g')"
if [ -f "$MOZILLA_FIVE_HOME/chrome/$MOZLOCALE.jar" ]; then
	MOZARGS="-UILocale $MOZLOCALE"
fi

$MOZ_PROGRAM -remote 'ping()' &>/dev/null
RUNNING=$?
if [ $? -eq 2 ]; then RUNNING=0; fi

CMD=0
while [ "$1" ]; do
	case "$1" in
#	  -mail|-email)
#		if [ $RUNNING -eq 0 -a $CMD -ne 1 ]; then
#			MOZARGS="-remote xfeDoCommand(openInbox) $MOZARGS"
#			CMD=1
#		fi;;
#	  -compose|-editor)
#		if [ $RUNNING -eq 0 -a $CMD -ne 1 ]; then
#			MOZARGS="-remote xfeDoCommand(composeMessage) $MOZARGS"
#			CMD=1
#		fi;;
	  -remote)
		if [ $CMD -ne 1 ]; then
			MOZARGS="-remote $2 $MOZARGS"
			CMD=1
		fi
		shift;;
	  -profile|-profile-manager)
		CMD=1
		;;
	  -*)
		MOZARGS="$MOZARGS $1"
		;;
	  *)
		if [ $CMD -ne 1 ]; then
			if [ -e "$PWD/$1" ]; then
				URL="file://$PWD/$1"
			elif [ -e "$1" ]; then
				URL="file://$1"
			else
				URL="$1"
			fi
			if [ $RUNNING -eq 0 ]; then
				MOZARGS="-remote openURL(\"$URL\",new-window) $MOZARGS"
			else
				MOZARGS="-remote openURL(\"$URL\") $MOZARGS"
			fi
			CMD=1
		else
			MOZARGS="$MOZARGS $1"
		fi;;
	esac
	shift
done

if [ $RUNNING -eq 0 -a $CMD -ne 1 ]; then
	exec $MOZ_PROGRAM -remote "xfeDoCommand(openBrowser)" $MOZARGS
else
	exec $MOZ_PROGRAM $MOZARGS &
fi;
EOF

%build
export MOZ_APP_NAME="firefox"
%{!?_without_autoconf213:autoconf-2.13}
%{?_without_autoconf213:autoconf}

export MOZ_PHOENIX="1"
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
%{__make} -f client.mk depend
%{__make} %{?_smp_mflags} -f client.mk build

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_libdir}

%{__make} -C xpinstall/packager/ \
	MOZ_PKG_APPNAME="firefox" \
	MOZILLA_BIN="\$(DIST)/bin/firefox-bin"

%{__install} -D -m0755 firefox.sh %{buildroot}%{_bindir}/firefox
%{__install} -D -m0644 browser/base/skin/Throbber.png %{buildroot}%{_datadir}/pixmaps/firefox.png

%{__tar} -xvz -C %{buildroot}%{_libdir} -f dist/firefox-*-linux-gnu.tar.gz

%{__install} -m0644 bookmarks.html %{buildroot}%{_libdir}/firefox/defaults/profile/
%{__install} -m0644 bookmarks.html %{buildroot}%{_libdir}/firefox/defaults/profile/US/

%{__perl} -pi.orig -e 's|mozilla-MOZILLA_VERSION|firefox|g; s|LIBDIR|%{_libdir}|g;' build/package/rpm/SOURCES/mozilla-rebuild-databases.pl.in
%{__install} -D -m0755 build/package/rpm/SOURCES/mozilla-rebuild-databases.pl.in %{buildroot}%{_libdir}/firefox/firefox-rebuild-database

### FIXME: Fixed "nsNativeComponentLoader: GetFactory(libwidget_gtk.so) Load FAILED with error: libwidget_gtk.so" by linking. (Please fix upstream)
if [ ! -f %{buildroot}%{_libdir}/firefox/components/libwidget_gtk.so ]; then
	%{__ln_s} -f libwidget_gtk2.so %{buildroot}%{_libdir}/firefox/components/libwidget_gtk.so
fi

%if %{?_without_freedesktop:1}0
        %{__install} -D -m0644 firefox.desktop %{buildroot}%{_datadir}/gnome/apps/Internet/firefox.desktop
%else
        %{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
	desktop-file-install --vendor net                  \
		--add-category X-Red-Hat-Base              \
		--dir %{buildroot}%{_datadir}/applications \
		firefox.desktop
%endif

%post
/sbin/ldconfig 2>/dev/null
%{_libdir}/firefox/firefox-rebuild-databases.pl &>/dev/null || :

%postun
/sbin/ldconfig 2>/dev/null
if [ $1 -gt 1 ]; then
	%{_libdir}/firefox/firefox-rebuild-databases.pl &>/dev/null || :
fi

%preun
if [ $1 -eq 0 ]; then
	%{__rm} -rf %{_libdir}/firefox/{chrome/overlayinfo/,components/}
	%{__rm} -f %{_libdir}/firefox/chrome/*.rdf
fi

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc LEGAL LICENSE
%{_bindir}/firefox
%{_libdir}/firefox/
%{_datadir}/pixmaps/firefox.png
%{?_without_freedesktop:%{_datadir}/gnome/apps/Internet/firefox.desktop}
%{!?_without_freedesktop:%{_datadir}/applications/net-firefox.desktop}

%changelog
* Tue Jun 15 2004 Dag Wieers <dag@wieers.com> - 0.9-1
- Updated to release 0.9.

* Sat Jun 12 2004 Dag Wieers <dag@wieers.com> - 0.8-3
- Added xremote patches. (Peter Peltonen)
- Open new window instead of new tab.
- Enabled all default extensions except irc and venkman. (Luke Ross, Edward Rudd, Anthony Ball, Ian Burrell)
- Firefox start-up script now handles file://-URLs.

* Wed Jun  2 2004 Matthias Saou <http://freshrpms.net/> 0.8-2
- Added Yellow Dog 3.0 build dependencies.
- Added libIDL-devel and gcc-c++ build requirements.
- Change dist/firefox-i*-linux-gnu to dist/firefox-*-linux-gnu because of ppc.

* Fri Apr 09 2004 Dag Wieers <dag@wieers.com> - 0.8-2
- Fixed off-by-1 border for plugins. (Daniele Paoni)
- Open new window by default, added --profile-manager. (Gary Peck)
- RH73 build using gcc 3.2.3. (Edward Rudd)
- Added x86_64 patch. (Oliver Sontag)
- Added xmlextras to extensionlist. (Richard Prescott)

* Wed Feb 11 2004 Dag Wieers <dag@wieers.com> - 0.8-1
- Used gtk2 explicitly as the toolkit again and fix libwidget_gtk2.
- Small fix in firefox start-up script. (Andre Costa)

* Tue Feb 10 2004 Dag Wieers <dag@wieers.com> - 0.8-0
- Changed name from mozilla-firebird to firefox.
- Updated to release 0.8.

* Thu Oct 16 2003 Dag Wieers <dag@wieers.com> - 0.7-0
- Added typeaheadfind to extensionlist. (Jeroen Cranendonk)
- Updated to release 0.7.

* Tue Aug 12 2003 Dag Wieers <dag@wieers.com> - 0.6.1-1
- Used gtk2 explicitly as the toolkit. (Duncan Mak)

* Sun Aug 03 2003 Dag Wieers <dag@wieers.com> - 0.6.1-0
- Updated to release 0.6.1.

* Wed Jun 25 2003 Dag Wieers <dag@wieers.com> - 0.6-0
- Initial package. (using DAR)
