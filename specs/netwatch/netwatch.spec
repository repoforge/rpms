# $Id$
# Authority: dag
# Upstream: Gordon MacKay <mackay@uno.slctech.org>

%define real_version 1.0a

Summary: Ethernet/PPP IP Packet Monitor
Name: netwatch
Version: 1.0
Release: 0.a
License: GPL
Group: Applications/Internet
URL: http://www.slctech.org/~mackay/netwatch.html

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.slctech.org/~mackay/netwatch-%{real_version}.src.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description 
The software enables real-time viewing of network activity.
Network usage is tracked on a per host basis. Packet
and byte counts are available for all host communication.
Router statistics and summary charts are available.
 
%prep
%setup -n %{name}-%{real_version}

%{__perl} -pi.orig -e '
		s|chown|#chown|;
		s|\$\(INSTALLDIR\)|\$(bindir)|;
		s|/usr/man|\$(mandir)|;
	' Makefile.in

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir} \
			%{buildroot}%{_mandir}/man1/
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc BUGS CHANGES COPYING README* TODO
%doc %{_mandir}/man?/*
%{_bindir}/*

%changelog
* Sun Apr 25 2004 Dag Wieers <dag@wieers.com> - 1.0-0.a
- Initial package. (using DAR)
