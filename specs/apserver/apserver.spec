# $Id$

# Authority: dries

Summary: A NTLM authorization proxy server.
Name: apserver
Version: 0.9.8
Release: 2
License: GPL
Group: System Environment/Daemons
URL: http://apserver.sf.net/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://apserver.sf.net/aps098.tar.gz
BuildRoot: %{_tmppath}/root-%{_name}-%{_version}
BuildRequires: dos2unix
Requires: python

%description
'NTLM Authorization Proxy Server' (APS) is a proxy software that allows you
to authenticate via an MS Proxy Server using the proprietary NTLM
protocol.It can change arbitrary values in your client's request header so
that those requests will look like they were created by MS IE.

%prep
%{__rm} -rf "${RPM_BUILD_ROOT}"
%setup -n aps098

%build
dos2unix server.cfg
cat > apserver <<EOF
#!/bin/bash
cd /usr/share/apserver
python main.py -c /etc/apserver.cfg
EOF

%install
echo RPM_BUILD_ROOT is $RPM_BUILD_ROOT
export DESTDIR=$RPM_BUILD_ROOT
mkdir -p ${DESTDIR}/usr/bin/
mkdir -p ${DESTDIR}/usr/share/apserver/
mkdir -p ${DESTDIR}/etc/
cp apserver ${DESTDIR}/usr/bin/
chmod +x ${DESTDIR}/usr/bin/apserver
cp server.cfg ${DESTDIR}/etc/apserver.cfg
cp -R main.py lib ${DESTDIR}/usr/share/apserver/

%files
%defattr(-,root,root, 0755)
%doc research.txt readme.txt Install.txt COPYING doc
%{_sysconfdir}/apserver.cfg
%{_bindir}/apserver
/usr/share/apserver

%changelog
* Sat Jan 10 2004 Dries Verachtert <dries@ulyssis.org> 0.9.8-2
- spec file cleanup

* Fri Dec 26 2003 Dries Verachtert <dries@ulyssis.org> 0.9.8-1
- first packaging for Fedora Core 1
