# $Id$

# Authority: dag
# Upstream: Markus Braun <markus.braun@krawel.de>

Summary: Utility to enable the IBM ThinkPad(tm) special keys
Name: tpb
Version: 0.6.1
Release: 0
License: GPL
Group: Applications/System
URL: http://www.nongnu.org/tpb/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://savannah.nongnu.org/download/tpb/%{name}-%{version}.tar.gz
#Source1: tpbrc
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: gettext, XFree86-devel, xosd-devel >= 2.0

%description
This program enables the IBM Thinkpad(tm) special keys. It is possible to bind
a program to the ThinkPad button. It has a on-screen display (OSD) to show
volume, mute and brightness of the LCD.

%prep
%setup

%{__cat} <<EOF >tpb.xinit
#!/bin/sh
%{_bindir}/tpb -d
EOF

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}
%{__install} -d -m0755 %{buildroot}%{_sysconfdir}/X11/xinit/xinitrc.d \
			%{buildroot}/dev
#%{__install} -m0755 %{SOURCE1} %{buildroot}%{_sysconfdir}
%{__install} -m0755 doc/tpbrc %{buildroot}%{_sysconfdir}
%{__install} -m0755 tpb.xinit %{buildroot}%{_sysconfdir}/X11/xinit/xinitrc.d/tpb

touch %{buildroot}/dev/nvram

%post
if [ -e /dev/.devfsd ]; then
	if [ -x /usr/sbin/update-devfsd ]; then
		/usr/sbin/update-devfsd
	fi
else
	if [ ! -e /dev/nvram ]; then
		/dev/MAKEDEV nvram
		chmod 0644 /dev/nvram
	fi
fi

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING CREDITS README TODO doc/callback_example.sh doc/nvram.txt doc/tpbrc
%doc %{_mandir}/man?/*
%config(noreplace) %{_sysconfdir}/tpbrc
%config(noreplace) %{_sysconfdir}/X11/xinit/xinitrc.d/*
%{_bindir}/*
%ghost /dev/nvram

%changelog
* Tue Jan 20 2004 Dag Wieers <dag@wieers.com> - 0.6.1-0
- Updated to release 0.6.1.

* Sun Nov 23 2003 Dag Wieers <dag@wieers.com> - 0.6.0-1
- Don't replace config-files.

* Tue Aug 12 2003 Dag Wieers <dag@wieers.com> - 0.6.0-0
- Updated to release 0.6.0.

* Thu Apr 10 2003 Dag Wieers <dag@wieers.com> - 0.5.1-0
- Updated to release 0.5.1.

* Sun Apr 06 2003 Dag Wieers <dag@wieers.com> - 0.5.0-0
- Updated to release 0.5.0.

* Tue Mar 11 2003 Dag Wieers <dag@wieers.com> - 0.4.2-0
- Initial package. (using DAR)
- Included tpb.xinit. (Tim Verhoeven)
