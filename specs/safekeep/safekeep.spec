# $Id$
# Authority: dag

%define logmsg logger -t %{name}/rpm

Summary: Client/server backup system
Name: safekeep
Version: 1.0.5
Release: 2%{?dist}
License: GPL
Group: Applications/System
URL: http://safekeep.sourceforge.net/

Source: http://dl.sf.net/safekeep/safekeep-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: asciidoc > 6.0.3
BuildRequires: xmlto

%description
SafeKeep is a client/server backup system which enhances the
power of rdiff-backup with simple, centralized configuration.

%package common
Summary: Client/server backup system (common component)
Group: Applications/System
Requires: python >= 2.2
Requires: rdiff-backup

%description common
SafeKeep is a client/server backup system which enhances the
power of rdiff-backup with simple, centralized configuration.

This is the common component of SafeKeep. It is shared in 
between the client/server components.

%package client
Summary: Client/server backup system (client component)
Group: Applications/System
Requires: coreutils
Requires: openssh-server
Requires: safekeep-common = %{version}-%{release}
Requires: util-linux

%description client
SafeKeep is a client/server backup system which enhances the
power of rdiff-backup with simple, centralized configuration.

This is the client component of SafeKeep. It should be
installed on all hosts that need to be backed-up.

%package server
Summary: Client/server backup system (server component)
Group: Applications/System
Requires: %{_sbindir}/groupadd
Requires: %{_sbindir}/useradd
Requires: openssh, openssh-clients
Requires: safekeep-common = %{version}-%{release}

%description server
SafeKeep is a client/server backup system which enhances the
power of rdiff-backup with simple, centralized configuration.

This is the server component of SafeKeep. It should be
installed on the server on which the data will be backed-up to.

%prep
%setup

%build
%{__make} build

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0644 safekeep.conf %{buildroot}%{_sysconfdir}/safekeep/safekeep.conf
%{__install} -Dp -m0755 safekeep.cron %{buildroot}%{_sysconfdir}/cron.daily/safekeep
%{__install} -Dp -m0755 safekeep %{buildroot}%{_bindir}/safekeep
%{__install} -Dp -m0444 doc/safekeep.1 %{buildroot}%{_mandir}/man1/safekeep.1
%{__install} -Dp -m0444 doc/safekeep.backup.5 %{buildroot}%{_mandir}/man5/safekeep.backup.5
%{__install} -Dp -m0444 doc/safekeep.conf.5 %{buildroot}%{_mandir}/man5/safekeep.conf.5

%{__install} -d -m0755 %{buildroot}%{_sysconfdir}/safekeep/backup.d/
%{__install} -d -m0750 %{buildroot}%{_localstatedir}/lib/safekeep/
%{__install} -d -m0700 %{buildroot}%{_localstatedir}/lib/safekeep/.ssh/

%clean
%{__rm} -rf %{buildroot}

%pre server
%{_sbindir}/groupadd -f -r safekeep
if ! id safekeep &>/dev/null; then
    /usr/sbin/useradd -r -g safekeep -d %{_localstatedir}/lib/safekeep/ -s /sbin/nologin \
    -c "Used by safekeep to run and store backups." safekeep || \
        %logmsg "Unexpected error adding user \"nagios\". Aborting installation."
fi

%files common
%defattr(-, root, root, 0755)
%doc ANNOUNCE AUTHORS COPYING LICENSE README TODO
%doc %{_mandir}/man1/safekeep.1*
%{_bindir}/safekeep

%files client
%defattr(-, root, root, 0755)

%files server
%defattr(-, root, root, 0755)
%doc sample.backup
%doc %{_mandir}/man5/safekeep.backup.5*
%doc %{_mandir}/man5/safekeep.conf.5*
%config(noreplace) %{_sysconfdir}/safekeep/safekeep.conf
%config %{_sysconfdir}/cron.daily/safekeep
%config %{_sysconfdir}/safekeep/

%defattr(0750, safekeep, safekeep, 0750)
%dir %{_localstatedir}/lib/safekeep/

%defattr(0700, safekeep, safekeep, 0700)
%dir %{_localstatedir}/lib/safekeep/.ssh/

%changelog
* Wed Dec 17 2008 Dag Wieers <dag@wieers.com> - 1.0.5-2
- Fixed syntax error in %%pre script. (Eduard Malinschi)

* Wed Oct 08 2008 Dag Wieers <dag@wieers.com> - 1.0.5-1
- Updated to release 1.0.5.

* Wed Nov 07 2007 Dag Wieers <dag@wieers.com> - 1.0.3-1
- Initial package. (using DAR)
