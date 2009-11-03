# $Id$
# Authority: dag

%define real_name obexfs

Summary: FUSE based filesystem using ObexFTP
Name: fuse-obexfs
Version: 0.12
Release: 1%{?dist}
License: GPL
Group: System Environment/Kernel
URL: http://dev.zuckschwerdt.org/openobex/wiki/ObexFs/

Source: http://dl.sf.net/openobex/obexfs-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: fuse-devel >= 2.2
BuildRequires: libobexftp-devel >= 0.22
Requires: fuse >= 2.2
Requires: libobexftp >= 0.22

Obsoletes: obexfs <= %{name}-%{version}
Provides: obexfs = %{name}-%{version}

%description
ObexFS is a FUSE based filesystem using ObexFTP.

%prep
%setup -n %{real_name}-%{version}

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
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%{_bindir}/obexfs
%{_bindir}/obexautofs

%changelog
* Mon Apr 27 2009 Dag Wieers <dag@wieers.com> - 0.12-1
- Updated to release 0.12.

* Mon Jun 16 2008 Dag Wieers <dag@wieers.com> - 0.11-1
- Updated to release 0.11.

* Tue Nov 13 2007 Dag Wieers <dag@wieers.com> - 0.10-1
- Updated to release 0.10.

* Sat May 12 2007 Dag Wieers <dag@wieers.com> - 0.8-1
- Initial package. (using DAR)
