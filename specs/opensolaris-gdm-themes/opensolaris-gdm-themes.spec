# $Id$
# Authority: hadams

Name:			opensolaris-gdm-themes
License:		LGPL
Group:			System/GUI/GNOME
BuildArchitectures:	noarch
Version:		0.2
Release:		1%{?dist}
Distribution:		Mercury
Vendor:			OpenSolaris Project.
Summary:		OpenSolaris branded GNOME login manager theme
Source:			%{name}-%{version}.tar.gz
URL:			http://dlc.sun.com/osol/jds/downloads/extras/
BuildRoot:		%{_tmppath}/%{name}-%{version}-build
Docdir:			%{_defaultdocdir}/%{name}
Autoreqprov:		on

%define intltool_version 0.25

BuildRequires:  intltool >= %{intltool_version}

%description
This package contains OpenSolaris branded GNOME login manager [GDM] themes 

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
* Sat Jan 26 2008 Heiko Adams <info-2007@fedora-blog.de> 0.2-1
- Version update to 0.2

* Wed Nov 21 2007 Heiko Adams <info@fedora-blog.de> 0.1-1
- Initial CentOS Build
