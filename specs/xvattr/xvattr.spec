# $Id$

Summary: Utility for getting and setting Xv attributes
Name: xvattr
Version: 1.3
Release: 3.fr
License: GPL
Group: User Interface/X
URL: http://www.dtek.chalmers.se/groups/dvd/
Source: http://www.dtek.chalmers.se/groups/dvd/dist/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: XFree86, gtk+
BuildRequires: XFree86-devel, gtk+-devel

%description
This program is used for getting and setting Xv attributes such as
XV_BRIGHTNESS, XV_CONTRAST, XV_SATURATION, XV_HUE, XV_COLORKEY, ...

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%makeinstall

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_bindir}/g%{name}
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 1.3-3.fr
- Rebuild for Fedora Core 1.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.

* Fri Oct 4 2002 Matthias Saou <http://freshrpms.net/>
- Initial rpm release.

