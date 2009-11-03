# $Id$
# Authority: dag

Summary: Checks DNS files for errors
Name: nslint
Version: 2.1a3
Release: 1%{?dist}
License: BSD
Group: Applications/Internet

Source: ftp://ftp.ee.lbl.gov/nslint-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
nslint is a lint-like program that checks DNS files for errors. 
DNS or Domain Name System generally maps names to IP addresses
and e-mail addresses in a hierarchical fashion.

Errors detected include missing trailing dots, illegal characters
(RFC 1034), A records without matching PTR records and vice-versa,
duplicat names in a subnet, duplicate names for an address,
names with cname records (RFC 1033) missing quotes, and unknown keywords.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 nslint %{buildroot}%{_bindir}/nslint
%{__install} -Dp -m0644 nslint.8 %{buildroot}%{_mandir}/man8/nslint.8

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES FILES INSTALL README VERSION
%{_mandir}/man8/nslint.8*
%{_bindir}/nslint

%changelog 
* Fri Feb 23 2007 Dag Wieers <dag@wieers.com> - 2.1a3-1
- Initial package. (using DAR)
