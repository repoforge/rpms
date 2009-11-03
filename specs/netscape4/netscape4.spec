# $Id$
# Authority: dag

Summary: The Netscape Communicator suite of tools.
Name: netscape4
Version: 4.8
Release: 3.2%{?dist}
Epoch: 4
License: Proprietary
Group: Applications/Internet
URL: http://www.netscape.com/

Source0: ftp://ftp.netscape.com/pub/communicator/english/4.8/unix/supported/linux22/complete_install/communicator-v48-us.x86-unknown-linux2.2.tar.gz
Source1: ftp://ftp.netscape.com/pub/communicator/english/4.8/unix/supported/linux22/navigator_standalone/navigator-v48-us.x86-unknown-linux2.2.tar.gz
Source2: netscape.sh
Source3: netscape-communicator.desktop
Source4: netscape-navigator.desktop
Source5: bookmark.htm
Source10: nethelp-ja.tar.bz2
Source11: Netscape.ja.4.79.bz2
Source12: nethelp-es.tar.bz2
Source13: Netscape.es.4.79.bz2
Source14: nethelp-fr.tar.bz2
Source15: Netscape.fr.4.79.bz2
Source16: nethelp-de.tar.bz2
Source17: Netscape.de.4.79.bz2
Source18: netscape-wheelmouse
Source19: netscape.png
Source20: Netscape.ru.4.79.bz2
Source21: Netscape.zh_TW.big5.4.79.bz2
Source22: Netscape.zh_CN.gb2312.4.79.bz2
Source23: nethelp-zh_TW.big5.tar.bz2
Source24: font.properties.zh_TW
Source25: Netscape.ko.4.79.bz2
Source26: nethelp-ko.tar.bz2
# Japanese fix
Source30: ns-bogus-locale.tgz
Source31: font.properties.ja

BuildRequires: bzip2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Prefix: /usr

ExclusiveArch: i386
%define __spec_install_post :

%description
Netscape Navigator is a Web browser which supports the latest HTML
standards, Java, JavaScript and some style sheets.

%package -n netscape-common
Requires: indexhtml >= 6.2-2
Obsoletes: nls
Prereq: chkfontpath
Summary: Files shared by Netscape Navigator and Communicator.
Group: Applications/Internet

%description -n netscape-common
This package contains the files that are shared between the Netscape
Navigator Web browser and the Netscape Communicator suite of tools
(the Navigator Web browser, an email client, a news reader, and a Web
page editor).

Install the netscape-common package if you're installing either the
netscape-navigator or the netscape-communicator program.

%package -n netscape-communicator
Requires: netscape-common = %{epoch}:%{version}-%{release}
Provides: webclient
Summary: The Netscape Communicator suite of tools.
Group: Applications/Internet

%description -n netscape-communicator
Netscape Communicator is a suite of tools including a Web browser, a
Usenet news reader, and an email client.

%package -n netscape-navigator
Requires: netscape-common = %{epoch}:%{version}-%{release}
Provides: webclient
Summary: The Netscape Navigator Web browser.
Group: Applications/Internet

%description -n netscape-navigator
Netscape Navigator is a Web browser which supports the latest HTML
standards, Java, JavaScript, and some style sheets.

%prep
%setup -c -b 1
mv communic*/* .
rmdir communicator*

%install
%{__rm} -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir} \
	%{buildroot}%{_libdir}/netscape/plugins \
	%{buildroot}%{_libdir}/netscape/java/classes

for I in *.nif; do
	tar -C %{buildroot}%{_libdir}/netscape -xzvf $I
done
mv %{buildroot}%{_libdir}/netscape/netscape %{buildroot}%{_libdir}/netscape/netscape-communicator
cp -a vreg %{buildroot}%{_libdir}/netscape
cp -a *.jar %{buildroot}%{_libdir}/netscape/java/classes
install -m 644 %{SOURCE24} %{buildroot}%{_libdir}/netscape/java/classes
install -m 644 %{SOURCE31} %{buildroot}%{_libdir}/netscape/java/classes
echo 'Communicator,4.8.0.20020722,%{_libdir}/netscape' > /tmp/infile
./vreg %{buildroot}%{_libdir}/netscape/registry /tmp/infile
rm -f /tmp/infile

# get the netscape-navigator binary now
tar xvzf %{SOURCE1} '*/netscape-v48.nif'
tar xvzf navigator*/netscape-v48.nif netscape

