# $Id$

# Authority: dag

# Upstream: Kevin Vigor <kevin@vigor.nu>

Summary: A differential X protocol compressor.
Name: dxpc
Version: 3.8.2
Release: 0
License: BSD
Group: User Interface/X
URL: http://www.vigor.nu/dxpc/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.vigor.nu/dxpc/%{version}/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: lzo-devel

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
%doc %{_mandir}/man1/*
%{_bindir}/*

%changelog
* Thu Oct 09 2003 Dag Wieers <dag@wieers.com> - 3.8.2-0
- Initial package. (using DAR)
