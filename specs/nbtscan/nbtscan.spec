# $Id$

# Authority: dag
# Upstream: Alla Bezroutchko <alla$inetcat,org>

Summary: NetBIOS name network scanner
Name: nbtscan
Version: 1.5.1
Release: 1.2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://www.inetcat.org/software/nbtscan.html

Source: http://www.inetcat.org/software/nbtscan-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

#BuildRequires:

%description
NBTscan is a program for scanning IP networks for NetBIOS name
information. It sends NetBIOS status query to each address in
supplied range and lists received information in human readable
form. For each responded host it lists IP address, NetBIOS
computer name, logged-in user name and MAC address.

%prep
%setup -n %{name}-%{version}a

### FIXME: Make Makefile use autotool directory standard. (Please fix upstream)
%{__perl} -pi.orig -e 's|\@bindir\@|\$(sbindir)|' Makefile.in

%build
%configure \
	--disable-schemas-install
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}

### FIXME: Makefile doesn't create target directories (Please fix upstream)
%{__install} -d -m0755 %{buildroot}%{_sbindir}

%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING README
%{_sbindir}/*

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.5.1-1.2
- Rebuild for Fedora Core 5.

* Mon Mar 22 2004 Dag Wieers <dag@wieers.com> - 1.5.1-1
- Initial package. (using DAR)
