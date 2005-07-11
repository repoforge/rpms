# $Id$
# Authority: dag
# Upstream: <oliver@net-track.ch>

Summary: Remote tty
Name: retty
Version: 0.1
Release: 1
License: GPL
Group: System Environment/Base
URL: http://www.net-track.ch/opensource/retty/

Source: http://www.net-track.ch/php/d.php?f=/opensource/retty/retty-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
retty (short for "remote tty") makes TCP connections available as pseudo
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
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README* retty.conf
%{_sysconfdir}/retty.conf
%doc %{_mandir}/man1/retty.1*
%{_bindir}/retty

%changelog
* Mon Jul 11 2005 Dag Wieers <dag@wieers.com> - 0.1-1
- Initial package. (using DAR)
