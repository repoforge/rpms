# $Id$
# Authority: dag
# Upstream: Snax <snax$shmoo,com>

%{?dtag: %{expand: %%define %dtag 1}}

%{!?dtag:%define _with_libpcapdevel 1}
%{?el5:%define _with_libpcapdevel 1}
%{?fc6:%define _with_libpcapdevel 1}

%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}
%{?rh6:%define _without_freedesktop 1}

%define desktop_vendor rpmforge

%define real_version 0.2.7e

Summary: Wireless LAN (WLAN) tool which recovers encryption keys
Name: airsnort
Version: 0.2.7
Release: 0.e.2%{?dist}
License: GPL
Group: System Environment/Base
URL: http://airsnort.shmoo.com/

Source: http://dl.sf.net/airsnort/airsnort-%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtk+-devel, libgnomeui-devel >= 2.0.0
BuildRequires: autoconf, automake, libpcap
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}
%{?_with_libpcapdevel:BuildRequires:libpcap-devel}

%description
AirSnort is a wireless LAN (WLAN) tool which recovers encryption keys.
AirSnort operates by passively monitoring transmissions, computing the
encryption key when enough packets have been gathered.

%prep
%setup -n %{name}-%{real_version}

%{__cat} <<EOF >airsnort.desktop
[Desktop Entry]
Name=Airsnort Wireless Sniffer
Comment=Recover wireless encryption keys.
Icon=redhat-internet.png
Exec=airsnort
Terminal=false
Type=Application
Categories=GNOME;Application;Network;
EOF

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%if %{?_without_freedesktop:1}0
        %{__install} -Dp -m0644 airsnort.desktop %{buildroot}%{_datadir}/gnome/apps/Network/airsnort.desktop
%else
        %{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
        desktop-file-install --vendor %{desktop_vendor}    \
                --add-category X-Red-Hat-Base              \
                --dir %{buildroot}%{_datadir}/applications \
                airsnort.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc *.txt AUTHORS ChangeLog COPYING INSTALL NEWS README* TODO
%doc %{_mandir}/man1/airsnort.1*
%doc %{_mandir}/man1/decrypt.1*
%doc %{_mandir}/man1/gencases.1*
%{_bindir}/airsnort
%{_bindir}/decrypt
%{_bindir}/gencases
%{_bindir}/orinoco_hopper
%{?_without_freedesktop:%{_datadir}/gnome/apps/Network/airsnort.desktop}
%{!?_without_freedesktop:%{_datadir}/applications/%{desktop_vendor}-airsnort.desktop}

%changelog
* Fri Feb 11 2005 Dag Wieers <dag@wieers.com> - 0.2.7-0.e
- Updated to release 0.2.7e.

* Fri Dec 24 2004 Dag Wieers <dag@wieers.com> - 0.2.7-0.b
- Updated to release 0.2.7b.

* Thu Apr 15 2004 Dag Wieers <dag@wieers.com> - 0.2.4-0.a
- Updated to release 0.2.4a.

* Sat Jan 03 2004 Dag Wieers <dag@wieers.com> - 0.2.3-0.c
- Added desktop-file.
- Updated to release 0.2.3c.

* Sat Jul 12 2003 Dag Wieers <dag@wieers.com> - 0.2.2-0
- Initial package. (using DAR)
