# $Id$
# Authority: dag

Summary: Rsync Backup Made Easy
Name: rbme
Version: 1.6
Release: 1%{?dist}
License: GPL
Group: Applications/Archiving
URL: http://www.schapiro.org/schlomo/projects/rbme.php

Source: http://www.schapiro.org/schlomo/projects/rbme/rbme-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: openssh-clients
Requires: openssh-clients
Requires: procmail
Requires: rsync

%description
Rsync Backup Made Easy (RBME) is a rsync-based backup solution with integrated
backup disk space management to remove old backups when the disk gets full.

Creates nice reports to serve as daily backup overview.

%prep
%setup

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 rbme %{buildroot}%{_bindir}/rbme
%{__install} -Dp -m0644 rbme.conf %{buildroot}%{_sysconfdir}/rbme.conf

%files
%defattr(-, root, root, 0755)
%doc LICENSE NEWS README
%config(noreplace) %{_sysconfdir}/rbme.conf
%{_bindir}/rbme

%changelog
* Thu Jun 03 2010 Dag Wieers <dag@wieers.com> - 1.6-1
- Initial package. (using DAR)
