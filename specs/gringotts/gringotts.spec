# $Id$
# Authority: dag
# Upstream: Germano Rizzo <mano$pluto,linux,it>

%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}
%{?rh6:%define _without_freedesktop 1}

Summary: Electronic strongbox
Name: gringotts
Version: 1.2.9
Release: 1%{?dist}
License: GPL
Group: Applications/Productivity
URL: http://devel.pluto.linux.it/projects/Gringotts/

Source: http://download.berlios.de/gringotts/gringotts-%{version}.tar.gz
Patch: gringotts-1.2.8-gtk24.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtk2-devel >= 2.12, popt, textutils, libgringotts-devel >= 1.1.1, pkgconfig
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}
BuildRequires: libmcrypt-devel, gettext

%description
Gringotts is a small but (hopely ;) useful utility that stores sensitive
data (passwords, credit card numbers, friends' addresses) in an organized,
optimized and most of all very secure form.
It uses libGringotts to provide a strong level of encryption, just aiming
to be as trustworthy as possible.

%prep
%setup
%patch0

### FIXME: Include improved desktop-file. (Please fix upstream)
%{__cat} <<EOF >gringotts.desktop.in
[Desktop Entry]
Name=Gringotts Data Protection
Comment=Store sensitive data securely
Icon=gringotts.xpm
Exec=gringotts
Terminal=false
Type=Application
StartupNotify=true
Encoding=UTF-8
Categories=GNOME;Application;Utility;
EOF

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%if %{!?_without_freedesktop:1}0
    %{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
    desktop-file-install --vendor gnome --delete-original \
        --add-category X-Red-Hat-Base                 \
        --dir %{buildroot}%{_datadir}/applications    \
        %{buildroot}%{_datadir}/gnome/apps/Utilities/gringotts.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS BUGS ChangeLog FAQ NEWS README TODO
%{_datadir}/pixmaps/gringotts.xpm
%{!?_without_freedesktop:%{_datadir}/applications/gnome-gringotts.desktop}
%{?_without_freedesktop:%{_datadir}/gnome/apps/Utilities/gringotts.desktop}

%defattr(4755, root, root, 0755)
%{_bindir}/gringotts

%changelog
* Mon Jan 28 2008 Dag Wieers <dag@wieers.com> - 1.2.9-1
- Updated to release 1.2.9.

* Wed Jun 29 2004 Dag Wieers <dag@wieers.com> - 1.2.8-1
- Fix for gtk 2.4. (Rok Mandeljc)

* Sun Jun 06 2004 Dag Wieers <dag@wieers.com> - 1.2.8-1
- Add improved desktop file.

* Thu Oct 23 2003 Dag Wieers <dag@wieers.com> - 1.2.8-0
- Updated to release 1.2.8.

* Tue Apr 29 2003 Dag Wieers <dag@wieers.com> - 1.2.7-0
- Updated to release 1.2.7.

* Thu Apr 18 2003 Dag Wieers <dag@wieers.com> - 1.2.6-0
- Updated to release 1.2.6.

* Tue Jan 07 2003 Dag Wieers <dag@wieers.com> - 1.2.3-0
- Initial package. (using DAR)
