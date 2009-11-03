# $Id$
# Authority: dag
# Upstream: Russell Stuart <russell-conspy$stuart,id,au>

Summary: Remote control for text mode virtual consoles
Name: conspy
Version: 1.5
Release: 1%{?dist}
License: Eclipse Public License v1.0
Group: Applications/System
URL: http://ace-host.stuart.id.au/russell/files/conspy/

Source: http://ace-host.stuart.id.au/russell/files/conspy/conspy-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: ncurses-devel

%description
Conspy allows a (possibly remote) user to see what is displayed on a
Linux virtual console, and to send keystrokes to it. It only known to
work with Linux. It is rather like VNC, but where VNC takes control of
a GUI, conspy takes control of a text-mode virtual console. Unlike
VNC, conspy does not require a server to be installed prior to being
used.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog INSTALL README *.html
%doc %{_mandir}/man1/conspy.1*
%{_bindir}/conspy

%changelog
* Mon Sep 24 2007 Dag Wieers <dag@wieers.com> - 1.5-1
- Updated to release 1.5.

* Wed Jan 25 2006 Dries Verachtert <dries@ulyssis.org> - 1.4-1
- Updated to release 1.4.

* Wed Jan 11 2006 Dag Wieers <dag@wieers.com> - 1.3-1
- Initial package. (using DAR)
