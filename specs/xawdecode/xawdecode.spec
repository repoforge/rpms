# $Id$
# Authority: dag
# Upstream: <xawdecode-project$lists,sf,net>

%{?dtag: %{expand: %%define %dtag 1}}

%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}

%{?el4:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}
%{?el2:%define _without_modxorg 1}
%{?fc4:%define _without_modxorg 1}
%{?fc3:%define _without_modxorg 1}
%{?fc2:%define _without_modxorg 1}
%{?fc1:%define _without_modxorg 1}

%define desktop_vendor rpmforge

Summary: Video4Linux stream capture viewer
Name: xawdecode
Version: 1.9.3
Release: 1.2%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://xawdecode.sourceforge.net/

Source: http://dl.sf.net/xawdecode/xawdecode-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: lirc
#BuildRequires: lirc-devel
%{?_without_modxorg:BuildRequires: XFree86-devel}
%{!?_without_modxorg:BuildRequires: libX11-devel}
BuildRequires: xosd-devel, Xaw3d-devel
BuildRequires: xvidcore-devel, divx4linux, lame-devel, ffmpeg-devel
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}

%description
xawdecode allows you to watch TV, record AVI and DIVX files.
It interacts with AleVT for Teletext and Nxtvepg for NextView signal.

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%{__cat} <<EOF >xawdecode.desktop
[Desktop Entry]
Name=Xawdecode Video Capture
Comment=A versatile video capturing tool
Exec=xawdecode
Icon=xawdecode.png
Terminal=false
Type=Application
Categories=AudioVideo;Application;
EOF

%build
%configure \
	--x-libraries="%{_prefix}/X11R6/%{_lib}" \
	--disable-dependency-tracking \
	--disable-alsa \
	--enable-xosd
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}

### FIXME: /etc is not created by make install. (Please fix upstream)
%{__install} -d -m0755 %{buildroot}%{_sysconfdir}

%makeinstall \
	ROOT="%{buildroot}"

%{__install} -Dp -m0644 xawdecode.1 %{buildroot}%{_mandir}/man1/xawdecode.1
%{__install} -Dp -m0644 xawdecode_cmd.1 %{buildroot}%{_mandir}/man1/xawdecode_cmd.1
%{__install} -Dp -m0644 xawdecode-48.png %{buildroot}%{_datadir}/pixmaps/xawdecode.png

%if %{?_without_freedesktop:1}0
	%{__install} -Dp -m0644 xawdecode.desktop %{buildroot}%{_datadir}/gnome/apps/Multimedia/xawdecode.desktop
%else
	%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
	desktop-file-install --vendor %{desktop_vendor}    \
		--add-category X-Red-Hat-Base              \
		--dir %{buildroot}%{_datadir}/applications \
		xawdecode.desktop
%endif

%post
xset fp rehash || :

%postun
xset fp rehash || :

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING FAQfr-xawdecode libavc-rate-control.txt NEWS TODO
%doc *.sample lisez-moi README*
%doc %{_mandir}/man?/*
%config(noreplace) %{_sysconfdir}/*.conf
%{_bindir}/*
%{_datadir}/xawdecode/
%{_prefix}/X11R6/lib/X11/app-defaults/*
%{_prefix}/X11R6/%{_lib}/X11/fonts/misc/*
%{_datadir}/pixmaps/*.png
%{!?_without_freedesktop:%{_datadir}/applications/%{desktop_vendor}-xawdecode.desktop}
%{?_without_freedesktop:%{_datadir}/gnome/apps/Multimedia/xawdecode.desktop}

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/xawdecode/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.9.3-1.2
- Rebuild for Fedora Core 5.

* Wed Sep 22 2004 Dag Wieers <dag@wieers.com> - 1.9.3-1
- Updated to release 1.9.3.

* Mon Jun 21 2004 Dag Wieers <dag@wieers.com> - 1.9.2-1
- Updated to release 1.9.2.

* Thu Apr 15 2004 Dag Wieers <dag@wieers.com> - 1.9.1-1
- Updated to release 1.9.1.

* Mon Feb 09 2004 Dag Wieers <dag@wieers.com> - 1.9.0-0
- Updated to release 1.9.0.

* Fri Nov 28 2003 Dag Wieers <dag@wieers.com> - 1.8.2-0
- Updated to release 1.8.2.

* Sun Oct 05 2003 Dag Wieers <dag@wieers.com> - 1.8.1-0
- Updated to release 1.8.1.

* Sun Sep 14 2003 Dag Wieers <dag@wieers.com> - 1.8.0-0
- Updated to release 1.8.0.

* Sat Jul 12 2003 Dag Wieers <dag@wieers.com> - 1.7.0-0
- Updated to release 1.7.0.

* Mon Apr 07 2003 Dag Wieers <dag@wieers.com> - 1.6.7-0
- Updated to release 1.6.7.

* Wed Feb 19 2003 Dag Wieers <dag@wieers.com> - 1.6.6a-1
- Build against new lame-3.93.1-1 and ffmpeg-0.4.6-1 package.

* Sun Jan 19 2003 Dag Wieers <dag@wieers.com> - 1.6.6a-0
- Initial package. (using DAR)