install -m 755 netscape %{buildroot}%{_libdir}/netscape/netscape-navigator

install -m755 $RPM_SOURCE_DIR/netscape.sh %{buildroot}%{_bindir}/netscape

# put this stuff into the doc directory
mv %{buildroot}%{_libdir}/netscape/{LICENSE,README,Netscape.ad} .

mkdir -p %{buildroot}/etc/X11/applnk/Internet
cp -av $RPM_SOURCE_DIR/netscape-communicator.desktop \
 %{buildroot}/etc/X11/applnk/Internet/netscape-communicator.desktop
cp -av $RPM_SOURCE_DIR/netscape-navigator.desktop \
 %{buildroot}/etc/X11/applnk/Internet/netscape-navigator.desktop

ln -s netscape %{buildroot}%{_bindir}/netscape-navigator
ln -s netscape %{buildroot}%{_bindir}/netscape-communicator

rm -f `find %{buildroot} -path "*dynMotif*"`

install -m 644 $RPM_SOURCE_DIR/bookmark.htm %{buildroot}%{_libdir}/netscape

(
 cd %{buildroot}%{_libdir}/netscape/movemail-src
 gcc $RPM_OPT_FLAGS -o ../movemail -DMAIL_USE_LOCKF -DNETSCAPE movemail.c
)

# Do localization stuff

dir=`pwd`

for locale in de es fr ja ko ru zh_CN.gb2312 zh_TW.big5; do
  mkdir -p %{buildroot}/usr/X11R6/lib/X11/$locale/app-defaults
  bunzip2 -c $RPM_SOURCE_DIR/Netscape.$locale.4.79.bz2 > \
     %{buildroot}/usr/X11R6/lib/X11/$locale/app-defaults/Netscape
#  cat $RPM_SOURCE_DIR/netscape-wheelmouse >> \
#     %{buildroot}/usr/X11R6/lib/X11/$locale/app-defaults/Netscape
  if [ -e $RPM_SOURCE_DIR/nethelp-$locale.tar.bz2 ]; then
     mkdir -p %{buildroot}%{_libdir}/netscape/$locale
     cd %{buildroot}%{_libdir}/netscape/$locale ; \
        bunzip2 -c $RPM_SOURCE_DIR/nethelp-$locale.tar.bz2 | tar -xvvf -
  fi
%ifarch sparc
  pushd %{buildroot}/usr/X11R6/lib/X11/$locale/app-defaults
  perl -pi -e "s|4.8|4.51|g" Netscape
  popd
%endif
done

#cd $dir
#mkdir -p %{buildroot}/usr/X11R6/lib/X11/app-defaults
#install -m 644 Netscape.ad \
#	%{buildroot}/usr/X11R6/lib/X11/app-defaults/Netscape
#cat $RPM_SOURCE_DIR/netscape-wheelmouse >> \
#     %{buildroot}/usr/X11R6/lib/X11/app-defaults/Netscape

(
  cd %{buildroot}%{_libdir}/netscape
  mv de de_DE
  mv es es_ES
  mv fr fr_FR
  mv ja ja_JP.eucJP
  mv ko ko_KR.eucKR
)

#
# build and install the library for motif bug.
#
tar xzf %{SOURCE30}
mv ns-bogus-locale/README README.ns_bogus_locale
(cd ns-bogus-locale;
make
cp ns_bogus_locale.so %{buildroot}%{_libdir}/netscape/
)

find %{buildroot}%{_libdir}/netscape -type d -exec chmod 755 {} \;
find %{buildroot}%{_libdir}/netscape -type f -exec chmod go+rX {} \;

# install icon for KDE use. This is the same icon as is in gnome-core;
# it *shouldn't* conflict.

mkdir -p %{buildroot}%{_datadir}/pixmaps
install -m 644 $RPM_SOURCE_DIR/netscape.png \
	%{buildroot}%{_datadir}/pixmaps/

mkdir -p %{buildroot}%{_libdir}/mozilla/plugins
ln -s ../../netscape/plugins/libflashplayer.so \
   %{buildroot}%{_libdir}/mozilla/plugins/libflashplayer.so

%clean
%{__rm} -rf %{buildroot}

