# $Id$

# Authority: dag

Summary: A TCP hijacking tool.
Name: hunt
Version: 1.5
Release: 0
License: GPL
Group: Applications/Internet
URL: http://lin.fsid.cvut.cz/~kra/#HUNT

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://lin.fsid.cvut.cz/~kra/hunt/%{name}-%{version}.tgz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

%description
hunt is a program for intruding into a connection, watching it
and resetting it.

hunt is operating on Ethernet and is best used for connections
which can be watched through it. However, it is possible to do
something even for hosts on another segments or hosts that are
on switched ports. 

hunt doesn't distinguish between local network connections and
connections going to/from Internet. It can handle all
connections it sees.

%prep
%setup 

%build
%{__make} %{?_smp_mflags} \
	CFLAGS="%{optflags}"
%{__make} %{?_smp_mflags} -C tpserv \
	CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_sbindir} \
			%{buildroot}%{_mandir}/man1/
%{__install} -m0755 hunt tpserv/tpserv tpsetup/transproxy %{buildroot}%{_sbindir}
%{__install} -m0644 man/hunt.1 %{buildroot}%{_mandir}/man1/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES COPYING README README.tp TODO
%doc %{_mandir}/man?/*
%{_sbindir}/*

%changelog
* Sun Jul 13 2003 Dag Wieers <dag@wieers.com> - 1.5-0
- Initial package. (using DAR)
