# $Id$
# Authority: dries
# Upstream: Theo Van Dinter <felicity$kluge,net>

%define real_version 3_3

Summary: Automate changes to DNS zone files
Name: mkrdns
Version: 3.3
Release: 1%{?dist}
License: GPL
Group: Applications/Utilities
URL: http://www.mkrdns.org/

Source: http://www.mkrdns.org/ftp/mkrdns-%{real_version}.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Buildarch: noarch

%description
mkrdns is a small Perl script that helps automate changes to your DNS zone 
files. It does this by reading your named.boot/named.conf file to find all 
the domains/networks for which you are authoritative. It then reads all of 
the forward zone files and generates PTR records which it inserts in the 
reverse zone maps.

%prep
%setup -cT
zcat %{SOURCE0} >mkrdns

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 mkrdns %{buildroot}%{_bindir}/mkrdns

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_bindir}/mkrdns

%changelog
* Thu Nov 29 2007 Dries Verachtert <dries@ulyssis.org> - 3.3-1
- Initial package.
