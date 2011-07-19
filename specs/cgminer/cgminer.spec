# $Id$
# Authority: yury
# Upstream: Con Kolivas <kernel$kolivas,org>

Summary: CPU/GPU Miner by Con Kolivas
Name: cgminer
Version: 1.3.0
Release: 1%{?dist}
License: GPLv2
Group: Applications/Internet
URL: http://forum.bitcoin.org/index.php?topic=28402.0

Source: http://ck.kolivas.org/apps/%{name}/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc
BuildRequires: make
BuildRequires: yasm >= 1.1.0

%if 0%{?el6}
BuildRequires: libcurl-devel
%else
BuildRequires: curl-devel
%endif

BuildRequires: ncurses-devel
BuildRequires: pkgconfig >= 0.9.0

%description
This is a multi-threaded CPU and GPU miner for Bitcoin.

The present package is compiled without support for GPU mining, so only
CPU mining is possible at this moment.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags} CFLAGS="-O3 -Wall"

%install
%{__make} install DESTDIR=%{buildroot}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README
%{_bindir}/cgminer
%exclude %{_bindir}/*.cl

%changelog
* Tue Jul 19 2011 Yury V. Zaytsev <yury@shurup.com> - 1.3.0-1
- Updated to release 1.3.0.

* Mon Jul 18 2011 Yury V. Zaytsev <yury@shurup.com> - 1.2.8-1
- Updated to release 1.2.8.

* Sun Jul 17 2011 Yury V. Zaytsev <yury@shurup.com> - 1.2.7-1
- Initial package.
