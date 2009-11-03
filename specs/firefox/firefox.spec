# $Id$
# Authority: dag

# ExcludeDist: fc3 el4


%{?rh7:%define _without_freedesktop 1}
%{?rh7:%define _without_gtk2 1}
%{?el2:%define _without_freedesktop 1}
%{?el2:%define _without_gtk2 1}

Summary: Mozilla Firefox web browser
Name: firefox
Version: 0.10.1
Release: 0.1.2%{?dist}
License: MPL/LGPL
Group: Applications/Internet
URL: http://www.mozilla.org/projects/firefox/

#Source: http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/firefox-%{version}-source.tar.bz2
Source: http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/firefox-1.0PR-source.tar.bz2
Source1: firefox-rebuild-databases.pl.in
Source2: firefox.png
Source3: bookmarks.html
Source4: firefox.xpm
Patch2: firefox-0.9.3-uri.patch
Patch3: mozilla-default-plugin-less-annoying.patch
Patch4: firefox-0.7.3-freetype-compile.patch
Patch5: mozilla-1.7-psfonts.patch
Patch6: firefox-0.10-gcc3-alpha.patch
Patch7: firefox-PR1-js-64bit-math.patch
Patch90: firefox-PR1-gtk-file-chooser-trunk.patch
Patch91: firefox-PR1-gtk-file-chooser-updates.patch
Patch101: firefox-PR1-pkgconfig.patch
Patch102: firefox-PR1-clipboard-access.patch
Patch103: firefox-PR1-alt-num-tab-switch.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: XFree86-devel, zlib-devel, zip
BuildRequires: libpng-devel, libjpeg-devel
BuildRequires: ORBit-devel, gcc-c++, krb5-devel
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}
%{!?_without_gtk2:BuildRequires: gtk2-devel, libIDL-devel, gnome-vfs2-devel}
%{?_without_gtk2:BuildRequires: gtk+-devel}

Obsoletes: phoenix, MozillaFirebird, mozilla-firebird, mozilla-firefox
Provides: webclient

%description
Mozilla Firefox is an open-source web browser, designed for standards
compliance, performance and portability.

%prep
%setup -q -n mozilla
%patch2 -p0 -b .uri
%patch3 -p1 -b .plugin
#patch4 -p0 -b .freetype
%patch5 -p1 -b .psfonts
%patch6 -p1 -b .gcc3-alpha
%patch7 -p0 -b .64bit-math
%patch90 -p0 -b .gtk-file-chooser-trunk
%patch91 -p1 -b .gtk-file-chooser-updates
%patch101 -p0 -b .pkgconfig
%patch102 -p0 -b .clipboard-access
%patch103 -p0 -b .alt-num-tab-switch

%{__cat} <<'EOF' >.mozconfig
. $topsrcdir/browser/config/mozconfig
export BUILD_OFFICIAL=1
export MOZILLA_OFFICIAL=1
mk_add_options BUILD_OFFICIAL=1
mk_add_options MOZILLA_OFFICIAL=1
ac_add_options --x-libraries="%{_prefix}/X11R6/%{_lib}"
ac_add_options --disable-debug
ac_add_options --disable-installer
ac_add_options --disable-jsd
ac_add_options --disable-strip
ac_add_options --disable-tests
ac_add_options --disable-xprint
ac_add_options --enable-extensions="default,-content-packs,-editor,-help,-irc,-spellcheck,-typeaheadfind"
ac_add_options --enable-official-branding
# We want to replace -O? with -Os to optimize compilation for size
ac_add_options --enable-optimize="-Os %(echo "%{optflags}" | sed 's/-O.//')"
ac_add_options --with-pthreads
ac_add_options --with-system-jpeg
ac_add_options --with-system-png
ac_add_options --with-system-zlib
%{?_without_gtk2:ac_add_options --enable-default-toolkit="gtk"}
%{?_without_gtk2:ac_add_options --disable-freetype2}
%{!?_without_gtk2:ac_add_options --enable-default-toolkit="gtk2"}
%{!?_without_gtk2:ac_add_options --enable-xft}
%{!?_without_gtk2:ac_add_options --enable-xinerama}
EOF

%{__cat} <<EOF >firefox.desktop
[Desktop Entry]
Name=Firefox Web Browser
GenericName=Web Browser
Comment=Browse the Web
Exec=firefox
Icon=firefox.png
Terminal=false
Type=Application
MimeType=text/html;text/xml;text/x-java;inode/directory;application/xhtml+xml;
Categories=Application;Network;
EOF

%{__cat} <<'EOF' >firefox.sh
#!/bin/sh

### Written by Dag Wieers <dag@wieers.com>
### Please send suggestions and fixes to me.

MOZ_APP_NAME="firefox"
MOZILLA_FIVE_HOME="%{_libdir}/firefox"
MOZ_PROGRAM="$MOZILLA_FIVE_HOME/firefox"

