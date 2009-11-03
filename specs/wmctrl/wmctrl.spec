# $Id$
# Authority: dag

%{?dtag: %{expand: %%define %dtag 1}}

%{?el4:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}

Summary: Command line tool to interact with an X Window Manager
Name: wmctrl
Version: 1.07
Release: 1%{?dist}
License: GPL
Group: User Interface/X
URL: http://sweb.cz/tripie/utils/wmctrl

Source: http://sweb.cz/tripie/utils/wmctrl/dist/wmctrl-%{version}.tar.gz
Patch: http://ftp.de.debian.org/debian/pool/main/w/wmctrl/wmctrl_1.07-6.diff.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: glib2-devel
%{!?_without_modxorg:BuildRequires: libXmu-devel, xorg-x11-proto-devel}
%{?_without_modxorg:BuildRequires: XFree86-devel}

%description
The wmctrl program is a UNIX/Linux command line tool to interact with an·
EWMH/NetWM compatible X Window Manager. The tool provides command line access·
to almost all the features defined in the EWMH specification. It can be used,·
for example, to obtain information about the window manager, to get a detailed·
list of desktops and managed windows, to switch and resize desktops, to make·
windows full-screen, always-above or sticky, and to activate, close, move,·
resize, maximize and minimize them. The command line access to these window·
management functions makes it easy to automate and execute them from any·
application that is able to run a command in response to an event.·

%prep
%setup
%patch0 -p1

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
%doc AUTHORS ChangeLog COPYING INSTALL README
%doc %{_mandir}/man1/wmctrl.1*
%{_bindir}/wmctrl

%changelog
* Thu Sep 10 2009 Dag Wieers <dag@wieers.com> - 1.07-1
- Initial package. (using DAR)
