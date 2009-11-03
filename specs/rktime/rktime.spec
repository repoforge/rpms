# $Id$
# Authority: dag
# Upstream: G. Richard Keech <rkeech$redhat,com>

Summary: Multi-zone time display utility
Name: rktime
Version: 0.6
Release: 1.2%{?dist}
License: GPL
Group: Applications/Productivity
URL: http://people.redhat.com/rkeech/

### Source is not available from homepage, only SRPM
Source: http://people.redhat.com/rkeech/rktime-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
Requires: sh-utils

%description
rktime is a command-line utility which displays the time
in multiple timezones in an easy-to-read way, using color
to help indicate which locations are currently in business
hours.

%prep
%setup

%{__cat} <<'EOF' >rktime.conf
### This is the configuration file for rktime
WEEKDAY_COLOR=$GREEN
AFTERHOURS_COLOR=$BLUE
WEEKEND_COLOR=$WHITE

ZONES="
        US/Pacific
        US/Eastern
        UTC
        Europe/London
        Europe/Brussels
        Asia/Calcutta
        Asia/Singapore
        Asia/Hong_Kong
        Asia/Tokyo
        Australia/Brisbane
"

TIMEOFFSET=on
COLOR=on
TIMEFORMAT=24h
EOF

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 rktime %{buildroot}%{_bindir}/rktime
%{__install} -Dp -m0644 rktime.conf %{buildroot}%{_sysconfdir}/rktime.conf
%{__install} -Dp -m0644 rktime.1 %{buildroot}%{_mandir}/man1/rktime.1
%{__install} -Dp -m0644 rktime.conf.5 %{buildroot}%{_mandir}/man5/rktime.conf.5

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc rktime.conf.sample
%doc %{_mandir}/man1/rktime.1*
%doc %{_mandir}/man5/rktime.conf.5*
%config(noreplace) %{_sysconfdir}/rktime.conf
%{_bindir}/rktime

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.6-1.2
- Rebuild for Fedora Core 5.

* Sun Nov 14 2004 Dag Wieers <dag@wieers.com> - 0.6-1
- Cosmetic changes to SPEC file.

* Sun May 09 2004 <rkeech@redhat.com>
- Added rktime.conf.sample.
- Misc cleanups to main script.

* Wed Oct 08 2003 <rkeech@redhat.com>
- Added Asia/Calcutta zone

* Tue Sep 17 2002 <rkeech@redhat.com>
- Added Europe/Paris zone

* Fri Apr 19 2002 <rkeech@redhat.com>
- spec file change only

* Fri Nov 17 2000 <rkeech@redhat.com>
- Corrected for RH7
