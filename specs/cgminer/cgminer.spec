# $Id$
# Authority: yury
# Upstream: Con Kolivas <kernel$kolivas,org>
#
# ExclusiveDist: el5 el6

Summary: CPU/GPU Miner by Con Kolivas
Name: cgminer
Version: 1.6.2
Release: 1%{?dist}
License: GPLv2
Group: Applications/Internet
URL: http://forum.bitcoin.org/index.php?topic=28402.0

Source0: http://ck.kolivas.org/apps/%{name}/%{name}-%{version}.tar.bz2

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc
BuildRequires: make
BuildRequires: yasm >= 1.1.0
BuildRequires: ncurses-devel
BuildRequires: pkgconfig >= 0.9.0

%if 0%{?el6}
BuildRequires: libcurl-devel
%endif

%if 0%{?el5}
BuildRequires: curl-devel
%endif

%description
This is a multi-threaded CPU and GPU miner for Bitcoin.

The present package is compiled without support for GPU mining, so only
CPU mining is possible at this moment.

%prep
%setup

%build

CFLAGS="%{optflags} -O2 -Wall" \
%configure

%{__make} %{?_smp_mflags}

%install
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README
%{_bindir}/cgminer
%exclude %{_bindir}/*.cl

%changelog
* Fri Sep 02 2011 Yury V. Zaytsev <yury@shurup.com> - 1.6.2-1
- Building against older curl works again, drop static version :-)
- Now only usable with -t flag (plain text interface) :-(
- CPU mining with -O3 is unstable, switched to -O2.
- Updated to release 1.6.2.

* Sun Jul 24 2011 Yury V. Zaytsev <yury@shurup.com> - 1.4.1-1
- Static build against libcurl from RHEL6 on RHEL5.
- Updated to release 1.4.1.

* Sat Jul 23 2011 Yury V. Zaytsev <yury@shurup.com> - 1.4.0-1
- Updated to release 1.4.0.

* Wed Jul 20 2011 Yury V. Zaytsev <yury@shurup.com> - 1.3.1-1
- Updated to release 1.3.1.

* Tue Jul 19 2011 Yury V. Zaytsev <yury@shurup.com> - 1.3.0-1
- Updated to release 1.3.0.

* Mon Jul 18 2011 Yury V. Zaytsev <yury@shurup.com> - 1.2.8-1
- Updated to release 1.2.8.

* Sun Jul 17 2011 Yury V. Zaytsev <yury@shurup.com> - 1.2.7-1
- Initial package.
