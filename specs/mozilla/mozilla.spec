# $Id$
# Authority: dag

%{?dist: %{expand %%define %dist 1}}

### FIXME: TODO: Build RH73 builds with gcc 3.2.3
### FIXME: TODO: Improve firefox start-up script for file:// URLs.
### FIXME: TODO: Check extra patches (x86_64)
### FIXME: TODO: Fixed off-by-1 border for plugins.

%define real_version 1.6
%define _unpackaged_files_terminate_build 0

Summary: Web browser and mail reader
Name: mozilla
Version: 1.6
Release: 1
Epoch: 38
License: MPL/NPL/GPL/LGPL
Group: Applications/Internet
URL: http://www.mozilla.org/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source0: ftp://ftp.mozilla.org/pub/mozilla.org/mozilla/releases/mozilla%{real_version}/src/mozilla-source-%{real_version}.tar.bz2
Source1: mozilla.sh.in
Source2: mozilla-icon.png
Source4: mozilla.desktop
Source7: mozilla-make-package.pl
Source9: mozicon16.xpm
Source10: mozicon50.xpm
Source11: mozilla-rebuild-databases.pl.in
Source12: mozilla-mail.desktop
Source13: mozilla-mail-icon.png
Source14: mozilla-compose.desktop
Source15: mozilla-compose-icon.png
Source17: mozilla-psm-exclude-list
Source18: mozilla-xpcom-exclude-list
Source19: mozilla-redhat-default-bookmarks.html
Patch0: mozilla-navigator-overlay-menu.patch
Patch1: mozilla-editor-overlay-menu.patch
Patch6: mozilla-prefs-debug.patch
Patch7: mozilla-redhat-home-page.patch
Patch12: mozilla-psfonts-7.2.patch
Patch13: mozilla-nspr-packages.patch
Patch14: mozilla-default-plugin-less-annoying.patch
Patch17: mozilla-buildid-title.patch
Patch22: mozilla-1.4-x86_64.patch
Patch23: mozilla-1.6-gnome-uriloader.patch
Patch28: mozilla-1.4.1-ppc64.patch
Patch29: mozilla-1.4-prdtoa.patch

Patch1001: mozilla-1.6-gtk2xtbin.patch

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


### Removed compat-gcc-c++, compat-libstdc++-devel, compat-gcc
BuildRequires: libpng-devel, libjpeg-devel, zlib-devel, zip, perl, autoconf
BuildRequires: indexhtml, perl
%{?fc1:BuildRequires: glib2-devel, gtk2-devel, libIDL-devel >= 0.8.0}
%{?el3:BuildRequires: glib2-devel, gtk2-devel, libIDL-devel >= 0.8.0}
%{?rh9:BuildRequires: glib2-devel, gtk2-devel, libIDL-devel >= 0.8.0}
%{?rh8:BuildRequires: glib2-devel, gtk2-devel, libIDL-devel >= 0.8.0}
Requires: fileutils, perl, /usr/bin/killall, indexhtml
Requires: mozilla-nspr = %{epoch}:%{version}-%{release}
Requires: mozilla-nss = %{epoch}:%{version}-%{release}
Obsoletes: mozilla-psm, mozilla-spellchecker
Provides: webclient

ExclusiveArch: i386 x86_64 ia64 ppc s390 s390x

%description
Mozilla is an open-source web browser, designed for standards
compliance, performance and portability.

%package nspr
Summary: Netscape Portable Runtime
Group: Applications/Internet
Conflicts: mozilla < 35:0.9.9

%description nspr
NSPR provides platform independence for non-GUI operating system
facilities. These facilities include threads, thread synchronization,
normal file and network I/O, interval timing and calendar time, basic
memory management (malloc and free) and shared library linking.

%package nspr-devel
Summary: Development Libraries for the Netscape Portable Runtime
Group: Development/Libraries
Requires: mozilla-nspr = %{epoch}:%{version}-%{release}

%description nspr-devel
Header files for doing development with the Netscape Portable Runtime.

