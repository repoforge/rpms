# $Id$

# Authority: dag

### FIXME: Add sysv script and default configuration.

Summary: virtual private network daemon
Name: tinc
Version: 1.0.2
Release: 0
License: GPL
Group: Applications/Internet
URL: http://tinc.nl.linux.org/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://tinc.nl.linux.org/packages/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: openssl >= 0.9.7

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
%configure \
	--disable-dependency-tracking
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_sbindir} \
			%{buildroot}%{_mandir}/man5/ \
			%{buildroot}%{_mandir}/man8/
%{__install} -m0755 src/tincd %{buildroot}%{_sbindir}
%{__install} -m0644 doc/tincd.8 %{buildroot}%{_mandir}/man8/
%{__install} -m0644 doc/tinc.conf.5 %{buildroot}%{_mandir}/man5/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING* NEWS README THANKS TODO 
%doc doc/tinc.info* doc/tinc.texi doc/sample-config*
%doc %{_mandir}/man?/*
%{_sbindir}/*

%changelog
* Mon Nov 17 2003 Dag Wieers <dag@wieers.com> - 1.0.2-0
- Updated to release 1.0.2.

* Sat Aug 16 2003 Dag Wieers <dag@wieers.com> - 1.0.1-0
- Initial package. (using DAR)
