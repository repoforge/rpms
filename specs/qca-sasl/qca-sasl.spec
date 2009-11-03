# $Id$
# Authority: dag

Summary: SASL plugin for the Qt Cryptographic Architecture
Name: qca-sasl
Version: 1.0
Release: 1%{?dist}
License: LGPL
Group: Applications/Internet
URL: http://delta.affinix.com/qca/

Source: http://delta.affinix.com/download/qca/qca-sasl-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: qt-devel >= 1:3.0, cyrus-sasl-devel >= 2.0

%description
This is a plugin to provide SSL/SASL capability to programs that use the Qt
Cryptographic Architecture (QCA).  QCA is a library providing an easy API
for several cryptographic algorithms to Qt programs.  This package only
contains the SASL plugin.

%prep
%setup

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
