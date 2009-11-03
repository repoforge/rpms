# $Id$
# Authority: dag

%{?dtag: %{expand: %%define %dtag 1}}

%{!?dtag:%define _with_openssl098 1}
%{?el5:%define _with_openssl098 1}

Summary: TLS plugin for the Qt Cryptographic Architecture
Name: qca-tls
Version: 1.0
Release: 1%{?dist}
License: LGPL
Group: Applications/Internet
URL: http://delta.affinix.com/qca/

Source: http://delta.affinix.com/download/qca/qca-tls-%{version}.tar.bz2
Patch: qca-tls-1.0-mach.patch
Patch1: qca-tls-1.0-openssl098.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: qt-devel >= 1:3.0, openssl-devel
%{?_with_openssl098:BuildRequires: openssl-devel >= 0.9.8}

%description
This is a plugin to provide SSL/TLS capability to programs that use the Qt
Cryptographic Architecture (QCA).  QCA is a library providing an easy API
for several cryptographic algorithms to Qt programs.  This package only
contains the TLS plugin.

%prep
%setup
%patch0 -p0 -b .mach
%{?_with_openssl098:%patch1 -p0 -b .openssl098}

%build
source %{_sysconfdir}/profile.d/qt.sh
./configure --qtdir="$QTDIR"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}$QTDIR/plugins/crypto/
%{__make} install INSTALL_ROOT="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING README
%dir %{_libdir}/qt-*/
%dir %{_libdir}/qt-*/plugins/
%{_libdir}/qt-*/plugins/crypto/

%changelog
* Wed Jun 06 2007 Dag Wieers <dag@wieers.com> - 1.0-1
- Initial package. (using DAR)
