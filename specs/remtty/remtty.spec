# $Id: remtty.spec $
# Authority: dag
# Upstream: <oliver@net-track.ch>

Summary: Remote tty
Name: remtty
Version: 0.2
Release: 1%{?dist}
License: GPL
Group: System Environment/Base
URL: http://www.net-track.ch/opensource/remtty/

Source: http://www.net-track.ch/php/d.php?f=/opensource/remtty/remtty-%{version}.tar.gz
#currently disabled
#Obsoletes: retty = 0.1
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
remtty (short for "remote tty") makes TCP connections available as pseudo
ttys. It allows you to use access servers with direct access to the
modems (such as Cisco NAS) as ordinary dial-out modems for faxing, sending
sms or visiting BBS'. It offers functionality similar to Cisco's Dialout
Utility, but on GNU/Linux instead of Windows.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README* remtty.conf
%config(noreplace) %{_sysconfdir}/remtty.conf
%doc %{_mandir}/man1/remtty.1*
%{_bindir}/remtty

%changelog
* Tue May 22 2007 Stefan Radman <stefan.radman@ctbto.org> - 0.2-1
- package renamed by upstream to resolve name conflict (thanks Oliver)

* Mon Jul 11 2005 Dag Wieers <dag@wieers.com> - 0.1-1
- Initial package. (using DAR)
