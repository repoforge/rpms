# $Id$
# Authority: dries
# Screenshot: http://gnubiff.sourceforge.net/pics/screenshot-gtk.png
# ScreenshotURL: http://gnubiff.sourceforge.net/screenshots.php

# ExcludeDist: fc1 el3

%{?dtag: %{expand: %%define %dtag 1}}

Summary: Mail notification program
Name: gnubiff
Version: 2.2.11
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://gnubiff.sourceforge.net/

Source: http://dl.sf.net/gnubiff/gnubiff-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gettext, libgnomeui-devel, gnome-panel, gcc-c++
BuildRequires: openssl-devel, gdk-pixbuf-devel
BuildRequires: glib2-devel, libglade2-devel, gamin-devel
BuildRequires: perl(XML::Parser), intltool
BuildRequires: texinfo
%{!?dtag:BuildRequires: gnome-panel-devel}
%{?el5:BuildRequires: gnome-panel-devel}
%{?fc6:BuildRequires: gnome-panel-devel}
%{?fc5:BuildRequires: gnome-panel-devel}
%{?fc4:BuildRequires: gnome-panel-devel}
%{?el4:BuildRequires: gnome-panel-devel}
%{?fc3:BuildRequires: gnome-panel-devel}
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
%{__rm} -f %{buildroot}%{_infodir}/dir

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc ABOUT-NLS AUTHORS ChangeLog COPYING INSTALL NEWS README THANKS
%doc %{_datadir}/info/gnubiff.info.gz
%doc %{_mandir}/man1/gnubiff.1*
%{_bindir}/gnubiff
%{?fc2:%{_libdir}/bonobo/servers/GNOME_gnubiffApplet.server}
%{?fc2:%{_datadir}/gnome-2.0/ui/GNOME_gnubiffApplet.xml}
%{?fc3:%{_libdir}/bonobo/servers/GNOME_gnubiffApplet.server}
%{?fc3:%{_datadir}/gnome-2.0/ui/GNOME_gnubiffApplet.xml}
%{?el4:%{_libdir}/bonobo/servers/GNOME_gnubiffApplet.server}
%{?el4:%{_datadir}/gnome-2.0/ui/GNOME_gnubiffApplet.xml}
%{?fc4:%{_libdir}/bonobo/servers/GNOME_gnubiffApplet.server}
%{?fc4:%{_datadir}/gnome-2.0/ui/GNOME_gnubiffApplet.xml}
%{?fc5:%{_libdir}/bonobo/servers/GNOME_gnubiffApplet.server}
%{?fc5:%{_datadir}/gnome-2.0/ui/GNOME_gnubiffApplet.xml}
%{?fc6:%{_libdir}/bonobo/servers/GNOME_gnubiffApplet.server}
%{?fc6:%{_datadir}/gnome-2.0/ui/GNOME_gnubiffApplet.xml}
%{?el5:%{_libdir}/bonobo/servers/GNOME_gnubiffApplet.server}
%{?el5:%{_datadir}/gnome-2.0/ui/GNOME_gnubiffApplet.xml}
%{_datadir}/gnubiff/
%{_datadir}/pixmaps/

%changelog
* Tue Apr  7 2009 Dries Verachtert <dries@ulyssis.org> - 2.2.11-1
- Updated to release 2.2.11.

* Sun Apr 20 2008 Dries Verachtert <dries@ulyssis.org> - 2.2.10-1
- Updated to release 2.2.10.

* Mon Jul 16 2007 Dries Verachtert <dries@ulyssis.org> - 2.2.7-1
- Updated to release 2.2.7.

* Mon Apr 16 2007 Dries Verachtert <dries@ulyssis.org> - 2.2.6-1
- Updated to release 2.2.6.

* Mon Jan 29 2007 Dries Verachtert <dries@ulyssis.org> - 2.2.5-1
- Updated to release 2.2.5.

* Fri Dec 15 2006 Dries Verachtert <dries@ulyssis.org> - 2.2.4-1
- Updated to release 2.2.4.

* Sun Nov 12 2006 Dries Verachtert <dries@ulyssis.org> - 2.2.3-1
- Updated to release 2.2.3.

* Mon Aug 07 2006 Dries Verachtert <dries@ulyssis.org> - 2.2.2-1
- Updated to release 2.2.2.

* Tue May 24 2006 Dries Verachtert <dries@ulyssis.org> - 2.2.1-1
- Updated to release 2.2.1.

* Mon Apr 10 2006 Dries Verachtert <dries@ulyssis.org> - 2.2.0-1
- Updated to release 2.2.0.

* Mon Jan 09 2006 Dries Verachtert <dries@ulyssis.org> - 2.1.9-1
- Updated to release 2.1.9.

* Tue Dec 20 2005 Dries Verachtert <dries@ulyssis.org> - 2.1.8-1
- Update to release 2.1.8.

* Wed Nov 02 2005 Dries Verachtert <dries@ulyssis.org> - 2.1.7-1
- Update to release 2.1.7.

* Tue Oct 11 2005 Dries Verachtert <dries@ulyssis.org> - 2.1.6-1
- Update to release 2.1.6.

* Mon Aug 22 2005 Dries Verachtert <dries@ulyssis.org> - 2.1.5-1
- Update to release 2.1.5.

* Tue Jun 28 2005 Dries Verachtert <dries@ulyssis.org> - 2.1.4-1
- Update to release 2.1.4.

* Thu Mar 31 2005 Dries Verachtert <dries@ulyssis.org> - 2.1.2-1
- Update to release 2.1.2.

* Thu Dec 23 2004 Dries Verachtert <dries@ulyssis.org> - 2.1.0-1
- Update to release 2.1.0.

* Sat Dec 04 2004 Dries Verachtert <dries@ulyssis.org> - 2.0.3-1
- Update to release 2.0.3.

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
