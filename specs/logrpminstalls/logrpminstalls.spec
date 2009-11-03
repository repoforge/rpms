# $Id$
# Authority: dries
# Upstream: Dries Verachtert <dries$ulyssis,org>

Summary: Creates a log with timestamps of every install of an rpm
Name: logrpminstalls
Version: 1.0
Release: 1.2%{?dist}
License: GPL
Group: Applications/System
URL: http://dries.ulyssis.org/projects/logrpminstalls/

Source: http://dries.ulyssis.org/projects/logrpminstalls/logrpminstalls-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Requires: rpm, perl, crontabs

%description
This script makes a log file /var/log/rpminstalls which contains timestamps
of every rpm which get installed. It's executed by cron every day. The
logfile contains lines like:
timestamp name-version-release

%prep
%setup

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%config %{_sysconfdir}/cron.daily/logrpminstalls

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.0-1.2
- Rebuild for Fedora Core 5.

* Fri Mar 19 2004 Dries Verachtert <dries@ulyssis.org> 1.0-1
- first packaging for Fedora Core 1
