# $Id$

# Authority: dag

### FIXME: Makefiles don't allow -jX (parallel compilation) (Please fix upstream)
# Distcc: 0

%define dfi %(which desktop-file-install &>/dev/null; echo $?)

Summary: Video4Linux stream capture viewer.
Name: xawdecode
Version: 1.9.0
Release: 0
License: GPL
Group: Applications/Multimedia
URL: http://xawdecode.sf.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/xawdecode/xawdecode-%{version}.tar.bz2
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: XFree86-devel, lirc-devel, xosd-devel
BuildRequires: xvidcore-devel, divx4linux, lame-devel, ffmpeg-devel

%description
xawdecode allows you to watch TV, record AVI and DIVX files.
It interacts with AleVT for Teletext and Nxtvepg for NextView signal.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%{__cat} <<EOF >%{name}.desktop
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

%{__install} -d -m0755 %{buildroot}%{_mandir}/man1/ \
			%{buildroot}%{_datadir}/pixmaps/
%{__install} -m0644 xawdecode.1 xawdecode_cmd.1 %{buildroot}%{_mandir}/man1/
%{__install} -m0644 xawdecode-48.png %{buildroot}%{_datadir}/pixmaps/xawdecode.png

%if %{dfi}
        %{__install} -d -m0755 %{buildroot}%{_datadir}/gnome/apps/Multimedia/
        %{__install} -m0644 %{name}.desktop %{buildroot}%{_datadir}/gnome/apps/Multimedia/
%else
        %{__install} -d -m0755 %{buildroot}%{_datadir}/applications
        desktop-file-install --vendor net                  \
                --add-category X-Red-Hat-Base              \
                --dir %{buildroot}%{_datadir}/applications \
                %{name}.desktop
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
%{_prefix}/X11R6/lib/X11/fonts/misc/*
%{_datadir}/pixmaps/*.png
%if %{dfi}
        %{_datadir}/gnome/apps/Multimedia/*.desktop
%else
        %{_datadir}/applications/*.desktop
%endif

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/xawdecode/

%changelog
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
