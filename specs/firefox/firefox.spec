# $Id$

# Authority: dag

### FIXME: TODO: Improve firefox start-up script for file:// URLs.

### FIXME: Doesn't compile with distcc (PATH seems to be honored ??)
# Distcc: 0
# Soapbox: 0

%define dfi %(which desktop-file-install &>/dev/null; echo $?)

Summary: Mozilla Firefox web browser.
Name: firefox
Version: 0.8
Release: 1
License: MPL/LGPL
Group: Applications/Internet
URL: http://www.mozilla.org/projects/firefox/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/firefox-source-%{version}.tar.bz2
Patch1001: firefox-0.8-gtk2xtbin.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: XFree86-devel, zlib-devel, zip, perl
BuildRequires: gtk+-devel, libpng-devel, libmng-devel, libjpeg-devel, ORBit-devel
%{?rhfc1:BuildRequires: gtk2-devel}
%{?rhel3:BuildRequires: gtk2-devel}
%{?rh90:BuildRequires: gtk2-devel}
%{?rh80:BuildRequires: gtk2-devel}
%{?rh73:BuildRequires: gtk+-devel}
%{?rhel21:BuildRequires: gtk+-devel}
%{?rhel62:BuildRequires: gtk+-devel}

Obsoletes: phoenix, MozillaFirebird, mozilla-firebird, mozilla-firefox

%description
Mozilla Firefox is an open-source web browser, designed for standards
compliance, performance and portability.

%prep
%setup -n mozilla
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
ac_add_options --with-system-jpeg
ac_add_options --with-system-zlib
ac_add_options --with-system-png
ac_add_options --with-system-mng
ac_add_options --with-pthreads
ac_add_options --disable-tests
ac_add_options --disable-debug
ac_add_options --disable-debug-modules
ac_add_options --disable-xprint
ac_add_options --disable-mailnews
ac_add_options --disable-composer
ac_add_options --disable-ldap
ac_add_options --disable-jsd
ac_add_options --disable-dtd-debug
ac_add_options --disable-gtktest
ac_add_options --disable-freetype2
ac_add_options --disable-freetypetest
ac_add_options --disable-installer
ac_add_options --enable-plaintext-editor-only
ac_add_options --enable-optimize="%{optflags}"
ac_add_options --enable-crypto
ac_add_options --enable-strip
ac_add_options --enable-strip-libs
ac_add_options --enable-reorder
ac_add_options --enable-mathml
ac_add_options --enable-xinerama
ac_add_options --enable-extensions="pref,cookie,wallet,typeaheadfind"
%{?rhfc1:ac_add_options --enable-xft}
%{?rhfc1:ac_add_options --enable-default-toolkit="gtk2"}
%{?rhel3:ac_add_options --enable-xft}
%{?rhel3:ac_add_options --enable-default-toolkit="gtk2"}
%{?rh90:ac_add_options --enable-xft}
%{?rh90:ac_add_options --enable-default-toolkit="gtk2"}
%{?rh80:ac_add_options --enable-xft}
%{?rh80:ac_add_options --enable-default-toolkit="gtk2"}
%{?rh73:ac_add_options --disable-xft}
%{?rh73:ac_add_options --enable-default-toolkit="gtk"}
%{?rhel21:ac_add_options --disable-xft}
%{?rhel21:ac_add_options --enable-default-toolkit="gtk"}
%{?rh62:ac_add_options --disable-xft}
%{?rh62:ac_add_options --enable-default-toolkit="gtk"}
EOF

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=Firefox Web Browser
Comment=Lightweight Mozilla-based web browser
Exec=firefox
Icon=firefox.png
Terminal=false
Type=Application
StartupNotify=true
MimeType=text/html;text/x-java;inode/directory;application/xhtml+xml;
Categories=Application;Network;
EOF

%{__cat} <<'EOF' >%{name}.sh
#!/bin/sh

### Written by Dag Wieers <dag@wieers.com>
### Please send suggestions and fixes to me.

ulimit -c 0

MOZ_PROGRAM="%{_libdir}/firefox/firefox"

MOZILLA_FIVE_HOME="%{_libdir}/firefox"
LD_LIBRARY_PATH="%{_libdir}/firefox:%{_libdir}/firefox/plugins:$LD_LIBRARY_PATH"
MOZ_PLUGIN_PATH="%{_libdir}/firefox/plugins:%{_libdir}/mozilla/plugins"
FONTCONFIG_PATH="/etc/fonts:%{_libdir}/firefox/res/Xft"
export MOZILLA_FIVE_HOME LD_LIBRARY_PATH MOZ_PLUGIN_PATH FONTCONFIG_PATH

