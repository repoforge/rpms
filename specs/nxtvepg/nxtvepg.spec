# $Id$
# Authority: dag
# Upstream: <nxtvepg-users$lists,sf,net>

%define desktop_vendor rpmforge

%{?dtag: %{expand: %%define %dtag 1}}

%{?fc4:%define _without_modxorg 1}
%{?el4:%define _without_modxorg 1}
%{?fc3:%define _without_modxorg 1}
%{?fc2:%define _without_modxorg 1}
%{?fc1:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}

%{?rh9:%define _without_modxorg 1}
%{?rh9:%define _without_tcltk_devel 1}

%{?rh8:%define _without_tcltk_devel 1}

%{?rh7:%define _without_freedesktop 1}
%{?rh7:%define _without_modxorg 1}
%{?rh7:%define _without_tcltk_devel 1}

%{?el2:%define _without_freedesktop 1}
%{?el2:%define _without_modxorg 1}
%{?el2:%define _without_tcltk_devel 1}

Summary: NexTView EPG decoder and browser
Name: nxtvepg
Version: 2.8.0
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://nxtvepg.sourceforge.net/

Source: http://dl.sf.net/nxtvepg/nxtvepg-%{version}.tar.gz
Source1: nxtvepg.png
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%{!?_without_freedesktop:BuildRequires: desktop-file-utils}
%{!?_without_tcltk_devel:BuildRequires: tcl-devel >= 8.3, tk-devel}
%{?_without_tcltk_devel:BuildRequires: tcl >= 8.3, tk}
%{?_without_modxorg:BuildRequires: XFree86-devel}
%{!?_without_modxorg:BuildRequires: xorg-x11-proto-devel, libXmu-devel}

%description
nxtvepg is a decoder and browser for nexTView - an Electronic TV Programme
Guide for the analog domain (as opposed to the various digital EPGs that
come with most digital broadcasts). It allows you to decode and browse TV
programme listings for most of the major networks in Germany, Austria,
France and Switzerland.

%prep
%setup

%{__perl} -pi.orig -e '
        s|/usr/lib|%{_datadir}|g;
        s|/usr/tmp|%{_localstatedir}/tmp|g;
        s|\$\(mandir\)|\$(mandir)/man1|g;
        s|/lib\b|/%{_lib}|g;
    ' Makefile

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=Nextview TV Browser
Comment=Browse through TV Nextview information.
Icon=nxtvepg.png
Exec=nxtvepg
Terminal=false
Type=Application
Categories=Application;AudioVideo;
EOF

%build
%{__make} %{?_smp_mflags} \
    prefix="%{_prefix}" \
    CCFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall \
    resdir="%{buildroot}%{_prefix}/X11R6/%{_lib}/X11" \
    SYS_DBDIR="%{buildroot}%{_localstatedir}/tmp/nxtvdb"

%{__install} -Dp -m0644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/nxtvepg.png

%if %{?_without_freedesktop:1}0
    %{__install} -Dp -m0644 nxtvepg.desktop %{buildroot}%{_datadir}/gnome/apps/Utilities/nxtvepg.desktop
%else
    %{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
    desktop-file-install --vendor %{desktop_vendor}    \
        --add-category X-Red-Hat-Base              \
        --dir %{buildroot}%{_datadir}/applications \
        nxtvepg.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES COPYRIGHT README* TODO manual.html
%doc %{_mandir}/man1/nxtvepg.1*
%doc %{_mandir}/man1/nxtvepgd.1*
%{_bindir}/nxtvepg
%{_bindir}/nxtvepgd
%{_datadir}/applications/%{desktop_vendor}-nxtvepg.desktop
%{_datadir}/pixmaps/nxtvepg.png
%{_localstatedir}/tmp/nxtvdb/
%{_prefix}/X11R6/%{_lib}/X11/app-defaults/*

%changelog
* Tue Jan 08 2008 Dag Wieers <dag@wieers.com> - 2.8.0-1
- Updated to release 2.8.0.

* Mon Jan 22 2007 Dag Wieers <dag@wieers.com> - 2.7.7-1
- Updated to release 2.7.7.

* Sat Apr 04 2005 Dag Wieers <dag@wieers.com> - 2.7.5-1
- Updated to release 2.7.5.

* Sun Apr 04 2004 Dag Wieers <dag@wieers.com> - 2.7.0-1
- Updated to release 2.7.0.

* Tue Mar 09 2004 Dag Wieers <dag@wieers.com> - 2.6.0-1
- Initial package. (using DAR)
