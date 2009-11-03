# $Id$
# Authority: dries


Summary: Scan the firewire IEEE-1394 bus
Name: gscanbus
Version: 0.7.1
Release: 1.2%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://gscanbus.berlios.de/

Source: http://download.berlios.de/gscanbus/gscanbus-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libraw1394-devel, gtk+-devel, desktop-file-utils
%{?fc4:BuildRequires: compat-gcc-32}

%description
Gscanbus is a little tool for testing and visualising the firewire IEEE-1394
bus. Using the Linux ieee1394 subsystem, it displays a graphical tree of all
connected firewire devices and allows basic control of camcorders and other
devices. It is designed as development and debugging tool and can be used
for testing the basic firewire setup of a Linux machine.

%prep
%setup

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=gscanbus
Comment=Scan the firewire bus
Exec=gscanbus
Terminal=false
Type=Application
StartupNotify=true
Categories=Application;AudioVideo;
EOF

%build
%{?fc4:export CC=gcc32}
%{expand: %%define optflags -O2}
%configure --disable-gtktest
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d %{buildroot}%{_sysconfdir}
%{__perl} -pi -e "s| /etc/| %{buildroot}%{_sysconfdir}/|g;" Makefile
%makeinstall

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor rpmforge             \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	%{name}.desktop

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%{_bindir}/gscanbus
%config(noreplace) %{_sysconfdir}/guid-resolv.conf
%config(noreplace) %{_sysconfdir}/oui-resolv.conf
%{_datadir}/applications/*-gscanbus.desktop

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.7.1-1.2
- Rebuild for Fedora Core 5.

* Fri Aug 26 2005 Dries Verachtert <dries@ulyssis.org> - 0.7.1-1
- Initial package.
