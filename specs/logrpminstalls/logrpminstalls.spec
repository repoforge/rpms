# $Id: $

# Upstream: Dries Verachtert <dries@ulyssis.org>
# Authority: dries

Summary: Creates a log with timestamps of every install of an rpm
Name: logrpminstalls
Version: 1.0
Release: 1
License: GPL
Group: Applications/System
URL: http://dries.ulyssis.org/projects/logrpminstalls/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

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
%{__rm} -rf ${RPM_BUILD_ROOT}
%makeinstall

%files
%defattr(-, root, root, 0755)
%doc README
%{_sysconfdir}/cron.daily/logrpminstalls

%changelog
* Fri Mar 19 2004 Dries Verachtert <dries@ulyssis.org> 1.0-1
- first packaging for Fedora Core 1
