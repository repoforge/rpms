# $Id$
# Authority: matthias
# Upstream: <vlc-devel$videolan,org>

# Distcc: 0

%define real_name vlc
%define dfi %(which desktop-file-install &>/dev/null; echo $?)

Summary: The VideoLAN client, also a very good standalone DVD player
Name: videolan-client
Version: 0.5.3
Release: 2
Group: Applications/Multimedia
License: GPL
URL: http://www.videolan.org/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.videolan.org/pub/vlc/vlc-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: XFree86-devel, qt-devel, kdelibs-devel
BuildRequires: gtk+-devel, gnome-libs-devel, ncurses-devel
BuildRequires: libdvdread-devel, libdvdcss-devel, libdvdplay-devel
BuildRequires: libdvbpsi-devel, aalib-devel, speex-devel, libxvidcore-devel
BuildRequires: libmad-devel, a52dec-devel, libvorbis-devel, SDL-devel
BuildRequires: esound-devel, arts-devel, xosd-devel, faad2-devel
BuildRequires: openslp-devel, edb-devel
#BuildRequires: lirc-devel, libalsa-devel

Provides: %{real_name}
Obsoletes: %{real_name}

%description
The vlc is part of the VideoLAN project, a full MPEG2 client/server
solution. The VideoLAN Client can also be used as a standalone program
to play MPEG2 streams from a hard disk or a DVD.

%package devel
Summary: Headers for developing programs that will use %{name}
Group: Development/Libraries
Requires: %{name} = %{version}

%description devel
This package contains the static libraries and header files needed for
developing applications that use vlc.

%prep
%setup -n %{real_name}-%{version}

%build
source "%{_sysconfdir}/profile.d/qt.sh"
export X_EXTRA_LIBS="-L%{buildroot}%{_libdir}"
%configure \
	--program-prefix="%{?_program_prefix}" \
	--enable-release  \
	--enable-dvdread  \
	--enable-dvdplay  \
	--enable-v4l      \
	--enable-mad      \
	--enable-aa       \
	--enable-ffmpeg   \
	--with-ffmpeg="%{_prefix}" \
	--enable-xvid     \
	--enable-dv       \
	--enable-dsp      \
	--enable-esd      \
	--enable-faad     \
	--enable-arts     \
	--enable-familiar \
	--enable-gnome    \
	--enable-qt       \
	--enable-kde      \
	--enable-ncurses  \
	--enable-xosd     
#	--enable-mozilla
#	--enable-alsa
#	--enable-mga
#	--enable-lirc     \
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__strip} %{buildroot}%{_bindir}/vlc %{buildroot}%{_libdir}/vlc/*/*
%find_lang %{real_name}

%{__install} -d -m0755 %{buildroot}%{_mandir}/man1
%{__install} -m0644 doc/*.1 %{buildroot}%{_mandir}/man1

cat <<EOF >gnome-%{name}.desktop
[Desktop Entry]
Name=VideoLAN Client
Comment=An all-round MPEG, DivX and DVD-player.
Icon=%{_datadir}/vlc/vlc48x48.png
Exec=vlc
Terminal=false
Type=Application
EOF

%if %{dfi}
	%{__install} -d -m0755 %{buildroot}%{_datadir}/gnome/apps/Multimedia/
	%{__install} -m0644 gnome-%{name}.desktop %{buildroot}%{_datadir}/gnome/apps/Multimedia/
%else
	%{__install} -d -m0755 %{buildroot}%{_datadir}/applications
	desktop-file-install --vendor "gnome"              \
		--add-category X-Red-Hat-Base              \
		--add-category Application                 \
		--add-category AudioVideo                  \
		--dir %{buildroot}%{_datadir}/applications \
		gnome-%{name}.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files -f %{real_name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog NEWS README THANKS doc/*.txt doc/*.html
%doc %{_mandir}/man1/vlc.*
%{_bindir}/*vlc
%{_libdir}/vlc/
%{_datadir}/vlc/
%if %{dfi}
        %{_datadir}/gnome/apps/Multimedia/*.desktop
%else
        %{_datadir}/applications/*.desktop
%endif

%files devel
%defattr(-, root, root, 0755)
%doc %{_mandir}/man1/vlc-config.*
%{_bindir}/vlc-config
%{_libdir}/*.a
%{_includedir}/vlc/

%changelog
* Fri Apr 11 2003 Dag Wieers <dag@wieers.com> - 0.5.3-2
- Build against new edb package.
- Removed epoch.

* Tue Apr 10 2003 Dag Wieers <dag@wieers.com> - 0.5.3-1
- Build against new faad2 and openslp packages.

* Wed Apr 09 2003 Dag Wieers <dag@wieers.com> - 0.5.3-0
- Updated to release 0.5.3.

* Tue Apr 08 2003 Dag Wieers <dag@wieers.com> - 0.5.2-2
- Build against new (renamed) libxvidcore package.

* Wed Mar 12 2003 Dag Wieers <dag@wieers.com> - 0.5.2-0
- Updated to release 0.5.2.

* Fri Feb 21 2003 Dag Wieers <dag@wieers.com> - 0.5.1-3
- Build against aalib-1.3.95-0 package.
- Build against newer ffmpeg-0.4.6-2 package.
- Fixed the --program-prefix problem.

* Thu Feb 20 2003 Dag Wieers <dag@wieers.com> - 0.5.1-2
- Build against new xvidcore-0.9.1-0 package.

* Wed Feb 19 2003 Dag Wieers <dag@wieers.com> - 0.5.1-1
- Build against new xosd-2.1.1-0 package.

* Wed Feb 19 2003 Dag Wieers <dag@wieers.com> - 0.5.1-0
- Updated to release 0.5.1.
- Build against ffmpeg package.

* Mon Feb 17 2003 Dag Wieers <dag@wieers.com> - 0.5.0-4
- Rebuild against new libdvdread-0.9.4-0 package.

* Wed Feb 05 2003 Dag Wieers <dag@wieers.com> - 0.5.0-0
- Initial package. (using DAR)
