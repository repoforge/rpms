# $Id$
# Authority: dag

%define real_name obexfs

Summary: FUSE based filesystem using ObexFTP
Name: fuse-obexfs
Version: 0.8
Release: 1
License: GPL
Group: System Environment/Kernel
URL: http://dev.zuckschwerdt.org/openobex/wiki/ObexFs/

Source: http://downloads.sourceforge.net/openobex/obexfs-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: fuse-devel >= 2.2, libobexftp-devel >= 0.19
Requires: fuse >= 2.2, libobexftp >= 0.19

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
* Sat May 12 2007 Dag Wieers <dag@wieers.com> - 0.8-1
- Initial package. (using DAR)
