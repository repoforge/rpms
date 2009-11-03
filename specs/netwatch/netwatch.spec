# $Id$
# Authority: dag
# Upstream: Gordon MacKay <mackay$uno,slctech,org>

Summary: Ethernet/PPP IP Packet Monitor
Name: netwatch
Version: 1.0c
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://www.slctech.org/~mackay/netwatch.html

Source: http://www.slctech.org/~mackay/netwatch-%{version}.src.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: ncurses-devel

%description
The software enables real-time viewing of network activity.
Network usage is tracked on a per host basis. Packet
and byte counts are available for all host communication.
Router statistics and summary charts are available.

%prep
%setup

%{__perl} -pi.orig -e '
		s|chown|#chown|;
		s|\$\(INSTALLDIR\)|\$(bindir)|;
		s|/usr/man|\$(mandir)|;
	' Makefile.in

%build
./configure
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
%doc %{_mandir}/man1/netwatch.1*
%{_bindir}/netresolv
%{_bindir}/netwatch

%changelog
* Thu Dec 21 2006 Dag Wieers <dag@wieers.com> - 1.0c-1
- Updated to release 1.0c.

* Sun Apr 25 2004 Dag Wieers <dag@wieers.com> - 1.0-0.a
- Initial package. (using DAR)
