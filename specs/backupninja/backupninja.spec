# $Id$
# Authority: dfateyev

Name: backupninja
Version: 1.0.1
Release: 1%{?dist}
Summary: Backupninja  backup system

Group: Applications/System
License: GPL+
URL: https://labs.riseup.net/code/projects/backupninja
Source0: https://labs.riseup.net/code/attachments/download/275/backupninja-1.0.1.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

%description
Backupninja allows you to coordinate system backup by dropping a few simple configuration
files into /etc/backup.d/. Most programs you might use for making backups don't have
their own configuration file format. Backupninja provides a centralized way to configure
and schedule many different backup utilities. It allows for secure, remote, incremental
filesytem backup (via rdiff-backup), compressed incremental data, backup system and
hardware info, encrypted remote backups (via duplicity), safe backup of MySQL/PostgreSQL
databases, subversion or trac repositories, burn CD/DVDs or create ISOs, incremental rsync
with hardlinking.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_sbindir}/backupninja
%{_sbindir}/ninjahelper
%{_libdir}/backupninja/easydialog
%{_libdir}/backupninja/parseini
%{_libdir}/backupninja/tools
%{_libdir}/backupninja/vserver
%config(noreplace) %{_sysconfdir}/backupninja.conf
%{_sysconfdir}/cron.d/backupninja
%{_sysconfdir}/logrotate.d/backupninja
%{_datadir}/backupninja/*
%{_mandir}/man1/*.gz
%{_mandir}/man5/*.gz

%changelog
* Mon Oct 01 2012 Denis Fateyev <denis@fateyev.com> - 1.0.1-1
- Initial RPM build