%package nss
Summary: Network Security Services
Group: Applications/Internet
Requires: mozilla-nspr = %{epoch}:%{version}-%{release}

%description nss
Network Security Services (NSS) is a set of libraries designed to
support cross-platform development of security-enabled server
applications. Applications built with NSS can support SSL v2 and v3,
TLS, PKCS #5, PKCS #7, PKCS #11, PKCS #12, S/MIME, X.509 v3
certificates, and other security standards.

%package nss-devel
Summary: Development Libraries for Network Security Services
Group: Applications/Internet
Requires: mozilla-nspr-devel = %{epoch}:%{version}-%{release}
Requires: mozilla-nss = %{epoch}:%{version}-%{release}

%description nss-devel
Header files to doing development with Network Security Services.

%package devel
Summary: Development files for Mozilla
Group: Development/Libraries
Requires: mozilla = %{epoch}:%{version}-%{release}
Requires: mozilla-nspr-devel = %{epoch}:%{version}-%{release}
Requires: mozilla-nss-devel = %{epoch}:%{version}-%{release}

%description devel
Development header files for mozilla.

%package mail
Summary: Mozilla-based mail system
Group: Applications/Internet
Prereq: fileutils, mozilla = %{epoch}:%{version}-%{release}

%description mail
Mail/news client based on the Mozilla web browser.  The mail/news
client supports IMAP, POP, and NNTP and has an easy to use interface.

%package chat
Summary: IRC client integrated with Mozilla
Group: Applications/Internet
Prereq: fileutils, mozilla = %{epoch}:%{version}-%{release}

%description chat
IRC client that is integrated with the Mozilla web browser.

%package js-debugger
Summary: JavaScript debugger for use with Mozilla
Group: Applications/Internet
Prereq: fileutils, mozilla = %{epoch}:%{version}-%{release}

%description js-debugger
JavaScript debugger for use with Mozilla.

%package dom-inspector
Summary: tool for inspecting the DOM of pages in Mozilla
Group: Applications/Internet
Prereq: fileutils, mozilla = %{epoch}:%{version}-%{release}

%description dom-inspector
This is a tool that allows you to inspect the DOM for web pages in
Mozilla.  This is of great use to people who are doing Mozilla chrome
development or web page development.

%prep
%setup -n %{name}
%patch1001 -b .gtk2xtbin

#%patch0 -p1
#%patch0 -p1 -R

#%patch1 -p1
#%patch1 -p1 -R

#%patch6 -p1
#%patch6 -p1 -R

%patch7 -p1
#%patch7 -p1 -R

### Can't hurt to leave this in since the defaults are empty.
%patch12 -p1

%patch13 -p1

### make the plugin dialog less annoying and disable redirection to the
### plugin downloader page.
%patch14 -p1

### remove the annoying buildid from the titlebar
#%patch17 -p1
#%patch17 -p1 -R

%patch22 -p1 -b .x86_64

# make sure that the gnome uri handler isn't run during registration
%patch23 -p1 -b .gnome

### add nss build support for ppc64
%patch28 -p1

### work around problems with prdtoa.c
%patch29 -p1

### set up our default bookmarks
%{__install} -m0644 %{SOURCE19} profile/defaults/bookmarks.html

%build
export BUILD_OFFICIAL="1"
export MOZILLA_OFFICIAL="1"
export NATIVE_THEME_SUPPORT="1"
./configure \
	--program-prefix="%{?_program_prefix}" \
	--prefix="%{_prefix}" \
	--libdir="%{_libdir}" \
	--mandir="%{_mandir}" \
	--with-default-mozilla-five-home="%{_libdir}/%{name}-%{real_version}" \
	--enable-optimize="%{optflags}" \
	--enable-strip-libs \
	--enable-xinerama \
	--enable-calendar \
	--disable-debug \
	--disable-tests \
	--disable-short-wchar \
	--disable-xprint \
	--enable-nspr-autoconf \
	--enable-extensions="default,irc" \
	--without-mng \
	--enable-crypto \
	--without-system-nspr \
	--with-system-zlib \
