# $Id$
# Authority: dag

Summary: Makes output from tcpdump easier to read and parse
Name: sniff
Version: 2.3
Release: 1.2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://www.thedumbterminal.co.uk/software/sniff.shtml

Source: http://www.thedumbterminal.co.uk/software/files/sniff-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Buildarch: noarch
BuildRequires: perl
Requires: perl

%description
sniff makes output from the tcpdump program easier to read and parse.

%prep
%setup

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 sniff %{buildroot}%{_bindir}/sniff

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README sniff.shtml
%{_bindir}/sniff

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 2.3-1.2
- Rebuild for Fedora Core 5.

* Sun May 08 2005 Dag Wieers <dag@wieers.com> - 2.3-1
- Initial package. (using DAR)
