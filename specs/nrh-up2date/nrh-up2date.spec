# $Id$
# Authority: dag
# Upstream: <nrh-up2date-users$lists,sf,net>

%{?dtag: %{expand: %%define %dtag 1}}

Summary: Open Source server for Redhat's up2date suite
Name: nrh-up2date
Version: 1.3
Release: 0.2%{?dist}
License: GPL
Group: Applications/System
URL: http://www.nrh-up2date.org/

Source: http://www.nrh-up2date.org/download/nrh-up2date-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
Requires: perl, perl-Frontier-RPC, perl(XML::Parser), perl-BerkeleyDB, python, python-bsddb3
%{!?dtag:Requires: httpd, rpm, rpm-python, db4}
%{?el4:Requires: httpd, rpm, rpm-python, db4}
%{?fc3:Requires: httpd, rpm, rpm-python, db4}
%{?fc2:Requires: httpd, rpm, rpm-python, db4}
%{?fc1:Requires: httpd, rpm, rpm-python, db4}
%{?el3:Requires: httpd, rpm, rpm-python, db4}
%{?rh9:Requires: httpd, librpm404, rpm404-python, db4}
%{?rh8:Requires: httpd, librpm404, rpm404-python, db4}
%{?rh7:Requires: apache, python-xmlrpc, db3, perl-Digest-MD5}
%{?el2:Requires: apache, python-xmlrpc, db3, perl-Digest-MD5}
%{?rh6:Requires: apache, python-xmlrpc, db3, perl-Digest-MD5}

%description
NRH-up2date is a collection of utilities to use with RedHat's up2date
client without relying on the RedHat network servers. NRH-up2date is
implemented to provide an up2date server for a basic user, that wishes
to cache RHN content locally in his LAN (or central server), so each
client in that site wouldn't have to connect to RedHat network for
updates, waisting your bandwidth.

%prep
%setup

%{__perl} -pi.orig -e '
		s|\$\(INSTALL_ROOT\)|\$(DESTDIR)|g;
		s|\$\(PREFIX\)/share|\$(datadir)|g;
		s|\$\(PREFIX\)/sbin|\$(sbindir)|g;
		s|/etc|\$(sysconfdir)|g;
		s|/var|\$(localstatedir)|g;
	' Makefile

%build

%install
%{__rm} -rf %{buildroot}
%makeinstall \
	DOCS_DIR="./rpm-doc"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc rpm-doc/*
%config(noreplace) %{_sysconfdir}/nrh-up2date/
%{_sbindir}/*
%{_datadir}/nrh-up2date/
%{_localstatedir}/spool/nrh-up2date/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.3-0.2
- Rebuild for Fedora Core 5.

* Tue Mar 02 2004 Dag Wieers <dag@wieers.com> - 1.3-0
- Initial package. (using DAR)
