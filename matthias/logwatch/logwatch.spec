# Authority: dag

Summary: Analyzes and Reports on system logs
Name: logwatch
Version: 4.3.2
Release: 1
License: MIT
Group: Applications/System
URL: http://www.logwatch.org/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: ftp://ftp.kaybee.org/pub/linux/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildArch: noarch
Requires: perl, textutils, sh-utils, grep, mailx

%description
Logwatch is a customizable, pluggable log-monitoring system.  It will go
through your logs for a given period of time and make a report in the areas
that you wish with the detail that you wish.  Easy to use - works right out
of the package on many systems.

%prep
%setup

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_sysconfdir}/log.d/conf/logfiles \
			%{buildroot}%{_sysconfdir}/log.d/conf/services \
			%{buildroot}%{_sysconfdir}/log.d/scripts/services \
			%{buildroot}%{_sysconfdir}/log.d/scripts/shared \
			%{buildroot}%{_mandir}/man8 \
			%{buildroot}%{_sysconfdir}/cron.daily \
			%{buildroot}%{_sbindir}

%{__install} -m0755 scripts/logwatch.pl %{buildroot}%{_sysconfdir}/log.d/scripts/
%{__install} -m0755 scripts/services/* %{buildroot}%{_sysconfdir}/log.d/scripts/services/
%{__install} -m0755 scripts/shared/* %{buildroot}%{_sysconfdir}/log.d/scripts/shared/

for file in scripts/logfiles/* ; do
	if [ $(ls $file | wc -l) -ne 0 ] ; then
		%{__install} -d -m0755 %{buildroot}%{_sysconfdir}/log.d/$file
		%{__install} -m0755 $file/* %{buildroot}%{_sysconfdir}/log.d/$file
	fi
done

%{__install} -m0644 conf/logwatch.conf %{buildroot}%{_sysconfdir}/log.d/conf/
%{__install} -m0644 conf/logfiles/* %{buildroot}%{_sysconfdir}/log.d/conf/logfiles/
%{__install} -m0644 conf/services/* %{buildroot}%{_sysconfdir}/log.d/conf/services/
%{__install} -m0644 logwatch.8 %{buildroot}%{_mandir}/man8/

%{__ln_s} -f scripts/logwatch.pl %{buildroot}%{_sysconfdir}/log.d/logwatch
%{__ln_s} -f conf/logwatch.conf %{buildroot}%{_sysconfdir}/log.d/
%{__ln_s} -f ../log.d/scripts/logwatch.pl %{buildroot}%{_sysconfdir}/cron.daily/00-logwatch
%{__ln_s} -f ../..%{_sysconfdir}/log.d/scripts/logwatch.pl %{buildroot}%{_sbindir}/logwatch

#%{__rm} -f %{buildroot}%{_sysconfdir}/log.d/logwatch \
#   %{buildroot}%{_sysconfdir}/log.d/logwatch.conf \
#   %{buildroot}%{_sysconfdir}/cron.daily/logwatch \
#   %{buildroot}%{_sbindir}/logwatch

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc License project/CHANGES project/TODO
%doc README HOWTO-Make-Filter
%doc %{_mandir}/man8/*
%config %{_sysconfdir}/log.d/
%config %{_sysconfdir}/cron.daily/00-logwatch
%{_sbindir}/*

%changelog
* Thu Mar 27 2003 Dag Wieers <dag@wieers.com> - 4.3.2-0
- Initial package. (using DAR)
