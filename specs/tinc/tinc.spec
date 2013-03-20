# $Id$
# Authority: dag

### FIXME: Add sysv script and default configuration.

Summary: Virtual private network daemon
Name: tinc
Version: 1.0.20
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://www.tinc-vpn.org/

Source: http://www.tinc-vpn.org/packages/tinc-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: lzo-devel
BuildRequires: openssl >= 0.9.7
BuildRequires: openssl-devel

%description
tinc is a Virtual Private Network (VPN) daemon that uses tunnelling
and encryption to create a secure private network between hosts on
the Internet. Because the tunnel appears to the IP level network
code as a normal network device, there is no need to adapt any
existing software. This tunnelling allows VPN sites to share
information with each other over the Internet without exposing any
information to others.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 src/tincd %{buildroot}%{_sbindir}/tincd
%{__install} -Dp -m0644 doc/tincd.8 %{buildroot}%{_mandir}/man8/tincd.8
%{__install} -Dp -m0644 doc/tinc.conf.5 %{buildroot}%{_mandir}/man5/tinc.conf.5

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING* NEWS README THANKS
%doc doc/sample-config* doc/tinc.info* doc/tinc.texi
%doc %{_mandir}/man5/tinc.conf.5*
%doc %{_mandir}/man8/tincd.8*
%{_sbindir}/tincd

%changelog
* Wed Mar 13 2013 David Hrbáč <david@hrbac.cz> - 1.0.20-1
- new upstream release

* Wed Jun 27 2012 David Hrbáč <david@hrbac.cz> - 1.0.19-1
- new upstream release

* Fri Mar 30 2012 David Hrbáč <david@hrbac.cz> - 1.0.18-1
- new upstream release

* Sat Mar 10 2012 David Hrbáč <david@hrbac.cz> - 1.0.17-1
- new upstream release

* Mon Aug 01 2011 Dag Wieers <dag@wieers.com> - 1.0.16-1
- Updated to release 1.0.16.

* Wed May 11 2011 Dag Wieers <dag@wieers.com> - 1.0.14-1
- Updated to release 1.0.14.

* Mon Apr 19 2010 Dag Wieers <dag@wieers.com> - 1.0.13-1
- Updated to release 1.0.13.

* Tue Nov 03 2009 Dag Wieers <dag@wieers.com> - 1.0.11-1
- Updated to release 1.0.11.

* Thu Oct 22 2009 Dag Wieers <dag@wieers.com> - 1.0.10-1
- Updated to release 1.0.10.

* Mon Dec 29 2008 Dag Wieers <dag@wieers.com> - 1.0.9-1
- Updated to release 1.0.9.

* Wed May 16 2007 Dag Wieers <dag@wieers.com> - 1.0.8-1
- Updated to release 1.0.8.

* Wed Jan 10 2007 Dag Wieers <dag@wieers.com> - 1.0.7-1
- Updated to release 1.0.7.

* Tue Dec 19 2006 Dag Wieers <dag@wieers.com> - 1.0.6-1
- Updated to release 1.0.6.

* Wed Nov 05 2006 Dag Wieers <dag@wieers.com> - 1.0.5-1
- Updated to release 1.0.5.

* Wed May 04 2005 Dag Wieers <dag@wieers.com> - 1.0.4-1
- Updated to release 1.0.4.

* Fri Nov 12 2004 Dag Wieers <dag@wieers.com> - 1.0.3-1
- Updated to release 1.0.3.

* Mon Nov 17 2003 Dag Wieers <dag@wieers.com> - 1.0.2-0
- Updated to release 1.0.2.

* Sat Aug 16 2003 Dag Wieers <dag@wieers.com> - 1.0.1-0
- Initial package. (using DAR)
