# $Id: $

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
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING CREDITS INSTALL LICENSE NEWS README THANKS TODO
%{_bindir}/dyndnsupdate
%config(noreplace) %{_sysconfdir}/dyndns.hosts

%changelog
* Sat May 29 2004 Dries Verachtert <dries@ulyssis.org> - 0.8-1
- Initial package.

