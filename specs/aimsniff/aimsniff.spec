# $Id$
# Authority: dag
# Upstream: Shawn Grimes <shawn$aimsniff,com>
# Upstream: <aimsniff-devel$lists,sourceforge,net>

%define real_version 0.9d

Summary: Monitor and archive AOL Instant Messenger messages
Name: aimsniff
Version: 0.9
Release: 0.d.2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://www.aimsniff.com/

Source: http://www.aimsniff.com/releases/aimsniff-%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
AIM Sniff is a utility for monitoring and archiving AOL Instant Messenger
messages across a network. Aim Sniff can either do a live dump (actively
sniff the network) or read a PCAP file and parse the file for IM messages.
Aim Sniff also has the option of dumping the information to a MySQL
database or STDOUT.

%prep
%setup -n %{name}-%{real_version}

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 aimSniff.pl %{buildroot}%{_bindir}/aimsniff
%{__install} -Dp -m0644 aimsniff.config %{buildroot}%{_sysconfdir}/aimsniff.config
%{__install} -Dp -m0644 rc.aimsniff %{buildroot}%{_initrddir}/aimsniff

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog README table.struct
%config(noreplace) %{_sysconfdir}/aimsniff.config
%config %{_initrddir}/aimsniff
%{_bindir}/aimsniff

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.9-0.d.2
- Rebuild for Fedora Core 5.

* Fri Apr 09 2004 Dag Wieers <dag@wieers.com> - 0.9-0.d
- Initial package. (using DAR)
