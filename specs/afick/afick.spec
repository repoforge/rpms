# $Id$
# Authority: dag
# Upstream: Eric Gerbier <gerbier$users,sourceforge,net>


%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}

%define desktop_vendor rpmforge

%define real_version %{version}-0

Summary: File integrity checker
Name: afick
Version: 2.2
Release: 2.2%{?dist}
License: GPL
Group: Applications/System
URL: http://afick.sourceforge.net/

Source: http://dl.sf.net/afick/afick-%{real_version}.tgz
#Source: afick.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}

%description
afick is a portable file integrity checker
(it only needs standard perl to work).
it will be run daily by cron to detect new/deleted/modified files
It works by first (init) making an image of strategic directories attributes,
and then compare the disk status with this image.
A Graphical interface is available in afick-gui package.

%package gui
Summary: Graphical frontend for afick
Group: Applications/System
Requires: %{name} >= %{version}-%{release}, perl-Tk

%description gui
afick-gui is perl/tk tool for afick software
It can be used to launch afick with differents options
and to have a graphical view of results
It comes with menu for integration in kde/gnome ...

%prep
%setup -n %{name}-%{real_version}

%{__cat} <<EOF >afick.desktop
[Desktop Entry]
Name=File Integrity Checker
Comment=Check the integrity of your files
Exec=afick-tk
Terminal=false
Type=Application
Icon=afick.png
Categories=GNOME;Application;System;
EOF

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 afick.pl %{buildroot}%{_bindir}/afick.pl
%{__install} -Dp -m0755 afick-tk.pl %{buildroot}%{_bindir}/afick-tk.pl
%{__install} -Dp -m0755 afick.cron %{buildroot}%{_sysconfdir}/cron.daily/afick

%{__install} -Dp -m0644 afick.conf %{buildroot}%{_sysconfdir}/afick.conf
%{__install} -Dp -m0644 afick.logrotate %{buildroot}%{_sysconfdir}/logrotate.d/afick

%{__install} -Dp -m0644 afick.1 %{buildroot}%{_mandir}/man1/afick.1
%{__install} -Dp -m0644 afick-tk.1 %{buildroot}%{_mandir}/man1/afick-tk.1
%{__install} -Dp -m0644 afick.conf.5 %{buildroot}%{_mandir}/man1/afick.conf.5

%{__install} -Dp -m0644 afick.png %{buildroot}%{_datadir}/pixmaps/afick.png

%{__install} -d -m0755 %{buildroot}%{_localstatedir}/lib/afick/archive/
%{__install} -d -m0755 %{buildroot}%{_localstatedir}/log/afick/

%{__ln_s} -f afick.pl %{buildroot}%{_bindir}/afick
%{__ln_s} -f afick-tk.pl %{buildroot}%{_bindir}/afick-tk

%if %{?_without_freedesktop:1}0
	%{__install} -Dp -m0644 afick.desktop %{buildroot}%{_datadir}/gnome/apps/System/afick.desktop
%else
        %{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
        desktop-file-install --vendor %{desktop_vendor}    \
		--delete-original                          \
                --add-category X-Red-Hat-Base              \
                --dir %{buildroot}%{_datadir}/applications \
		afick.desktop
%endif

%post
#if [ $1 -eq 1 ]; then
#	%{_bindir}/afick -i
#fi

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc *.html AUTHORS Changelog COPYING COPYRIGHT INSTALL linux.conf NEWS README TODO
%doc %{_mandir}/man?/afick.*
%config(noreplace) %{_sysconfdir}/afick.conf
%config(noreplace) %{_sysconfdir}/cron.daily/afick
%config(noreplace) %{_sysconfdir}/logrotate.d/afick
%{_bindir}/afick
%{_bindir}/afick.pl
%{_localstatedir}/lib/afick/
%{_localstatedir}/log/afick/

%files gui
%defattr(-, root, root, 0755)
%doc Changelog-gui
%doc %{_mandir}/man?/afick-tk.*
%{_bindir}/afick-tk
%{_bindir}/afick-tk.pl
%{_datadir}/pixmaps/afick.png
%{?_without_freedesktop:%{_datadir}/gnome/apps/System/afick.desktop}
%{!?_without_freedesktop:%{_datadir}/applications/%{desktop_vendor}-afick.desktop}

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 2.2-2.2
- Rebuild for Fedora Core 5.

* Tue Jun 15 2004 Dag Wieers <dag@wieers.com> - 2.2-2
- Fixed afick cron script. (Charles)
- Added improved desktop file.

* Wed May 12 2004 Dag Wieers <dag@wieers.com> - 2.2-1
- Updated to release 2.2.

* Sun Apr 11 2004 Dag Wieers <dag@wieers.com> - 2.1-1
- Initial package. (using DAR)
