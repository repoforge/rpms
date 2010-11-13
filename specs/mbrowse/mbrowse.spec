# $Id$
# Authority: dag
# Upstream: Aaron Hodgen <ahodgen$munsterman,com>

# Screenshot: http://www.kill-9.org/mbrowse/screenshot/tree.png
# ScreenshotURL: http://www.kill-9.org/mbrowse/#Screenshots


%{?rh7:%define _without_freedesktop 1}
%{?rh7:%define _without_net_snmp 1}
%{?el2:%define _without_freedesktop 1}
%{?el2:%define _without_net_snmp 1}
%{?rh6:%define _without_freedesktop 1}
%{?rh6:%define _without_net_snmp 1}

%define desktop_vendor rpmforge

Summary: GUI SNMP MIB browser
Name: mbrowse
Version: 0.3.1
Release: 2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://www.kill-9.org/mbrowse/

Source: http://www.kill-9.org/mbrowse/mbrowse-%{version}.tar.gz
Patch0: gcc.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtk+-devel >= 1.2
%{!?_without_net_snmp:BuildRequires: net-snmp-devel >= 4.2}
%{?_without_net_snmp:BuildRequires: ucd-snmp-devel}
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}

%description
Mbrowse is an SNMP MIB browser based on GTK and net-snmp.

%prep
%setup
%patch0 -p1

%{__cat} <<EOF >mbrowse.desktop
[Desktop Entry]
Name=SNMP MIB Viewer
Comment=View your SNMP MIB files
Icon=gnome-internet.png
Exec=mbrowse
Terminal=false
Type=Application
Encoding=UTF-8
Categories=Application;Internet;
EOF

%build
%configure \
	--with-snmp-lib="%{_libdir}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%if %{?_without_freedesktop:1}0
	%{__install} -Dp -m0644 mbrowse.desktop %{buildroot}%{_datadir}/gnome/apps/Internet/mbrowse.desktop
%else
	%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
	desktop-file-install --vendor %{desktop_vendor}    \
		--add-category X-Red-Hat-Base              \
		--dir %{buildroot}%{_datadir}/applications \
		mbrowse.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_bindir}/*
%{?_without_freedesktop:%{_datadir}/gnome/apps/Internet/mbrowse.desktop}
%{!?_without_freedesktop:%{_datadir}/applications/rpmforge-mbrowse.desktop}

%changelog
* Mon May 29 2006 Dries Verachtert <dries@ulyssis.org> - 0.3.1-2
- Fixes for gcc 4.1 by Thomas C. Knoeller.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.3.1-0.2
- Rebuild for Fedora Core 5.

* Mon Mar 10 2003 Dag Wieers <dag@wieers.com> - 0.3.1-0
- Initial package. (using DAR)