%{?fc1:--enable-default-toolkit="gtk2"} \
%{?fc1:--enable-xft} \
%{?fc1:--disable-freetype2} \
%{?el3:--enable-default-toolkit="gtk2"} \
%{?el3:--enable-xft} \
%{?el3:--disable-freetype2} \
%{?rh9:--enable-default-toolkit="gtk2"} \
%{?rh9:--enable-xft} \
%{?rh9:--disable-freetype2} \
%{?rh8:--enable-default-toolkit="gtk2"} \
%{?rh8:--enable-xft} \
%{?rh8:--disable-freetype2} \
%{?rh7:--disable-xft} \
%{?el2:--disable-xft} \
%{?rh6:--disable-xft}
#%{?rh7:--without-libIDL} \

#unset CFLAGS
%{__make} %{?_smp_mflags} export
%{__make} %{?_smp_mflags} libs

%install
%{__rm} -rf %{buildroot}
export BUILD_OFFICIAL="1" 
export MOZILLA_OFFICIAL="1"
export NATIVE_THEME_SUPPORT="1"
%makeinstall \
	includedir="%{buildroot}%{_includedir}/%{name}-%{real_version}"

%{__install} -d -m0755 %{buildroot}%{_sysconfdir} \
			%{buildroot}%{_datadir}/pixmaps/ \
			%{buildroot}%{_datadir}/applications/ \
			%{buildroot}%{_libdir}/mozilla/plugins/ \
			%{buildroot}%{_libdir}/%{name}/ \
			%{buildroot}%{_libdir}/%{name}-%{real_version}/chrome/lang/ \
			%{buildroot}%{_libdir}/%{name}-%{real_version}/icons/ \
			%{buildroot}%{_libdir}/%{name}-%{real_version}/plugins/ \
			%{buildroot}%{_includedir}/%{name}-%{real_version}/nss/

### NSPR (4) and NSS (3) are both installed into /usr/lib instead of /usr/lib/mozilla-VERSION
for file in libnspr4.so libplc4.so libplds4.so libnss3.so libsmime3.so libsoftokn3.so libsoftokn3.chk libssl3.so; do
        %{__mv} -vf %{buildroot}%{_libdir}/%{name}-%{real_version}/$file %{buildroot}%{_libdir}/
done

### libnssckbi.so must be in both places
%{__cp} -vf %{buildroot}%{_libdir}/%{name}-%{real_version}/libnssckbi.so %{buildroot}%{_libdir}/

### Create empty listfiles
for file in "" -chat -devel -dom-inspector -js-debugger -mail -nspr -nspr-devel -nss -nss-devel; do
	echo '%defattr(-, root, root, 0755)' >mozilla$file.list
done

function buildlibdir {
	%{SOURCE7} \
		--install-dir %{buildroot}%{_libdir} \
		--install-root %{_libdir} \
		--package $1 \
		--package-file xpinstall/packager/packages-unix \
		--output-file %{_builddir}/%{buildsubdir}/$2 $3 $4 $5 $6
}

function buildmozdir {
	%{SOURCE7} \
		--install-dir %{buildroot}%{_libdir}/%{name}-%{real_version} \
		--install-root %{_libdir}/%{name}-%{real_version} \
		--package $1 \
		--package-file xpinstall/packager/packages-unix \
		--output-file %{_builddir}/%{buildsubdir}/$2 $3 $4 $5 $6
}

### Build filelists
buildlibdir nspr mozilla-nspr.list
buildlibdir nss mozilla-nss.list

### manually add the libnssckbi.so file (already in packages-unix)
#echo '%{_libdir}/%{name}-%{real_version}/libnssckbi.so' >> mozilla-nss.list
buildmozdir langenus mozilla.list
buildmozdir regus mozilla.list
buildmozdir deflenus mozilla.list
buildmozdir xpcom mozilla.list \
	--exclude-file="%{SOURCE18}"
