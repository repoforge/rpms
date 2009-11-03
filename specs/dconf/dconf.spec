# $Id$
# Authority: dag
# Upstream: Dag Wieers <dag@wieers.com>

Summary: Collect a system's hardware and software configuration
Name: dconf
Version: 0.5.1
Release: 1%{?dist}
License: GPL
Group: System Environment/Base
URL: http://dag.wieers.com/home-made/dconf/

Source: http://dag.wieers.com/home-made/dconf/dconf-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python, asciidoc, xmlto
Requires: python

%description
Dconf is a tool to collect a system's hardware and software configuration.
It allows to take your system configuration with you on the road, compare
identical systems (like nodes in a cluster) to troubleshoot HW or SW
problems.

Dconf is also useful in projects where you have to manage changes as a
team. Dconf can send out system changes to a list of email addresses so
that they can be revised and discussed in group.

You can customize your dconf configuration for specific needs, like making
a profile of your laptop's hardware or copy specific software configuration
files to send out or compare with other systems.

%prep
%setup

%build

%install
%{__rm} -rf %{buildroot}
%{__make} install install-redhat DESTDIR="%{buildroot}"

%postun
if [ $1 -eq 0 ]; then
        %{__rm} -f /etc/cron.*/dconf
fi

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING README THANKS TODO config/ scripts/
%doc %{_mandir}/man1/dconf.1*
%config %{_sysconfdir}/dconf.conf
%config(noreplace) %{_sysconfdir}/dconf-custom.conf
%{_bindir}/dconf
%{_localstatedir}/log/dconf/

%changelog
* Sun Jul 30 2006 Dag Wieers <dag@wieers.com> - 0.5.1-1
- Updated to release 0.5.1.

* Fri Sep 09 2005 Dag Wieers <dag@wieers.com> - 0.5.0-1
- Remove cron entry on removal. (David M. Dowdle)
- Updated to release 0.5.0.

* Wed Jul 13 2005 Dag Wieers <dag@wieers.com> - 0.4.2-1
- Updated to release 0.4.2.

* Wed Nov 24 2004 Dag Wieers <dag@wieers.com> - 0.4.1-1
- Updated to release 0.4.1.

* Sun Nov 21 2004 Dag Wieers <dag@wieers.com> - 0.4-1
- Updated to release 0.4.

* Sun Oct 24 2004 Dag Wieers <dag@wieers.com> - 0.3-1
- Updated to release 0.3.
