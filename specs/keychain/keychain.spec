# $Id$
# Authority: dag
# Upstream: Aron Griffis <agriffis$gentoo,org>

Summary: Agent manager for OpenSSH, ssh.com, Sun SSH, and GnuPG
Name: keychain
Version: 2.6.8
Release: 1
License: GPL
Group: Applications/Internet
URL: http://www.gentoo.org/proj/en/keychain/

Source: http://agriffis.n01se.net/keychain/keychain-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
Requires: bash sh-utils

%description
Keychain is a manager for OpenSSH, ssh.com, Sun SSH and GnuPG agents.
It acts as a front-end to the agents, allowing you to easily have one
long-running agent process per system, rather than per login session.
This dramatically reduces the number of times you need to enter your
passphrase from once per new login session to once every time your
local machine is rebooted.

%prep
%setup

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 keychain %{buildroot}%{_bindir}/keychain
%{__install} -Dp -m0644 keychain.1 %{buildroot}%{_mandir}/man1/keychain.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING keychain.pod README
%doc %{_mandir}/man1/keychain.1*
%{_bindir}/keychain

%changelog
* Sat Aug 29 2009 Dries Verachtert <dries@ulyssis.org> - 2.6.8-1
- Updated to release 2.6.8.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 2.5.1-1.2
- Rebuild for Fedora Core 5.

* Sat Feb 12 2005 Dag Wieers <dag@wieers.com> - 2.5.1-1
- Initial package. (using DAR)