buildmozdir browser mozilla.list
buildmozdir spellcheck mozilla.list
buildmozdir psm mozilla.list \
	--exclude-file="%{SOURCE17}"

buildmozdir mail mozilla-mail.list
buildmozdir chatzilla mozilla-chat.list
buildmozdir venkman mozilla-js-debugger.list
buildmozdir inspector mozilla-dom-inspector.list

### save a copy of the default installed-chrome.txt file before we
### muck with it
%{__cp} -vf %{buildroot}%{_libdir}/%{name}-%{real_version}/chrome/installed-chrome.txt %{buildroot}%{_libdir}/%{name}-%{real_version}/chrome/lang/

### Build our initial component and chrome registry
### register our components
export LD_LIBRARY_PATH="%{buildroot}%{_libdir}/%{name}-%{real_version}:%{buildroot}%{_libdir}"
export MOZILLA_FIVE_HOME="%{buildroot}%{_libdir}/%{name}-%{real_version}"
%{buildroot}%{_libdir}/%{name}-%{real_version}/regxpcom

### set up the default skin and locale to trigger the generation of
### the user-locales and users-skins.rdf
echo "skin,install,select,classic/1.0" >> %{buildroot}%{_libdir}/%{name}-%{real_version}/chrome/installed-chrome.txt
echo "locale,install,select,en-US" >> %{buildroot}%{_libdir}/%{name}-%{real_version}/chrome/installed-chrome.txt

### save the defaults in a file that will be used later to rebuild the
### installed-chrome.txt file
echo "skin,install,select,classic/1.0" >> %{buildroot}%{_libdir}/%{name}-%{real_version}/chrome/lang/default.txt
echo "locale,install,select,en-US" >> %{buildroot}%{_libdir}/%{name}-%{real_version}/chrome/lang/default.txt

### set up the chrome rdf files
%{buildroot}%{_libdir}/%{name}-%{real_version}/regchrome

### fix permissions of the chrome directories
find %{buildroot}%{_libdir}/%{name}-%{real_version} -type d -perm 0700 -exec chmod 755 {} \; || :

### cp -L (dereference all symlinks) is required for fileutils >= 2.0.27
### (POSIX compliance); prior versions don't understand -L, so fall back...

### copy the nss files to the right place
find security/nss/lib/ -name '*.h' -type f \
	-exec %{__cp} {} %{buildroot}%{_includedir}/%{name}-%{real_version}/nss/ \;

find %{buildroot}%{_includedir}/%{name}-%{real_version}/ -type f | \
		sed -e "s|%{buildroot}||" | \
		grep -v "%{_includedir}/%{name}-%{real_version}/nss" | \
		grep -v "%{_includedir}/%{name}-%{real_version}/nspr" \
	>mozilla-devel.list

find %{buildroot}%{_includedir}/%{name}-%{real_version}/ -type f | \
		sed -e "s|%{buildroot}||" | \
		grep "%{_includedir}/%{name}-%{real_version}/nspr" \
	>mozilla-nspr-devel.list

find %{buildroot}%{_includedir}/%{name}-%{real_version}/ -type f | \
		sed -e "s|%{buildroot}||" | \
		grep "%{_includedir}/%{name}-%{real_version}/nss" \
	>mozilla-nss-devel.list

### copy our idl into place
#mkdir -p %{buildroot}/%{prefix}/share/idl/mozilla-%{real_version}
#(cd dist/idl ; tar chf - * | \
#  (cd %{buildroot}/%{prefix}/share/idl/mozilla-%{real_version} ; \
#   tar xvf -))

### copy our devel tools
%{__install} -m0755 dist/bin/xpcshell dist/bin/xpidl dist/bin/xpt_dump dist/bin/xpt_link \
  %{buildroot}%{_libdir}/%{name}-%{real_version}/

### set up our desktop files
%{__install} -m0644 %{SOURCE2} %{SOURCE13} %{SOURCE15} %{buildroot}%{_datadir}/pixmaps/
%{__install} -m0644 %{SOURCE4} %{SOURCE12} %{SOURCE14} %{buildroot}%{_datadir}/applications/

