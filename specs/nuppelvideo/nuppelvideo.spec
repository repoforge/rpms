# $Id$
# Authority: dag
# Upstream: Roman Hochleitner <roman$mars,tuwien,ac,at>


%{?fc4:%define _without_modxorg 1}
%{?el4:%define _without_modxorg 1}
%{?fc3:%define _without_modxorg 1}
%{?fc2:%define _without_modxorg 1}
%{?fc1:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}
%{?rh9:%define _without_modxorg 1}
%{?rh8:%define _without_modxorg 1}
%{?rh7:%define _without_modxorg 1}
%{?el2:%define _without_modxorg 1}
%{?rh6:%define _without_modxorg 1}

%define real_name NuppelVideo
%define real_version 0.52a

Summary: NuppelVideo recording tool
Name: nuppelvideo
Version: 0.51.81
Release: 0.2%{?dist}
Group: Applications/Multimedia
License: GPL
URL: http://frost.htu.tuwien.ac.at/~roman/nuppelvideo/

Source: http://frost.htu.tuwien.ac.at/~roman/%{name}/%{real_name}-%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%{?_without_modxorg:BuildRequires: XFree86-devel}
%{!?_without_modxorg:BuildRequires: libX11-devel}

%description
NuppelVideo recording tool.

%prep
%setup -n %{real_name}-%{real_version}

%build
%{__perl} -pi -e 's|/usr/local/bin|%{buildroot}%{_bindir}|' Makefile
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc LICENSE* README*
%{_bindir}/*

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.51.81-0.2
- Rebuild for Fedora Core 5.

* Sun Mar 23 2003 Dag Wieers <dag@wieers.com> - 0.51.81
- Initial package. (using DAR)
