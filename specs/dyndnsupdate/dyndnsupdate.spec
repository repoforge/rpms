# $Id$

# Authority: dries
# Upstream: 

Summary: Update dndns hosts
Name: dyndnsupdate
Version: 0.8
Release: 1
License: GPL
Group: Applications/Internet
URL: http://lillesvin.linux.dk/dyndnsupdate/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://lillesvin.linux.dk/stuff/dyndnsupdate-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

# Screenshot: http://lillesvin.linux.dk/dyndnsupdate_screenshot.jpg

%description
DynDNSupdate is a small Bash-script to update your dyndns hosts at reboot or
from cron. It simply consists of 2 files, dyndnsupdate and dyndns.hosts.
dyndns.hosts holds information for the dyndns hosts, dyndnsupdate simply
processes the URLs in dyndns.hosts.

%prep
%setup

%build
# nothing to build...
sed -i "s/^some/#some/g;" dyndns.hosts.example

%install
%{__rm} -rf %{buildroot}
%{__install} -D -m 755 dyndnsupdate %{buildroot}%{_bindir}/dyndnsupdate
%{__install} -D -m 644 dyndns.hosts.example %{buildroot}%{_sysconfdir}/dyndns.hosts

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%{_bindir}/dyndnsupdate
%config(noreplace) %{_sysconfdir}/dyndns.hosts

%changelog
* Sat May 29 2004 Dries Verachtert <dries@ulyssis.org> - 0.8-1
- Initial package.