### our icons are better!
%{__install} -m0644 %{SOURCE9} %{SOURCE10} %{buildroot}%{_libdir}/%{name}-%{real_version}/icons/

### install our mozilla.sh file
%{__cat} %{SOURCE1} | sed -e 's|MOZILLA_VERSION|%{real_version}|g' \
			-e 's|LIBDIR|%{_libdir}|g' \
	> %{buildroot}%{_bindir}/mozilla
chmod 755 %{buildroot}%{_bindir}/mozilla

### install our rebuild file
%{__cat} %{SOURCE11} | sed -e 's|MOZILLA_VERSION|%{real_version}|g' \
			-e 's|LIBDIR|%{_libdir}|g' \
	> %{buildroot}%{_libdir}/%{name}-%{real_version}/mozilla-rebuild-databases.pl
chmod 755 %{buildroot}%{_libdir}/%{name}-%{real_version}/mozilla-rebuild-databases.pl

### install the gre.conf file
echo -e "[%{real_version}]\nGRE_PATH=%{_libdir}/%{name}-%{real_version}" >%{buildroot}%{_sysconfdir}/gre.conf

### Fix plugins
#{__mv} -f %{buildroot}%{_libdir}/%{name}-%{real_version}/plugins/ %{_libdir}/%{name}/
#{__ln_s} -f %{_libdir}/%{name}/plugins/ %{buildroot}%{_libdir}/%{name}-%{real_version}/plugins/

%clean
%{__rm} -rf %{buildroot}

%post
/sbin/ldconfig &>/dev/null
if [ -f %{_libdir}/%{name}-%{real_version}/mozilla-rebuild-databases.pl ]; then
    %{_libdir}/%{name}-%{real_version}/mozilla-rebuild-databases.pl
fi

%postun
/sbin/ldconfig &>/dev/null
if [ $1 -eq 2 ]; then
  if [ -f %{_libdir}/%{name}-%{real_version}/mozilla-rebuild-databases.pl ]; then
      %{_libdir}/%{name}-%{real_version}/mozilla-rebuild-databases.pl
  fi
fi

%triggerpostun -- mozilla < 1.0
# Older packages will leave mozilla unusable after the postun script
# script is run for the old package.  Rebuild the databases after that
# has been run.
if [ -f %{_libdir}/%{name}-%{real_version}/mozilla-rebuild-databases.pl ]; then
    %{_libdir}/%{name}-%{real_version}/mozilla-rebuild-databases.pl
fi

