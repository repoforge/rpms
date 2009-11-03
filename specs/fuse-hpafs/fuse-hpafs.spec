# $Id$
# Authority: dag

%define real_name hpafs

Summary: FUSE based filesystem to access the Hidden Protected Area (HPA) on disk
Name: fuse-hpafs
Version: 0.1.0
Release: 1%{?dist}
License: GPL
Group: System Environment/Kernel
URL: http://home.tiscali.nl/pebolle/code/hpafs/

Source: http://home.tiscali.nl/pebolle/code/hpafs/hpafs-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: fuse-devel >= 2.2
Requires: fuse >= 2.2

Obsoletes: hpafs <= %{name}-%{version}
Provides: hpafs = %{name}-%{version}

%description
hpafs is a FUSE based filesystem to access the Hidden Protected Area (HPA)
on disk.

%prep
%setup -n %{real_name}-%{version}

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
#%{__make} install DESTDIR="%{buildroot}"
%{__install} -Dp -m0755 hpafs %{buildroot}%{_bindir}/hpafs

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING README
%{_bindir}/hpafs

%changelog
* Thu Nov 01 2007 Dag Wieers <dag@wieers.com> - 0.1.0-1
- Initial package. (using DAR)
