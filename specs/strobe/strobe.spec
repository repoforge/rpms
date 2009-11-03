# $Id$
# Authority: dag

Summary: Super optimized TCP port surveyor
Name: strobe
Version: 1.06
Release: 1.2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://ftp.cerias.purdue.edu/pub/tools/unix/scanners/strobe/

Source: http://ftp.cerias.purdue.edu/pub/tools/unix/scanners/strobe/strobe-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
strobe is a network/security tool that locates and describes all
listening tcp ports on a (remote) host or on many hosts in a bandwidth
utilisation maximising, and process resource minimizing manner.


%prep
%setup -n %{name}

%build
%{__make} %{?_smp_mflags} \
	FLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 strobe %{buildroot}%{_bindir}/strobe
%{__install} -Dp -m0644 strobe.1 %{buildroot}%{_mandir}/man1/strobe.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYRIGHT CREDITS HISTORY INSTALL TODO VERSION strobe.services
%doc %{_mandir}/man1/strobe.1*
%{_bindir}/strobe

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.06-1.2
- Rebuild for Fedora Core 5.

* Sun Feb 13 2005 Dag Wieers <dag@wieers.com> - 1.06-1
- Initial package. (using DAR)
