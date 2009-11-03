# $Id$
# Authority: dag


%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}
%{?rh6:%define _without_freedesktop 1}

%define desktop_vendor rpmforge

Summary: Small and fast GUI web browser
Name: dillo
Version: 2.0
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://www.dillo.org/

Source: http://www.dillo.org/download/dillo-%{version}.tar.bz2
Source1: dillo48.png
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtk+-devel, zlib-devel, libjpeg-devel, fltk-devel, gcc-c++
BuildRequires: fltk-devel
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}
Provides: webclient

%description
Dillo is a very small and fast web browser using GTK.

%prep
%setup

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=Dillo Web Browser
Comment=Browse the Internet
Exec=dillo
Icon=dillo.png
Terminal=false
Type=Application
Encoding=UTF-8
Categories=Network;Application;
MimeType=text/html;
EOF

%build
%configure \
    --enable-cookies \
    --enable-ipv6
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%{__install} -Dp %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/dillo.png

### Remove buildroot from config files
%{__perl} -pi -e 's|%{buildroot}||g' %{buildroot}%{_sysconfdir}/*

%if %{?_without_freedesktop:1}0
        %{__install} -Dp -m0644 dillo.desktop %{buildroot}%{_datadir}/gnome/apps/Internet/dillo.desktop
%else
    %{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
    desktop-file-install --vendor %{desktop_vendor}    \
        --add-category X-Red-Hat-Base              \
        --dir %{buildroot}%{_datadir}/applications \
        dillo.desktop
%endif

%post
update-desktop-database %{_datadir}/applications &>/dev/null || :

%postun
update-desktop-database %{_datadir}/applications &>/dev/null || :

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING doc/ NEWS README
%config(noreplace) %{_sysconfdir}/*
%{_bindir}/*
%{_libdir}/dillo/
%{_datadir}/pixmaps/dillo.png
%{?_without_freedesktop:%{_datadir}/gnome/apps/Internet/dillo.desktop}
%{!?_without_freedesktop:%{_datadir}/applications/%{desktop_vendor}-dillo.desktop}

%changelog
* Fri May 05 2006 Dag Wieers <dag@wieers.com> - 0.8.6-1
- Updated to release 0.8.6.

* Mon Jul 11 2005 Dag Wieers <dag@wieers.com> - 0.8.5-1
- Updated to release 0.8.5.

* Wed Jan 12 2005 Dag Wieers <dag@wieers.com> - 0.8.4-1
- Updated to release 0.8.4.

* Mon Nov 01 2004 Dag Wieers <dag@wieers.com> - 0.8.3-1
- Updated to release 0.8.3.

* Sat Jul 10 2004 Dag Wieers <dag@wieers.com> - 0.8.2-1
- Updated to release 0.8.2.

* Mon May 17 2004 Dag Wieers <dag@wieers.com> - 0.8.1-1
- Updated to release 0.8.1.

* Wed Feb 11 2004 Dag Wieers <dag@wieers.com> - 0.8.0-1
- Remove %%{buildroot} occurances in configuration files. (Andre Costa)

* Tue Feb 10 2004 Dag Wieers <dag@wieers.com> - 0.8.0-0
- Updated to release 0.8.0.

* Sun Sep 14 2003 Dag Wieers <dag@wieers.com> - 0.7.3-0
- Initial package. (using DAR)
