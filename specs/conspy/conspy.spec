# $Id$
# Authority: dag
# Upstream: Russell Stuart <russell-conspy$stuart,id,au>

Summary: Remote control for text mode virtual consoles
Name: conspy
Version: 1.3
Release: 1
License: GPL
Group: Applications/System
URL: http://ace-host.stuart.id.au/russell/files/conspy/

Source: http://ace-host.stuart.id.au/russell/files/conspy/conspy-%{version}.tar.bz2
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
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README conspy.html
%doc %{_mandir}/man1/conspy.1*
%{_bindir}/conspy

%changelog
* Wed Jan 11 2006 Dag Wieers <dag@wieers.com> - 1.3-1
- Initial package. (using DAR)
