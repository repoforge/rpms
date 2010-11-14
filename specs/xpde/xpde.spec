# $Id$
# Authority: dag
# Upstream: <development$xpde,com>

# Tag: rft

%define installdir /opt/xkde
%define real_version 0.4.0-20030730

Summary: Integrated desktop environment (xpde) and window manager (xpwm)
Name: xpde
Version: 0.4.0
Release: 1.2%{?dist}
License: GPL
Group: User Interface/Desktops
URL: http://www.xpde.com/

NoSource: 0
Source: http://www.xpde.com/releases/xpde-%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
XPde is a desktop window Enviroment and a window manager thinking
to make easy to use people who begin in Linux with a familiar look
desktop. It tries to recreate the Window Xp interface nothing more.

%prep
%setup

%{__cat} <<EOF >xpde.session
#!/bin/sh
exec %{_sysconfdir}/X11/xdm/Xsession XPde
EOF

%{__cat} <<EOF >xpde.xclients
#!/bin/sh
exec %{installdir}/.xinitrcXPDE
EOF

%{__cat} <<'EOF' >xpde.xinitrc
#!/bin/sh

if [ -d $HOME/.xpde ]; then
	exec $HOME/.xinitrc
else
	cp -a %{installdir}/defaultdesktop $HOME/.xpde
	cp -v %{installdir}/xinitrcDEFAULT $HOME/.xinitrc
	chmod a+x $HOME/.xinitrc
	exec $HOME/.xinitrc
fi
EOF

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 xpde.session %{buildroot}%{_sysconfdir}/X11/gdm/Sessions/xpde
%{__install} -Dp -m0755 xpde.xclients %{buildroot}%{_datadir}/apps/switchdesk/Xclients.xpde

%{__install} -Dp -m0755 xpde.xinitrc %{buildroot}%{installdir}/.xinitrcXPDE
%{__install} -Dp -m0755 xinitrcDEFAULT %{buildroot}%{installdir}/xinitrcDEFAULT

%{__install} -d -m0755 %{buildroot}%{installdir}/themes/default/
%{__cp} -apv themes/default/* %{buildroot}%{installdir}/themes/default/

%{__install} -d -m0755 %{buildroot}%{installdir}/defaultdesktop/
%{__cp} -apv defaultdesktop/* %{buildroot}%{installdir}/defaultdesktop/

%{__install} -Dp -m0755 XPde %{buildroot}%{installdir}/bin/XPde
%{__install} -Dp -m0755 XPwm %{buildroot}%{installdir}/bin/XPwm
%{__install} -Dp -m0755 stub.sh %{buildroot}%{installdir}/bin/stub.sh
%{__install} -p -m0755 *.so* %{buildroot}%{installdir}/bin/

%{__install} -Dp -m0755 calculator %{buildroot}%{installdir}/bin/apps/calculator
%{__install} -Dp -m0755 fileexplorer %{buildroot}%{installdir}/bin/apps/fileexplorer
%{__install} -Dp -m0755 notepad %{buildroot}%{installdir}/bin/apps/notepad
%{__install} -Dp -m0755 taskmanager %{buildroot}%{installdir}/bin/apps/taskmanager

%{__install} -Dp -m0755 appexec %{buildroot}%{installdir}/bin/applets/appexec
%{__install} -Dp -m0755 DateTimeProps %{buildroot}%{installdir}/bin/applets/DateTimeProps
%{__install} -Dp -m0755 desk %{buildroot}%{installdir}/bin/applets/desk
%{__install} -Dp -m0755 keyboard %{buildroot}%{installdir}/bin/applets/keyboard
%{__install} -Dp -m0755 mouse %{buildroot}%{installdir}/bin/applets/mouse
%{__install} -Dp -m0755 networkproperties %{buildroot}%{installdir}/bin/applets/networkproperties
%{__install} -Dp -m0755 networkstatus %{buildroot}%{installdir}/bin/applets/networkstatus
%{__install} -Dp -m0755 regional %{buildroot}%{installdir}/bin/applets/regional
%{__install} -Dp -m0755 xpsu %{buildroot}%{installdir}/bin/applets/xpsu

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING doc/* gpl.txt INSTALL
%config %{_sysconfdir}/X11/gdm/Sessions/*
%{_datadir}/apps/switchdesk/*
%{installdir}

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.4.0-1.2
- Rebuild for Fedora Core 5.

* Mon Apr 05 2004 Dag Wieers <dag@wieers.com> - 0.4.0-1
- Small cosmetic changes.
- Updated to release 0.4.0.

* Thu Aug 03 2003 Ricardo Arroyo <ricarro@terra.com.pe> - 0.3.5-1
- Initial package.
