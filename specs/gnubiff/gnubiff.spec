# $Id$
# Authority: dries
# Screenshot: http://gnubiff.sourceforge.net/pics/screenshot-gtk.png
# ScreenshotURL: http://gnubiff.sourceforge.net/screenshots.php

Summary: Mail notification program
Name: gnubiff
Version: 2.0.2
Release: 1
License: GPL
Group: Applications/Internet
URL: http://gnubiff.sourceforge.net/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://dl.sf.net/gnubiff/gnubiff-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gettext, libgnomeui-devel, gnome-panel, gcc-c++
BuildRequires: openssl-devel, libglade-devel, gdk-pixbuf-devel 
BuildRequires: glib2-devel, libglade2-devel
%{?fc2:BuildRequires: gnome-panel-devel}

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
# sed -i "s/\#include \"Mailbox.h\"/\#include \"Mailbox.h\"\n\#include \"sys\/stat.h\"/g;" src/File.h
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc README ABOUT-NLS AUTHORS ChangeLog COPYING NEWS INSTALL THANKS
%{_bindir}/gnubiff
%{?fc2:%{_libdir}/bonobo/servers/GNOME_gnubiffApplet.server}
%{?fc2:%{_datadir}/gnome-2.0/ui/GNOME_gnubiffApplet.xml}
%{_datadir}/gnubiff
%{_datadir}/info/gnubiff.info.gz
%{_mandir}/man1/gnubiff.*
%{_datadir}/pixmaps

%changelog
* Fri Oct 22 2004 Dries Verachtert <dries@ulyssis.org> 2.0.2-1
- Update to version 2.0.2.

* Sun Sep 12 2004 Dries Verachtert <dries@ulyssis.org> 2.0.1-1
- Update to version 2.0.1.

* Fri Sep 03 2004 Dries Verachtert <dries@ulyssis.org> 2.0.0-1
- Update to version 2.0.0.

* Fri Jun 25 2004 Dries Verachtert <dries@ulyssis.org> 1.4.0-1
- Update to version 1.4.0.

* Thu May 20 2004 Dries Verachtert <dries@ulyssis.org> 1.2.0-1
- Update to version 1.2.0.

* Thu Dec 25 2003 Dries Verachtert <dries@ulyssis.org> 1.0.8-1
- first packaging for Fedora Core 1
