# $Id$
# Authority: hadams

Summary: Sun branded GNOME login manager theme
Name: sun-gdm-themes
Version: 0.25
Release: 1%{?dist}
License: LGPL
Group: User Interface/X
URL: http://sun.com/

Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: intltool >= 0.25, perl(XML::Parser)

%description
This package contains Sun branded GNOME login manager (GDM) themes.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%dir %{_datadir}/gdm/
%{_datadir}/gdm/themes/

%changelog
* Tue Jun 28 2007 Heiko Adams <info@fedora-blog.de> - 0.25-1
- Initial package for RPMforge.
