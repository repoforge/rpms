# $Id$
# Authority: dag
# Upstream: Brent Chun <bnc$theether,org>

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')

Summary: Parallel SSH tools
Name: pssh
Version: 1.2.2
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://www.theether.org/pssh/

Source: http://www.theether.org/pssh/pssh-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python
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
%{__install} -Dp -m0644 lib/python/psshutil.py %{buildroot}%{python_sitearch}/psshutil.py
%{__install} -Dp -m0644 lib/python/basethread.py %{buildroot}%{python_sitearch}/basethread.py

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%{_bindir}/pssh
%{_bindir}/pscp
%{_bindir}/pnuke
%{_bindir}/prsync
%{_bindir}/pslurp
%{python_sitearch}/psshutil.py
%{python_sitearch}/basethread.py

%changelog
* Mon Jun 19 2006 Dag Wieers <dag@wieers.com> - 1.2.2-1
- Updated to release 1.2.2.

* Wed Nov 10 2004 Dag Wieers <dag@wieers.com> - 1.2.0-1
- Initial package. (using DAR)
