# Authority: freshrpms
Summary: Utility for getting and setting Xv attributes.
Name: xvattr
Version: 1.3
Release: 0
License: GPL
Group: User Interface/X
URL: http://www.dtek.chalmers.se/groups/dvd/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.dtek.chalmers.se/groups/dvd/dist/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: XFree86-devel, gtk+-devel

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
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING ChangeLog NEWS README
%doc %{_mandir}/man1/*
%{_bindir}/*

%changelog
* Thu Feb 20 2003 Dag Wieers <dag@wieers.com> - 1.3-0
- Initial package. (using DAR)
