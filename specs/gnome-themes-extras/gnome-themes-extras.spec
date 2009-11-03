# $Id$
# Authority: hadams

Summary: Collection of metathemes for the Gnome desktop environment
Name: gnome-themes-extras
Version: 0.9.0
Release: 6%{?dist}
License: LGPL
Group: User Interface/Desktops
URL: http://librsvg.sourceforge.net/theme.php

Source: ftp://ftp.gnome.org/pub/GNOME/sources/gnome-themes-extras/0.9/gnome-themes-extras-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: gettext, gtk2-devel, perl(XML::Parser), gtk2-engines >= 2.6
Requires: gnome-icon-theme, gnome-themes
Obsoletes: themes-meta-nuvola

%description
The Gnome themes extras package is a collection of metathemes for the Gnome
desktop environment. This package requires that you use a Gnome 2.2 release or
newer to work properly. The design goal of this package is to give Gnome users
an extra set of themes that are not only functional, but also eye catching.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
#makeinstall
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING README TODO
%dir %{_datadir}/icons
%dir %{_datadir}/themes
%{_datadir}/icons/Amaranth/
%{_datadir}/icons/Gorilla/
%{_datadir}/icons/Lush/
%{_datadir}/icons/Nuvola/
%{_datadir}/icons/Wasp/
%{_datadir}/themes/Amaranth/
%{_datadir}/themes/Gorilla/
%{_datadir}/themes/Lush/
%{_datadir}/themes/Nuvola/
%{_datadir}/themes/Nuvola-old/
%{_datadir}/themes/Wasp/

%changelog 
* Sun Jul 08 2007 Heiko Adams <info@fedora-blog.de> - 0.9.0-6
- Rebuild for RPMforge.

* Mon Aug 27 2006 Michael J. Knox <michael[AT]knox.net.nz> - 0.9.0-5
- Rebuild for FC6
- fixed messed up changelog

* Tue Jun 06 2006 Michael J. Knox <michael[AT]knox.net.nz> - 0.9.0-3
- add builreq on perl(XML::Parser)

* Wed Apr 26 2006 Michael J. Knox <michael[AT]knox.net.nz> - 0.9.0-2
- use bz2 tarball

* Tue Apr 24 2006 Michael J. Knox <michael[AT]knox.net.nz> - 0.9.0-1
- updated version to 0.9.0
- some house work

* Mon Apr 11 2005 Adrian Reber <adrian@lisas.de> - 0.8.1-1
- updated to 0.8.1
- BuildArch: noarch

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Mon Feb 28 2005 Adrian Reber <adrian@lisas.de> - 0.8.0-2
- added a patch with a fix for compiler warnings (bug #149713)

* Fri Nov 26 2004 Adrian Reber <adrian@lisas.de> - 0:0.8.0-0.fdr.1
- updated to 0.8.0
- changed gtk-2.0/2.2 to gtk-2.0/2.4
- libsmooth.so is deleted during installation as it is
  provided by gnome-themes
- removed empty NEWS file from doc

* Wed Oct 01 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:0.4-0.fdr.1
- Updated to 0.4.

* Sun Sep 21 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:0.3-0.fdr.2
- Fixed file permission on source tarball.
- Brought package more inline with current spec template.

* Sun Aug 31 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:0.3-0.fdr.1
- Updated to 0.3.

* Thu Aug 07 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:0.2-0.fdr.2
- Obsoletes themes-meta-nuvola.
- Req gnome-icon-theme.
- Req gnome-themes.

* Wed Aug 06 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:0.2-0.fdr.1
- Initial RPM release.