MOZARGS=""
MOZLOCALE="$(echo $LANG | sed 's|_\([^.]*\).*|-\1|g')"
if [ -f "%{_libdir}/firefox/chrome/$MOZLOCALE.jar" ]; then
	MOZARGS="-UILocale $MOZLOCALE"
fi

$MOZ_PROGRAM -remote 'ping()' &>/dev/null
RUNNING=$?
if [ $? -eq 0 -a $? -eq 2 ]; then RUNNING=0; fi

case "$1" in
  -mail|-email)
	if [ $RUNNING -eq 0 ]; then
		exec $MOZ_PROGRAM -remote "xfeDoCommand(openInbox)" $MOZARGS ${1+"$@"}
	fi;;
  -compose|-editor)
	if [ $RUNNING -eq 0 ]; then
		exec $MOZ_PROGRAM -remote "xfeDoCommand(composeMessage)" $MOZARGS ${1+"$@"}
	fi;;
  -remote)
	exec $MOZ_PROGRAM -remote "$2" $MOZARGS ${1+"$@"};;
  -profile|-profile-manager)
	exec $MOZ_PROGRAM $MOZARGS $@ &;;
  -*);;
  '');;
  *)
	if [ -z "$1" ]; then continue; fi
	if [ $RUNNING -eq 0 ]; then
		$MOZ_PROGRAM -remote "openURL($1,new-tab)" $MOZARGS ${1+"$@"} && exit 0
	else
		$MOZ_PROGRAM -remote "openURL($1)" $MOZARGS ${1+"$@"} && exit 0
	fi;;
esac

if [ $RUNNING -eq 0 ]; then
	exec $MOZ_PROGRAM -remote "xfeDoCommand (openBrowser)" $MOZARGS $@
else
	exec $MOZ_PROGRAM $MOZARGS $@ &
fi;
EOF

%build
export MOZ_PHOENIX="1"
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
%{__make} -f client.mk depend
%{__make} %{?_smp_mflags} -f client.mk build

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir} \
			%{buildroot}%{_libdir} \
			%{buildroot}%{_datadir}/pixmaps/

%{__make} -C xpinstall/packager/ \
	MOZ_PKG_APPNAME="firefox" \
	MOZILLA_BIN="\$(DIST)/bin/firefox-bin"

%{__install} -m0755 %{name}.sh %{buildroot}%{_bindir}/firefox

tar -xvz -C %{buildroot}%{_libdir} -f dist/firefox-i*-linux-gnu.tar.gz

%{__install} -m0644 browser/base/skin/Throbber.png %{buildroot}%{_datadir}/pixmaps/firefox.png
%{__install} -m0644 bookmarks.html %{buildroot}%{_libdir}/firefox/defaults/profile/
%{__install} -m0644 bookmarks.html %{buildroot}%{_libdir}/firefox/defaults/profile/US/

### FIXME: Fixed "nsNativeComponentLoader: GetFactory(libwidget_gtk.so) Load FAILED with error: libwidget_gtk.so" by linking. (Please fix upstream)
if [ ! -f %{buildroot}%{_libdir}/firefox/components/libwidget_gtk.so ]; then
	%{__ln_s} -f libwidget_gtk2.so %{buildroot}%{_libdir}/firefox/components/libwidget_gtk.so
fi

%if %{dfi}
        %{__install} -d -m0755 %{buildroot}%{_datadir}/gnome/apps/Internet/
        %{__install} -m0644 %{name}.desktop %{buildroot}%{_datadir}/gnome/apps/Internet/
%else
        %{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
	desktop-file-install --vendor net                  \
		--add-category X-Red-Hat-Base              \
		--dir %{buildroot}%{_datadir}/applications \
		%{name}.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_bindir}/*
%{_libdir}/firefox/
%{_datadir}/pixmaps/*
%if %{dfi}
	%{_datadir}/gnome/apps/Internet/*.desktop
%else
	%{_datadir}/applications/*.desktop
%endif

%changelog
* Thu Feb 19 2004 Dag Wieers <dag@wieers.com> - 0.8-2
- Fixed off-by-1 border for plugins. (Daniele Paoni)
- Open new window by default, added --profile-manager. (Gary Peck)
- RH73 build using gcc 3.2.3. (Edward Rudd)
- Added x86_64 patch. (Oliver Sontag)

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
