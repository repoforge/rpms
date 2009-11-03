# $Id$
# Authority: dag
# Upstream: Bart Samwel <bart@samwel.tk>

Summary: Tools to spin down hard disks automatically for power savings
Name: laptop-mode-tools
Version: 1.33
Release: 1%{?dist}
License: GPL
Group: System Environment/Base
URL: http://www.samwel.tk/laptop_mode/

Source: http://samwel.tk/laptop_mode/tools/downloads/laptop-mode-tools_%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
Requires: acpid

%description
Laptop mode is a Linux kernel feature that allows your laptop to save
considerable power, by allowing the hard drive to spin down for longer
periods of time. This package contains the userland scripts that are
needed to enable laptop mode. It includes support for automatically
enabling laptop mode when the computer is working on batteries.

%prep
%setup

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 usr/sbin/laptop_mode %{buildroot}%{_sbindir}/laptop_mode
%{__install} -Dp -m0755 usr/sbin/lm-syslog-setup %{buildroot}%{_sbindir}/lm-syslog-setup
%{__install} -Dp -m0755 etc/init.d/laptop-mode %{buildroot}%{_initrddir}/laptop-mode
%{__install} -Dp -m0644 etc/laptop-mode/laptop-mode.conf %{buildroot}%{_sysconfdir}/laptop-mode/laptop-mode.conf

for script in etc/acpi/actions/lm_*.sh; do
	%{__install} -Dp -m0755 $script %{buildroot}%{_sysconfdir}/acpi/actions/$(basename $script)
done

for file in etc/acpi/events/lm_*; do
	%{__install} -Dp -m0644 $file %{buildroot}%{_sysconfdir}/acpi/events/$(basename $file)
done

for man in man/*.8; do
	%{__install} -Dp -m0644 $man %{buildroot}%{_mandir}/man8/$(basename $man)
done

%clean
%{__rm} -rf %{buildroot}

%preun
if [ $1 -eq 0 ]; then
	/sbin/service laptop-mode stop &>/dev/null || :
	/sbin/chkconfig --del laptop-mode
fi

%post
/sbin/chkconfig --add laptop-mode
/sbin/service laptop-mode start &>/dev/null || :

%postun
/sbin/service laptop-mode condrestart &>/dev/null || :

%files
%defattr(-, root, root, 0755)
%doc COPYING Documentation/*.txt README
%doc %{_mandir}/man8/*.8*
%config %{_sysconfdir}/acpi/actions/lm_*.sh
%config %{_sysconfdir}/acpi/events/lm_*
%config(noreplace) %{_sysconfdir}/laptop-mode/
%config %{_initrddir}/laptop-mode
%{_sbindir}/laptop_mode
%{_sbindir}/lm-syslog-setup

%changelog
* Sun Jun 10 2007 Dries Verachtert <dries@ulyssis.org> - 1.33-1
- Updated to release 1.33.

* Sun Oct 08 2006 Dag Wieers <dag@wieers.com> - 1.32-1
- Updated to release 1.32.

* Sun Apr 16 2006 Dag Wieers <dag@wieers.com> - 1.31-1
- Updated to release 1.31.

* Sat Apr 15 2006 Dag Wieers <dag@wieers.com> - 1.30-1
- Updated to release 1.30.

* Sun Apr 10 2005 Dag Wieers <dag@wieers.com> - 1.05-1
- Initial package. (using DAR)
