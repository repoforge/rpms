# $Id$
# Authority: dag
# Upstream: Brent Chun <bnc$theether,org>

%define python_version %(python -c 'import sys; print sys.version[:3]')

Summary: Parallel SSH tools
Name: pssh
Version: 1.2.0
Release: 1.dag
License: GPL
Group: Applications/Internet
URL: http://www.theether.org/pssh/

Source: http://www.theether.org/pssh/pssh-%{version}.tar.gz 
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Requires: openssh, python >= 2.0

%description
This package provides various parallel tools based on ssh and scp.

%prep 
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 bin/pssh %{buildroot}%{_bindir}/pssh
%{__install} -Dp -m0755 bin/pscp %{buildroot}%{_bindir}/pscp
%{__install} -Dp -m0755 bin/pnuke %{buildroot}%{_bindir}/pnuke
%{__install} -Dp -m0755 bin/prsync %{buildroot}%{_bindir}/prsync
%{__install} -Dp -m0755 bin/pslurp %{buildroot}%{_bindir}/pslurp
%{__install} -Dp -m0644 lib/python2.2/psshutil.py %{buildroot}%{_libdir}/python%{python_version}/psshutil.py
%{__install} -Dp -m0644 lib/python2.2/basethread.py %{buildroot}%{_libdir}/python%{python_version}/basethread.py

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_bindir}/pssh
%{_bindir}/pscp
%{_bindir}/pnuke
%{_bindir}/prsync
%{_bindir}/pslurp
%{_libdir}/python%{python_version}/psshutil.py
%{_libdir}/python%{python_version}/basethread.py

%changelog
* Wed Nov 10 2004 Dag Wieers <dag@wieers.com> - 1.2.0-1
- Initial package. (using DAR)
