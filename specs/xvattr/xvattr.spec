# $Id$
# Authority: matthias
# Upstream: Björn Englund <d4bjorn$dtek,chalmers,se>

### EL6 ships with xvattr-1.3-18.el6
# ExclusiveDist: el2 el3 el4 el5

%{?el4:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}
%{?el2:%define _without_modxorg 1}

Summary: Utility for getting and setting Xv attributes
Name: xvattr
Version: 1.3
Release: 4%{?dist}
License: GPL
Group: User Interface/X
URL: http://www.dtek.chalmers.se/groups/dvd/

Source: http://www.dtek.chalmers.se/groups/dvd/dist/xvattr-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtk+-devel
%{!?_without_modxorg:BuildRequires: libX11-devel, libXv-devel}
%{?_without_modxorg:BuildRequires: XFree86-devel}

%description
This program is used for getting and setting Xv attributes such as
XV_BRIGHTNESS, XV_CONTRAST, XV_SATURATION, XV_HUE, XV_COLORKEY, ...

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
%doc AUTHORS COPYING ChangeLog NEWS README
%doc %{_mandir}/man?/*
%{_bindir}/*

%changelog
* Wed Mar 24 2004 Matthias Saou <http://freshrpms.net/> 1.3-4
- Remove explicit XFree86 dependency for the binary package.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 1.3-3
- Rebuild for Fedora Core 1.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.

* Fri Oct 4 2002 Matthias Saou <http://freshrpms.net/>
- Initial rpm release.

