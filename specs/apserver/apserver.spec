# $Id$
# Authority: dries
# Upstream: Dmitry Rozmanov <dima$xenon,spb,ru>

%define real_name aps
%define real_release 098

Summary: NTLM authorization proxy server
Name: apserver
Version: 0.9.8
Release: 2.2%{?dist}
License: GPL
Group: System Environment/Daemons
URL: http://apserver.sourceforge.net/

Source: http://apserver.sf.net/aps%{real_release}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: dos2unix
Requires: python

%description
'NTLM Authorization Proxy Server' (APS) is a proxy software that allows you
to authenticate via an MS Proxy Server using the proprietary NTLM
protocol.It can change arbitrary values in your client's request header so
that those requests will look like they were created by MS IE.

%prep
%setup -n %{real_name}%{real_release}

%build
dos2unix server.cfg
%{__cat} <<EOF  >apserver.sh
#!/bin/bash
cd %{_datadir}/apserver
exec python main.py -c %{_sysconfdir}/apserver.cfg
EOF

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 apserver.sh %{buildroot}%{_bindir}/apserver
%{__install} -Dp -m0644 server.cfg %{buildroot}%{_sysconfdir}/apserver.cfg

%{__install} -Dp -m0644 main.py %{buildroot}%{_datadir}/apserver/main.py
%{__cp} -apv lib/ %{buildroot}%{_datadir}/apserver/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING doc/ Install.txt readme.txt research.txt
%config(noreplace) %{_sysconfdir}/apserver.cfg
%{_bindir}/apserver
%{_datadir}/apserver/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.9.8-2.2
- Rebuild for Fedora Core 5.

* Sun May 02 2004 Dag Wieers <dag@wieers.com> - 0.9.8-3
- Cosmetic cleanup.
- Use exec in startup script.
- Tag config-file and add noreplace.

* Sat Jan 10 2004 Dries Verachtert <dries@ulyssis.org> 0.9.8-2
- spec file cleanup

* Fri Dec 26 2003 Dries Verachtert <dries@ulyssis.org> 0.9.8-1
- first packaging for Fedora Core 1