%files -n netscape-common
%defattr(-, root, root, 0755)
%{_bindir}/netscape
%dir %{_libdir}/netscape
%lang(de_DE) %{_libdir}/netscape/de_DE
%lang(fr_FR) %{_libdir}/netscape/fr_FR
%lang(es_ES) %{_libdir}/netscape/es_ES
%lang(ja_JP.eucJP) %{_libdir}/netscape/ja_JP.eucJP
%lang(ko_KR.eucKR) %{_libdir}/netscape/ko_KR.eucKR
%lang(zh_TW.big5) %{_libdir}/netscape/zh_TW.big5
%doc LICENSE Netscape.ad README
%{_libdir}/netscape/bookmark.htm
%{_libdir}/netscape/java
%{_libdir}/netscape/libjsd.so
%{_libdir}/netscape/nethelp
%{_libdir}/netscape/ns_bogus_locale.so
%{_libdir}/netscape/registry
%{_libdir}/netscape/vreg
%{_libdir}/netscape/plugins
%{_libdir}/netscape/XKeysymDB
%{_libdir}/mozilla/plugins/libflashplayer.so
/usr/X11R6/lib/X11/*/app-defaults/*
#/usr/X11R6/lib/X11/app-defaults/Netscape
%{_datadir}/pixmaps/netscape.png


%files -n netscape-navigator
%defattr(-, root, root, 0755)
%config(missingok) /etc/X11/applnk/Internet/netscape-navigator.desktop
%{_bindir}/netscape-navigator
%{_libdir}/netscape/netscape-navigator

%files -n netscape-communicator
%defattr(-, root, root, 0755)
%config(missingok) /etc/X11/applnk/Internet/netscape-communicator.desktop
%{_bindir}/netscape-communicator
%{_libdir}/netscape/netscape-communicator
%{_libdir}/netscape/movemail
%{_libdir}/netscape/movemail-src
%{_libdir}/netscape/spell

%post -n netscape-common
if [ -x %{_sbindir}/chkfontpath ]; then
  %{_sbindir}/chkfontpath -q -a /usr/X11R6/lib/X11/fonts/75dpi
fi

%pre -n netscape-common
for locale in de_DE es_ES fr_FR ja_JP.eucJP ko_KR.eucJP zh_CN.gb312 zh_TW.big5; do
  if [ ! -L %{_libdir}/netscape/$locale ] ; then
      rm -rf %{_libdir}/netscape/$locale
  fi
done
exit 0

%triggerpostun -n netscape-common -- netscape-common < 4.74-6
for locale in de es fr ja; do
  rmdir %{_libdir}/netscape/$locale >/dev/null 2>&1
done
exit 0


%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 4.8-3.2
- Rebuild for Fedora Core 5.

* Thu Apr 15 2004 Dag Wieers <dag@wieers.com> - 4.8-4
- Fixed epoch problem for RH9, RHEL3 and RHFC1. (Erik Williamson)

* Tue Feb 25 2003 Dag Wieers <dag@wieers.com> - 4.8-3
- Renamed package to netscape4.

* Sun Aug 25 2002 Dag Wieers <dag@wieers.com> - 4.8-2
- Updated to 4.8.

* Sun Jan 27 2002 Bill Nottingham <notting@redhat.com>
- 4.79
- tweak netscape script to not break with some fileutils (#56430)
- add LD_ASSUME_KERNEL in netscape script (#57576)

* Thu Aug  9 2001 Yukihiro Nakai <ynakai@redhat.com>
- Update Korean resources (Netscape, nethelp).

* Sun Jul 22 2001 Bill Nottingham <notting@redhat.com>
- 4.78

* Mon Apr  9 2001 Bill Nottingham <notting@redhat.com>
- 4.77

* Tue Mar 13 2001 Bill Nottingham <notting@redhat.com>
- look explicitly for a window-id to send remote commands to; this fixes
  -remote on KDE (#30574)
- show language-dependent index.html if it exists (#26721)
- add a symlink for the flash plugin in %{_libdir}/mozilla/plugins (#26102)

* Thu Feb  8 2001 Bill Nottingham <notting@redhat.com>
- fix typo in shell script

* Tue Feb  6 2001 Bill Nottingham <notting@redhat.com>
- fix detection of already running copies in the shell script (#26435)

* Mon Feb  5 2001 Bill Nottingham <notting@redhat.com>
- switch back to -irix-session-manangement so that Japanese with
  kinput2 works. WTF???? (#24911)

* Mon Jan 29 2001 Bill Nottingham <notting@redhat.com>
- fix detection of already running copies in the shell script (#25160)

* Wed Jan 23 2001 Bill Nottingham <notting@redhat.com>
- fix copious error messages when starting in Japanese (#24911)

* Fri Jan 19 2001 Bill Nottingham <notting@redhat.com>
- hack users' preferences files to avoid address book crashes. I feel dirty.
- %lang-ify
- switch off IRIX session management (#21234)
- add a 'sleep 1' to the startup script (#16741)
- fix composer (and other) invocations (#15716)
- merge in alpha script changes

* Mon Dec 18 2000 Bill Nottingham <notting@redhat.com>
- fix netscape.sh to not do really stupid stuff in the presence of mozilla
- remove chkfontpath from buildprereqs

* Sun Dec 17 2000 Yukihiro Nakai <ynakai@redhat.com>
- Add Korean resources
- Update netscape.sh to support Korean locale

* Sat Dec 16 2000 Yukihiro Nakai <ynakai@redhat.com>
- Add Japanese resources
- Update netscape.sh to support Japanese.
- Change URL unsupport -> support.
- Add BuildRequires
- Update Netscape.ja.4.76.bz2
- Add Japanese translation to *.desktop
- Add Chinese resource from CLE.

* Thu Nov  9 2000 Bill Nottingham <notting@redhat.com>
- update to 4.76
- add app-defaults file for koi8-r fonts (leon@geon.donetsk.ua)
- add icon (#17872)

* Thu Aug 24 2000 Bill Nottingham <notting@redhat.com>
- fix movemail so it might work right

* Thu Aug 17 2000 Bill Nottingham <notting@redhat.com>
- 4.75

* Wed Aug 16 2000 Bill Nottingham <notting@redhat.com>
- fix trigger
- fix summaries

* Sun Aug  6 2000 Bill Nottingham <notting@redhat.com>
- sv desktop entry translations
- just ship full locales

* Mon Jul 31 2000 Bill Nottingham <notting@redhat.com>
- fix ownership of nethelp dirs
- don't worry about fixing the 4.73 upgrade problem; it's unfixable

* Wed Jul 26 2000 Bill Nottingham <notting@redhat.com>
- fix problem with upgrading from broken 4.73 packages
- turn off wheelmouse for now

* Tue Jul 25 2000 Bill Nottingham <notting@redhat.com>
- updated german translation from Harald Hoyer (harald@redhat.com)

* Fri Jul 21 2000 Bill Nottingham <notting@redhat.com>
- 4.74

* Fri Jul 14 2000 Bill Nottingham <notting@redhat.com>
- fix nethelp dir inclusion

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Mon Jul  3 2000 Bill Nottingham <notting@redhat.com>
- hacks for wheelmouse support

* Sun Jun 18 2000 Matt Wilson <msw@redhat.com>
- use new path for indexhtml

* Fri Jun 16 2000 Bill Nottingham <notting@redhat.com>
- don't strip ia32 binaries on ia64

* Tue Jun 13 2000 Bill Nottingham <notting@redhat.com>
- hack ia64 build

* Sun Jun 11 2000 Bill Nottingham <notting@redhat.com>
- rebuild

* Wed May 10 2000 Bill Nottingham <notting@redhat.com>
- 4.73

* Fri Mar  3 2000 Bill Nottingham <notting@redhat.com>
- updated Japanese locale defaults
- move movemail, movemail-src, spell to communicator package

* Wed Mar  1 2000 Bernhard Rosenkränzer <bero@redhat.com>
- Add German nethelp
- fix up broken HTML in nethelp, all locales

* Tue Feb 29 2000 Bernhard Rosenkränzer <bero@redhat.com>
- Add locale files for German
- while at it, fix up the ISO-8859-15-entry for French and Spanish

* Fri Feb 25 2000 Bill Nottingham <notting@redhat.com>
- don't run sparc against glibc-2.0; the X bug has been fixed
- don't do locale-munging; 4.72 doesn't write broken locale settings

* Thu Feb 24 2000 Bill Nottingham <notting@redhat.com>
- tweak wrapper script to be smarter about lock files

* Wed Feb 23 2000 Bill Nottingham <notting@redhat.com>
- update to 4.72 on intel

* Wed Feb 16 2000 Bill Nottingham <notting@redhat.com>
- munge default bookmarks slightly

* Tue Feb  8 2000 Bill Nottingham <notting@redhat.com>
- fix netscape.sh syntax errors
- fix homepage detection

* Fri Feb  4 2000 Nalin Dahyabhai <nalin@redhat.com>
- fix netscape.sh syntax errors

* Fri Feb  4 2000 Bill Nottingham <notting@redhat.com>
- integrate some l10n stuff

* Fri Nov  5 1999 Bill Nottingham <notting@redhat.com>
- remove sparc binaries - in different package now.

* Wed Sep 29 1999 Bill Nottingham <notting@redhat.com>
- update to 4.7

* Fri Sep 24 1999 Bill Nottingham <notting@redhat.com>
- fix timezone

* Wed Sep 22 1999 Bill Nottingham <notting@redhat.com>
- fix quoting in shell script
- fix processname of compat-lib-ized netscape

* Mon Sep 20 1999 Matt Wilson <msw@redhat.com>
- make netscape-common requirements include the serial

* Fri Sep 17 1999 Bill Nottingham <notting@redhat.com>
- get default homepage back

* Sat Sep 11 1999 Bill Nottingham <notting@redhat.com>
- fix paths to pidof

* Fri Aug 27 1999 Bill Nottingham <notting@redhat.com>
- fix paths to compat libs in new script.

* Fri Aug 27 1999 Preston Brown <pbrown@redhat.com>
- some ideas from H. Peter Anvin and Dave Cinege's wrapper incorporated.

* Fri Aug 20 1999 Bill Nottingham <notting@redhat.com>
- run against the compatibility libs. This sucks.
- re-integrate the Sparc version, with different versions.

* Tue Jun 15 1999 Bill Nottingham <notting@redhat.com>
- update to 4.61

* Mon May 17 1999 Bill Nottingham <notting@redhat.com>
- update to 4.6

* Thu May  6 1999 Bill Nottingham <notting@redhat.com>
- remove libTrueDoc to get rid of libc5 dependency. Oops.

* Mon May  3 1999 Bill Nottingham <notting@redhat.com>
- update to attempt to fix pipe bug

* Thu Apr 15 1999 Bill Nottingham <notting@redhat.com>
- rewrite startup script to be sane

* Mon Apr 12 1999 Bill Nottingham <notting@redhat.com>
- move requires/obsoletes to the right place in the spec file.

* Thu Mar 25 1999 Bill Nottingham <notting@redhat.com>
- update to 4.51
- build on sparc. Wheee.

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 8)

* Tue Mar 16 1999 Bill Nottingham <notting@redhat.com>
- applink -> applnk
- make subpackages require versions

* Thu Feb 25 1999 Bill Nottingham <notting@redhat.com>
- wmconfig -> applink

* Fri Jan 22 1999 Bill Nottingham <notting@redhat.com>
- fix netscape script for other locales
- remove LD_PRELOAD (ns is now linked against libBrokenLocale....)

* Sun Jan 10 1999 Bill Nottingham <notting@redhat.com>
- spec file cosmetics

* Sun Dec 13 1998 Bill Nottingham <notting@redhat.com>
- update to 4.08

* Tue Oct  6 1998 Bill Nottingham <notting@redhat.com>
- update to 4.07

* Tue Aug 18 1998 Bill Nottingham <notting@redhat.com>
- updated to 4.06

* Fri Jul 10 1998 Cristian Gafton <gafton@redhat.com>
- modified to load libBrokenLocale.so.1, so that glibc-devel is no longer
  required

* Thu Jun 11 1998 Prospector System <bugs@redhat.com>
- translations modified for de

* Thu Jun 11 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Jun 10 1998 Erik Troan <ewt@redhat.com>
- replaced LANG=C with a preload of libBrokenLocale.so
- don't point to our html page if a home page is set in the user's preferences
- added missing " to wmconfig files

* Mon May 04 1998 Erik Troan <ewt@redhat.com>
- added LANG=C to netscape start wrapper

* Thu Apr 02 1998 Erik Troan <ewt@redhat.com>
- update to netscape 4.05
- moved common files to netscape-common package which both navigator and
  communicator require
- made relocateable (needs RPM >= 2.4.103 to relocate properly)

* Fri Jan 23 1998 Erik Troan <ewt@redhat.com>
- initial package is rel 3, works on RH 4.x and RH 5.x
