# $Id: gnubiff.spec,v 1.1 2004/03/01 15:41:10 driesve Exp $

# Authority: dries

# NeedsCleanup

%define	_name		gnubiff
%define	_version	1.0.8
%define _release	1.dries

Summary: a mail notification program
Summary(nl): een programma dat een indicatie geeft als email aankomt

BuildRoot:	%{_tmppath}/build-%{_name}-%{_version}
Name:		%{_name}
Version:	%{_version}
Release:	%{_release}
License:	GPL
Group:		Applications/Internet
URL: http://gnubiff.sourceforge.net/
Source: http://gnubiff.sourceforge.net/downloads/gnubiff-1.0.8.tar.gz

#(d) primscreenshot: http://gnubiff.sourceforge.net/pics/screenshot-gtk.png

%description
Gnubiff is a mail notification program that checks for mail, displays
headers when new mail has arrived and allows to read the first lines of new
mails. It supports pop3, apop, imap4, mh, qmail and mailfile.

%description -l nl
Gnubiff is een programma dat een indicatie geeft als email aankomt. Het kan
nagaan of er nieuwe emails zijn, het kan de headers tonen en het kan de
eerste lijnen van een email tonen. Het ondersteunt pop3, apop, imap4, mh,
qmail en mailfile.

%prep
%{__rm} -rf "${RPM_BUILD_ROOT}"
%setup

%build
%configure --with-gnome --with-password
make

%install
echo RPM_BUILD_ROOT is $RPM_BUILD_ROOT
export DESTDIR=$RPM_BUILD_ROOT
make install-strip

%files
%defattr(-,root,root)
%doc README ABOUT-NLS AUTHORS ChangeLog COPYING NEWS INSTALL THANKS
/usr/bin/gnubiff
/usr/lib/bonobo/servers/GNOME_gnubiffApplet.server
/usr/share/gnome-2.0/ui/GNOME_gnubiffApplet.xml
/usr/share/gnubiff
/usr/share/info/gnubiff.info.gz
/usr/share/locale/*/LC_MESSAGES/gnubiff.mo
/usr/share/man/man1/gnubiff.1.gz
/usr/share/pixmaps/gnubiff_icon.png
/usr/share/sounds/gnubiff/coin.wav
/usr/share/sounds/gnubiff/mail.wav

%changelog
* Thu Dec 25 2003 Dries Verachtert <dries@ulyssis.org> 1.0.8-1.dries
- first packaging for Fedora Core 1

