# $Id$
# Authority: hadams

Name:           gnome-themes-extras
Version:        0.9.0
Release:        6

Summary:        Collection of metathemes for the Gnome desktop environment

Group:          User Interface/Desktops
License:        LGPL
URL:            http://librsvg.sourceforge.net/theme.php
Source0:        ftp://ftp.gnome.org/pub/GNOME/sources/gnome-themes-extras/0.9/%{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  gettext, gtk2-devel, perl(XML::Parser), gtk2-engines >= 2.6
Requires:       gnome-icon-theme
Requires:       gnome-themes

Obsoletes:      themes-meta-nuvola

BuildArch:      noarch

%description
The Gnome themes extras package is a collection of metathemes for the Gnome
desktop environment. This package requires that you use a Gnome 2.2 release or
newer to work properly. The design goal of this package is to give Gnome users
an extra set of themes that are not only functional, but also eye catching.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%makeinstall

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog README TODO
%dir %{_datadir}/icons
%dir %{_datadir}/themes
%{_datadir}/icons/*
%{_datadir}/themes/*


%changelog 
* Sun Jul 08 2007 Heiko Adams <info@fedora-blog.de> - 0.9.0-6
- Rebuild for rpmforge

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
