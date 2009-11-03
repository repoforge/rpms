# $Id$
# Authority: dag
# Upstream: Kevin Vigor <kevin$vigor,nu>

%{?dtag: %{expand: %%define %dtag 1}}

%{?fc4:%define _without_modxorg 1}
%{?el4:%define _without_modxorg 1}
%{?fc3:%define _without_modxorg 1}
%{?fc2:%define _without_modxorg 1}
%{?fc1:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}
%{?rh9:%define _without_modxorg 1}
%{?rh7:%define _without_modxorg 1}
%{?el2:%define _without_modxorg 1}
%{?yd3:%define _without_modxorg 1}

Summary: Differential X protocol compressor
Name: dxpc
Version: 3.9.0
Release: 1%{?dist}
License: BSD
Group: User Interface/X
URL: http://www.vigor.nu/dxpc/

Source: http://www.vigor.nu/dxpc/%{version}/dxpc-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: lzo-devel, gcc-c++
%{!?_without_modxorg:BuildRequires: libX11-devel}
%{?_without_modxorg:BuildRequires: XFree86-devel}

%description
dxpc is an X protocol compressor designed to improve the
speed of X11 applications run over low-bandwidth links
(such as dialup PPP connections).

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall \
	man1dir="%{buildroot}%{_mandir}/man1/"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES README* TODO
%doc %{_mandir}/man1/dxpc.1*
%{_bindir}/dxpc

%changelog
* Sat Apr 15 2006 Dag Wieers <dag@wieers.com> - 3.9.0-1
- Initial package. (using DAR)

* Thu Oct 09 2003 Dag Wieers <dag@wieers.com> - 3.8.2-0
- Initial package. (using DAR)