LD_LIBRARY_PATH="$MOZILLA_FIVE_HOME:$MOZILLA_FIVE_HOME/plugins${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"
MOZ_PLUGIN_PATH="$MOZILLA_FIVE_HOME/plugins:%{_libdir}/mozilla/plugins${MOZ_PLUGIN_PATH:+:$MOZ_PLUGIN_PATH}"
FONTCONFIG_PATH="/etc/fonts:$MOZILLA_FIVE_HOME/res/Xft"
export FONTCONFIG_PATH LD_LIBRARY_PATH MOZ_PLUGIN_PATH MOZILLA_FIVE_HOME

MOZARGS=""
MOZLOCALE="$(echo $LANG | sed 's|_\([^.]*\).*|-\1|g')"
[ -f "$MOZILLA_FIVE_HOME/chrome/$MOZLOCALE.jar" ] && MOZARGS="-UILocale $MOZLOCALE"

$MOZ_PROGRAM -a firefox -remote 'ping()' &>/dev/null
RUNNING=$?
[ $? -eq 2 ] && RUNNING=0

REMOTE=0
METHOD="new-window"

while [ "$1" ]; do
	case "$1" in
#	  -mail|-email)
#		if [ $RUNNING -eq 0 -a $REMOTE -ne 1 ]; then
#			MOZARGS="-remote xfeDoCommand(openInbox) $MOZARGS"
#			REMOTE=1
#		fi;;
#	  -compose|-editor)
#		if [ $RUNNING -eq 0 -a $REMOTE -ne 1 ]; then
#			MOZARGS="-remote xfeDoCommand(composeMessage) $MOZARGS"
#			REMOTE=1
#		fi;;
#	  -safemode)
#		FONTCONFIG_PATH=""
#		MOZLOCALE="en_US"
#		LD_LIBRARY_PATH="$MOZILLA_FIVE_HOME${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"
#		MOZ_PLUGIN_PATH=""
#		RUNNING=1
#		MOZARGS="-P safemode"
#		MOZ_PROGRAM="ltrace -o firefox-ltrace -S -f $MOZ_PROGRAM-bin"
#		HOME="/tmp/dag"
#		rm -rf $HOME; mkdir -p $HOME
#		export FONTCONFIG_PATH LD_LIBRARY_PATH MOZ_PLUGIN_PATH HOME
#		;;
	  -remote)
		if [ $REMOTE -ne 1 ]; then
			MOZARGS="-remote $2 $MOZARGS"
			REMOTE=1
		fi
		shift;;
	  -profile|-profile-manager)
		MOZARGS="$MOZARGS -profilemanager"
		REMOTE=1
		;;
	  -t|-tab)
		METHOD="new-tab"
		;;
	  -*)
		MOZARGS="$MOZARGS $1"
		;;
	  *)
		if [ -e "$PWD/$1" ]; then
			URL="file://$PWD/$1"
		elif [ -e "$1" ]; then
			URL="file://$1"
		else
			URL="$1"
		fi;;
	esac
	shift
done

if [ -z "$URL" ]; then URL="about:blank"; fi

if [ $RUNNING -eq 0 -a $REMOTE -ne 1 ]; then
        exec $MOZ_PROGRAM -a $MOZ_APP_NAME $MOZARGS -remote "openURL($URL,$METHOD)"
fi

exec $MOZ_PROGRAM -a $MOZ_APP_NAME $MOZARGS $URL
EOF

%build
export MOZILLA_OFFICIAL=1
export BUILD_OFFICIAL=1
#%{__make} -f client.mk depend
%{__make} %{?_smp_mflags} -f client.mk build

%install
%{__rm} -rf %{buildroot}
%{__make} -C xpinstall/packager/ \
	MOZILLA_BIN="\$(DIST)/bin/firefox-bin"

%{__install} -Dp -m0755 firefox.sh %{buildroot}%{_bindir}/firefox
%{__install} -Dp -m0644 %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/firefox.png

%{__install} -d -m0755 %{buildroot}%{_libdir}
%{__tar} -xvz -C %{buildroot}%{_libdir} -f dist/firefox-*-linux-gnu.tar.gz

%{__install} -Dp -m0644 %{SOURCE3} %{buildroot}%{_libdir}/firefox/defaults/profile/bookmarks.html
%{__install} -Dp -m0644 %{SOURCE3} %{buildroot}%{_libdir}/firefox/defaults/profile/US/bookmarks.html
%{__install} -Dp -m0644 %{SOURCE4} %{buildroot}%{_libdir}/firefox/chrome/icons/default/default.xpm
%{__install} -Dp -m0644 %{SOURCE4} %{buildroot}%{_libdir}/firefox/icons/default.xpm

%{__install} -Dp -m0755 %{SOURCE1} %{buildroot}%{_libdir}/firefox/firefox-rebuild-database
%{__perl} -pi -e 's|\$MOZ_DIST_BIN|%{_libdir}/firefox|g;' %{buildroot}%{_libdir}/firefox/firefox-rebuild-database

%{__install} -d -m0755 %{buildroot}%{_libdir}/mozilla/plugins/

