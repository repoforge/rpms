# $Id$

# Authority: dries
# Screenshot: http://gnubiff.sourceforge.net/pics/screenshot-gtk.png
# ScreenshotURL: http://gnubiff.sourceforge.net/screenshots.php

Summary: Mail notification program
Name: gnubiff
Version: 1.2.0
Release: 1
License: GPL
Group: Applications/Internet
URL: http://gnubiff.sourceforge.net/

Source: http://dl.sf.net/gnubiff/gnubiff-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gettext, libgnomeui-devel, gnome-panel, gcc-c++, openssl-devel, libglade-devel, gdk-pixbuf-devel, glib2-devel, libglade2-devel
%{?fc2:BuildRequires: gnome-panel-devel}

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

%description
Gnubiff is a mail notification program that checks for mail, displays
headers when new mail has arrived and allows to read the first lines of new
mails. It supports pop3, apop, imap4, mh, qmail and mailfile.

%prep
%setup

%build
%configure \
	--with-gnome \
	--with-password
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
make install-strip \
	DESTDIR="%{buildroot}"

%files
%defattr(-,root,root,0755)
%doc README ABOUT-NLS AUTHORS ChangeLog COPYING NEWS INSTALL THANKS
%{_bindir}/gnubiff
%{_libdir}/bonobo/servers/GNOME_gnubiffApplet.server
%{_datadir}/gnome-2.0/ui/GNOME_gnubiffApplet.xml
%{_datadir}/gnubiff
%{_datadir}/info/gnubiff.info.gz
%{_datadir}/locale/*/LC_MESSAGES/gnubiff.mo
%{_datadir}/man/man1/gnubiff.*
%{_datadir}/pixmaps
%{_datadir}/sounds/gnubiff

%changelog
* Thu May 20 2004 Dries Verachtert <dries@ulyssis.org> 1.2.0-1
- update to 1.2.0

* Thu Dec 25 2003 Dries Verachtert <dries@ulyssis.org> 1.0.8-1
- first packaging for Fedora Core 1
