# $Id$
# Authority: dag


Summary: Print average throughput for a tcp connection
Name: tcpspray
%define real_version 1.1a
Version: 1.1
Release: 0.a.2%{?dist}
License: Unknown
Group: Applications/Internet
URL: http://ftp.linux.org.uk/pub/linux/Networking/attic/Other/tcpspray/

Source: http://ftp.linux.org.uk/pub/linux/Networking/attic/Other/tcpspray/tcpspray.%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Print average throughput for a tcp connection.

%prep
%setup -n %{name}
%build
%{__make} %{?_smp_mflags} \
	LDFLAGS="-s"

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 tcpspray %{buildroot}%{_bindir}/tcpspray
%{__install} -Dp -m0644 tcpspray.1 %{buildroot}%{_mandir}/man1/tcpspray.1

%files
%defattr(-, root, root, 0755)
%doc %{_mandir}/man1/tcpspray.1*
%{_bindir}/tcpspray

%clean
%{__rm} -rf %{buildroot}

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.1-0.a.2
- Rebuild for Fedora Core 5.

* Wed Nov 26 2003 Dag Wieers <dag@wieers.com> - 1.1-0.a
- Repackaged using DAR.

* Sun Jan 30 2000 Dag Wieers <dag@mind.be> - 1.1a-0
- Initial package.
