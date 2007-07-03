# $Id$
# Authority: hadams

#
# spec file for package sun-gdm-themes
#
# Copyright (c) 2003 Sun Microsystems Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#


Name:			sun-gdm-themes
License:		LGPL
Group:			System/GUI/GNOME
BuildArchitectures:	noarch
Version:		0.25
Release:		12
Distribution:		Mercury
Vendor:			Sun Microsystems Inc.
Summary:		Sun branded GNOME login manager theme
Source:			%{name}-%{version}.tar.gz
URL:			http://sun.com
BuildRoot:		%{_tmppath}/%{name}-%{version}-build
Docdir:			%{_defaultdocdir}/%{name}
Autoreqprov:		on

%define intltool_version 0.25

BuildRequires:  intltool >= %{intltool_version}

%description
This package contains Sun branded GNOME login manager [GDM] themes 

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" \
./configure \
	--prefix=%{_prefix} \
	--sysconfdir=%{_sysconfdir} \
	--localstatedir=/var/lib
make

%install
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%post

%files
%defattr (-, root, root)
%{_datadir}/gdm/themes/*

%changelog
* Tue Jun 28 2007 Heiko Adams <info@fedora-blog.de> 0.25-12
- Initial CentOS Build
* Sun Oct 26 2003 - <carl.gadener@sun.com>
- Bolder and Blue JDS banner
- Improved button alignment to handle all resolutions
- Offset panel 5% right/down according to Chester
- Changed order of buttons left-to-right with right most important
* Wed Oct 23 2003 - <carl.gadener@sun.com>
- Bolder Java Desktop System banner
- Sun Font on JDS
- Color Java Logo
* Tue Oct 21 2003 - glynn.foster@sun.com
- Updated tarball
* Sun Oct 19 2003 - damien.donlon@sun.com
- Adding sun-gdm-themes-l10n-po-0.4.tar.bz2 l10n content
* Tue Sep 02 2003 - <carl.gadener@sun.com>
- Added the new Sun default theme 
- renamed the others to meaningful names
* Fri Aug 08 2003 - <erwann@sun.com>
- bumped release for the new icons
* Tue Jul 22 2003 - <markmc@sun.com>
- update to 0.8.9.1
* Fri Jun 26 2003 - glynn.foster@Sun.COM
- It's a no architecture package
* Fri Jun 26 2003 - glynn.foster@Sun.COM
- Initial Sun release