%preun
if [ $1 -eq 0 ]; then
  %{__rm} -rf %{_libdir}/%{name}-%{real_version}/chrome/overlayinfo
  %{__rm} -f %{_libdir}/%{name}-%{real_version}/chrome/*.rdf
fi

%post nspr
/sbin/ldconfig &>/dev/null

%post nss
/sbin/ldconfig &>/dev/null

%postun nspr
/sbin/ldconfig &>/dev/null

%postun nss
/sbin/ldconfig &>/dev/null

%post mail
/sbin/ldconfig &>/dev/null
if [ -f %{_libdir}/%{name}-%{real_version}/mozilla-rebuild-databases.pl ]; then
    %{_libdir}/%{name}-%{real_version}/mozilla-rebuild-databases.pl
fi

%postun mail
/sbin/ldconfig &>/dev/null
if [ -f %{_libdir}/%{name}-%{real_version}/mozilla-rebuild-databases.pl ]; then
    %{_libdir}/%{name}-%{real_version}/mozilla-rebuild-databases.pl
fi

%post chat
/sbin/ldconfig &>/dev/null
if [ -f %{_libdir}/%{name}-%{real_version}/mozilla-rebuild-databases.pl ]; then
    %{_libdir}/%{name}-%{real_version}/mozilla-rebuild-databases.pl
fi

%postun chat
/sbin/ldconfig &>/dev/null
if [ -f %{_libdir}/%{name}-%{real_version}/mozilla-rebuild-databases.pl ]; then
    %{_libdir}/%{name}-%{real_version}/mozilla-rebuild-databases.pl
fi

%post js-debugger
/sbin/ldconfig &>/dev/null
if [ -f %{_libdir}/%{name}-%{real_version}/mozilla-rebuild-databases.pl ]; then
    %{_libdir}/%{name}-%{real_version}/mozilla-rebuild-databases.pl
fi

%postun js-debugger
/sbin/ldconfig &>/dev/null
if [ -f %{_libdir}/%{name}-%{real_version}/mozilla-rebuild-databases.pl ]; then
    %{_libdir}/%{name}-%{real_version}/mozilla-rebuild-databases.pl
fi

%post dom-inspector
/sbin/ldconfig &>/dev/null
if [ -f %{_libdir}/%{name}-%{real_version}/mozilla-rebuild-databases.pl ]; then
    %{_libdir}/%{name}-%{real_version}/mozilla-rebuild-databases.pl
fi

%postun dom-inspector
/sbin/ldconfig &>/dev/null
if [ -f %{_libdir}/%{name}-%{real_version}/mozilla-rebuild-databases.pl ]; then
    %{_libdir}/%{name}-%{real_version}/mozilla-rebuild-databases.pl
fi

%files -f mozilla.list
%defattr(-, root, root, 0755)
%doc %{_mandir}/man?/*
%config %{_sysconfdir}/gre.conf
%{_bindir}/mozilla
%{_libdir}/%{name}-%{real_version}/mozilla-rebuild-databases.pl
%{_datadir}/pixmaps/mozilla-icon.png
%{_datadir}/pixmaps/mozilla-mail-icon.png
%{_datadir}/pixmaps/mozilla-compose-icon.png

%{_libdir}/%{name}-%{real_version}/libgtkembedmoz.so

%verify (not md5 mtime size) %{_libdir}/%{name}-%{real_version}/components/compreg.dat
%verify (not md5 mtime size) %{_libdir}/%{name}-%{real_version}/components/xpti.dat

%dir %{_libdir}/%{name}/
%dir %{_libdir}/%{name}/plugins/

%dir %{_libdir}/%{name}-%{real_version}/defaults/pref/
%dir %{_libdir}/%{name}-%{real_version}/defaults/profile/US/
%dir %{_libdir}/%{name}-%{real_version}/defaults/profile/
%dir %{_libdir}/%{name}-%{real_version}/defaults/wallet/
%dir %{_libdir}/%{name}-%{real_version}/defaults/autoconfig/
%dir %{_libdir}/%{name}-%{real_version}/defaults/messenger/US/
%dir %{_libdir}/%{name}-%{real_version}/defaults/messenger/
%dir %{_libdir}/%{name}-%{real_version}/defaults/

%dir %{_libdir}/%{name}-%{real_version}/chrome/icons/default/
%dir %{_libdir}/%{name}-%{real_version}/chrome/icons/
%dir %{_libdir}/%{name}-%{real_version}/chrome/lang/
%dir %{_libdir}/%{name}-%{real_version}/chrome/overlayinfo/
%dir %{_libdir}/%{name}-%{real_version}/chrome/

%dir %{_libdir}/%{name}-%{real_version}/res/builtin/
%dir %{_libdir}/%{name}-%{real_version}/res/rdf/
%dir %{_libdir}/%{name}-%{real_version}/res/dtd/
%dir %{_libdir}/%{name}-%{real_version}/res/fonts/
%dir %{_libdir}/%{name}-%{real_version}/res/

%dir %{_libdir}/%{name}-%{real_version}/components/
%dir %{_libdir}/%{name}-%{real_version}/components/myspell/
%dir %{_libdir}/%{name}-%{real_version}/icons/
%dir %{_libdir}/%{name}-%{real_version}/searchplugins/

%dir %{_libdir}/%{name}-%{real_version}/plugins/
%dir %{_libdir}/%{name}-%{real_version}/res/html/
%dir %{_libdir}/%{name}-%{real_version}/res/samples/
%dir %{_libdir}/%{name}-%{real_version}/res/entityTables/
%dir %{_libdir}/%{name}-%{real_version}/ipc/modules/
%dir %{_libdir}/%{name}-%{real_version}/ipc/

%{_libdir}/%{name}-%{real_version}/chrome/lang/installed-chrome.txt
%{_libdir}/%{name}-%{real_version}/chrome/lang/default.txt

%dir %{_libdir}/%{name}-%{real_version}/
%{_datadir}/applications/mozilla.desktop

%files nspr -f mozilla-nspr.list
%defattr(-, root, root, 0755)
%{_datadir}/aclocal/nspr.m4

%files nspr-devel -f mozilla-nspr-devel.list
%defattr(-, root, root, 0755)
%{_libdir}/pkgconfig/mozilla-nspr.pc
%{_bindir}/mozilla-config
#%{_datadir}/aclocal/*.m4

%files nss -f mozilla-nss.list
%defattr(-, root, root, 0755)

%files nss-devel -f mozilla-nss-devel.list
%defattr(-, root, root, 0755)
%{_libdir}/pkgconfig/mozilla-nss.pc

%files mail -f mozilla-mail.list
%defattr(-, root, root, 0755)
%dir %{_libdir}/%{name}-%{real_version}/chrome/icons/default
%dir %{_libdir}/%{name}-%{real_version}/chrome/icons
%dir %{_libdir}/%{name}-%{real_version}/chrome
%dir %{_libdir}/%{name}-%{real_version}/components
%dir %{_libdir}/%{name}-%{real_version}
%{_datadir}/applications/mozilla-compose.desktop
%{_datadir}/applications/mozilla-mail.desktop

%files chat -f mozilla-chat.list
%defattr(-, root, root, 0755)

%files js-debugger -f mozilla-js-debugger.list
%defattr(-, root, root, 0755)

%files dom-inspector -f mozilla-dom-inspector.list
%defattr(-, root, root, 0755)

%files devel -f mozilla-devel.list
%defattr(-, root, root, 0755)
%{_datadir}/idl/%{name}-%{real_version}/*
%{_libdir}/pkgconfig/mozilla-js.pc
%{_libdir}/pkgconfig/mozilla-plugin.pc
%{_libdir}/pkgconfig/mozilla-xpcom.pc
%{_libdir}/pkgconfig/mozilla-gtkmozembed.pc
%{_libdir}/%{name}-%{real_version}/xpcshell
%{_libdir}/%{name}-%{real_version}/xpidl
%{_libdir}/%{name}-%{real_version}/xpt_dump
%{_libdir}/%{name}-%{real_version}/xpt_link

%changelog
* Sat Apr 03 2004 Dag Wieers <dag@wieers.com> - 1.6-1
- Fixed off-by-1 border for plugins. (Daniele Paoni)
- Open new window by default, added --profile-manager. (Gary Peck)
- Added x86_64 patch. (Oliver Sontag)

* Sat Jan 24 2004 Dag Wieers <dag@wieers.com> - 1.6-0
- Added psm and spellchecker sub-packages to mozilla package.
- Updated to release 1.6.

* Tue Dec 02 2003 Dag Wieers <dag@wieers.com> - 1.5-2
- Fix the history-not-updating problem. (Tim Verhoeven)

* Thu Oct 30 2003 Dag Wieers <dag@wieers.com> - 1.5-1
- Move libnss3.so and others back to %%{_libdir}. (Matthew Lenz)
- Removed the loop dependency of mozilla-nss-devel. (Zach Gelnett)

* Tue Oct 28 2003 Dag Wieers <dag@wieers.com> - 1.5-0
- Updated to release 1.5.

* Tue Jul 01 2003 Dag Wieers <dag@wieers.com> - 1.4-2
- Updated to release 1.4.

* Sun May 11 2003 Dag Wieers <dag@wieers.com> - 1.4-0.beta
- Initial package. (using DAR)