%if %{?_without_gtk2:1}0
### FIXME: Fixed "nsNativeComponentLoader: GetFactory(libwidget_gtk.so) Load FAILED with error: libwidget_gtk.so" by linking. (Please fix upstream)
if [ ! -f %{buildroot}%{_libdir}/firefox/components/libwidget_gtk.so ]; then
	%{__ln_s} -f libwidget_gtk2.so %{buildroot}%{_libdir}/firefox/components/libwidget_gtk.so
fi
%endif

%if %{?_without_freedesktop:1}0
	%{__install} -Dp -m0644 firefox.desktop %{buildroot}%{_datadir}/gnome/apps/Internet/firefox.desktop
%else
	%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
	desktop-file-install --vendor net \
		--add-category X-Red-Hat-Base \
		--dir %{buildroot}%{_datadir}/applications \
		firefox.desktop
%endif

### Clean up buildroot
find %{buildroot}%{_libdir}/firefox/chrome/* -type d -maxdepth 1 -exec %{__rm} -rf {} \;

%post
/sbin/ldconfig 2>/dev/null
%{_bindir}/firefox -register &>/dev/null || :
%{_libdir}/firefox/firefox-rebuild-databases &>/dev/null || :
%{_bindir}/update-desktop-database %{_datadir}/applications &>/dev/null || :

%preun
if [ $1 -eq 0 ]; then
	%{__rm} -rf %{_libdir}/firefox/{chrome/overlayinfo,components,extensions}/
	%{__rm} -f %{_libdir}/firefox/{chrome/*.rdf,components.ini}
fi

%postun
/sbin/ldconfig 2>/dev/null
%{_bindir}/update-desktop-database %{_datadir}/applications &>/dev/null || :

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc LEGAL LICENSE README.txt
%{_bindir}/firefox
%{_libdir}/firefox/
%dir %{_libdir}/mozilla/
%dir %{_libdir}/mozilla/plugins/
%{_datadir}/pixmaps/firefox.png
%{?_without_freedesktop:%{_datadir}/gnome/apps/Internet/firefox.desktop}
%{!?_without_freedesktop:%{_datadir}/applications/net-firefox.desktop}

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.10.1-0.1.2
- Rebuild for Fedora Core 5.

* Mon Oct 04 2004 Dag Wieers <dag@wieers.com> - 0.10.1-0.1
- Disable typeaheadfind as it breaks things. (Matthias Hensler)
- Added more patches from rawhide.
- A few improvements to the firefox startup script. (Nicolai Langfeldt)

* Tue Sep 28 2004 Dag Wieers <dag@wieers.com> - 0.10-0.1
- Include default mozconfig.
- Add mozilla and mozilla plugins directory to package.
- Clean up the leftover .jar content.

* Thu Sep 16 2004 Matthias Saou <http://freshrpms.net/> 0.10-0
- Update to 1.0 PR.

* Sun Aug 08 2004 Dag Wieers <dag@wieers.com> - 0.9.3-1
- Added upstream psfonts patch from mozilla 1.7.
- Added upstream file:// URI extensions patch.
- Re-added xpm icon, small improvements and cleanup.

* Fri Aug  6 2004 Matthias Saou <http://freshrpms.net/> 0.9.3-0
- Update to 0.9.3.
- Took the bookmarks.html file out of the spec and added entries to it.

* Tue Aug 03 2004 Dag Wieers <dag@wieers.com> - 0.9.2-5
- Added patch to fix crashes on x86_64. (Nicholas Miell)

* Fri Jul 30 2004 Matthias Saou <http://freshrpms.net/> 0.9.2-5
- Revert included xpm icon to an add-on png that looks nicer.

* Tue Jul 27 2004 Matthias Saou <http://freshrpms.net/> 0.9.2-4
- Fixed register by calling firefox instead of firefox-bin.
- Added krb5/gssapi support.
- Included the upstream -register patch.
- Included the mozilla "less annoying" plugin patch.
- Removed unneeded configure options (unexisting or defaults).
- Removed unneeded exports and defines.
- Other minor cleanups.

* Sat Jul 24 2004 Dag Wieers <dag@wieers.com> - 0.9.2-3
- Sanitized firefox startup script.
- Don't kill Xvfb and allow -register to dump error info.
- Disabled StartupNotify and register mimetypes for Gnome 2.8.
- Don't rebuild firefox databases in %postun.
- Disabled xinerama for < RH7 and enabled svg support.
- Use supplied icons.

* Sat Jul 24 2004 Dag Wieers <dag@wieers.com> - 0.9.2-2
- Fixed firefox -register and firefox-rebuild-databases. (Gary Peck)
- Remove extensions-directory after uninstalling. (Gary Peck)
- Added gnomevfs extension. (Gary Peck)
- Clean up Xvfb afterwards.

* Thu Jul 22 2004 Dag Wieers <dag@wieers.com> - 0.9.2-1
- Updated to release 0.9.2.

* Thu Jul 01 2004 Dag Wieers <dag@wieers.com> - 0.9.1-1
- Updated to release 0.9.1.

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
