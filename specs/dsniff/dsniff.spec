# $Id$
# Authority: dag
# Upstream: Dug Song <dugsong$monkey,org>

%{?dist: %{expand: %%define %dist 1}}

%define _libdir %{_sysconfdir}

Summary: Tools for network auditing and penetration testing
Name: dsniff
Version: 2.4
Release: 0.b1
License: GPL
Group: Applications/Internet
URL: http://www.monkey.org/~dugsong/dsniff/

Source: http://www.monkey.org/~dugsong/dsniff/beta/dsniff-%{version}b1.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libnet > 1.0, libnet < 1.1, libnids >= 1.16, openssl-devel >= 0.9.5a

%description
dsniff is a collection of tools for network auditing and penetration testing.

%prep
%setup

### FIXME: Make it build for RH9 and RHEL3
%{?el3:%{__perl} -pi.orig -e 's|^(INCS	=) |$1 -I/usr/kerberos/include |' Makefile.in}
%{?rh9:%{__perl} -pi.orig -e 's|^(INCS	=) |$1 -I/usr/kerberos/include |' Makefile.in}

%{__perl} -pi.orig -e 's|/usr/local/lib/|%{_sysconfdir}/|' *.8 pathnames.h

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_sbindir} \
			%{buildroot}%{_mandir}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES LICENSE README TODO
%doc %{_mandir}/man8/*.8*
%config(noreplace) %{_sysconfdir}/*
%{_sbindir}/*

%changelog
* Fri Nov 26 2004 Dag Wieers <dag@wieers.com> - 2.4-0.b1
- Updated to release 2.4b1.

* Mon Sep 15 2003 Dag Wieers <dag@wieers.com> - 2.3-0
- Initial package. (using DAR)
