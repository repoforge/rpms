# $Id$
# Authority: matthias

%{?fedora: %{expand: %%define fc%{fedora} 1}}

%{?el4:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}

%define desktop_vendor rpmforge

Summary: GNU/Linux Audio MEchanics, the GIMP of audio processing
Name: glame
Version: 2.0.1
Release: 3%{?dist}
License: GPL
Group: Applications/Multimedia
Source0: http://dl.sf.net/glame/glame-%{version}.tar.gz
Source1: glame.png
URL: http://glame.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires(post): info
Requires(preun): info
BuildRequires: gcc-c++, libgnomeui-devel, guile-devel
BuildRequires: libgnomecanvas-devel, gtk2-devel >= 2.6.0
BuildRequires: fftw-devel, audiofile-devel, esound-devel
BuildRequires: lame-devel, libmad-devel, libvorbis-devel, ladspa-devel
%{!?_without_alsa:BuildRequires: alsa-lib-devel}
BuildRequires: desktop-file-utils
%{!?_without_modxorg:BuildRequires: xorg-x11-xbitmaps}

%description
GLAME is meant to be the GIMP of audio processing. It is designed to be
a powerful, fast, stable, and easily extensible sound editor for Linux
and compatible systems.


%package devel
Summary: Development libraries from the GNU/Linux Audio MEchanics
Group: Development/Libraries
Requires(post): info
Requires(preun): info
Requires: %{name} = %{version}

%description devel
GLAME is meant to be the GIMP of audio processing. It is designed to be
a powerful, fast, stable, and easily extensible sound editor for Linux
and compatible systems.

These are the development libraries provided by GLAME. You will also
need to install the main lame package in order to install these
libraries.


%prep
%setup


%build
%configure
%{__make}
# %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

# Modify desktop file if needed and install pixmap
%if 0%{!?_without_freedesktop:1}
%{__mkdir_p} %{buildroot}%{_datadir}/applications
desktop-file-install \
    --vendor %{desktop_vendor} \
    --dir %{buildroot}%{_datadir}/applications \
    --add-category "AudioVideo" \
    --delete-original \
    %{buildroot}%{_datadir}/gnome/apps/Multimedia/glame.desktop
%endif
%{__install} -Dp -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/glame.png


%clean
%{__rm} -rf %{buildroot}


%post
/sbin/install-info %{_infodir}/glame.info.gz %{_infodir}/dir
update-desktop-database %{_datadir}/applications &>/dev/null || :

%preun
if [ $1 -eq 0 ]; then
    /sbin/install-info --delete %{_infodir}/glame.info.gz %{_infodir}/dir
fi

%postun
update-desktop-database %{_datadir}/applications &>/dev/null || :


%post devel
/sbin/install-info %{_infodir}/glame-dev.info.gz %{_infodir}/dir

%preun devel
if [ $1 -eq 0 ]; then
    /sbin/install-info --delete %{_infodir}/glame-dev.info.gz %{_infodir}/dir
fi


%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS BUGS COPYING CREDITS ChangeLog NEWS README TODO
%{_bindir}/*
%dir %{_libdir}/glame/
%{_libdir}/glame/*.so*
%{_datadir}/glame/
%{_datadir}/pixmaps/glame.png
%{_infodir}/glame.info*
%if 0%{!?_without_freedesktop:1}
%{_datadir}/applications/%{desktop_vendor}-glame.desktop
%else
%{_datadir}/gnome/apps/Multimedia/glame.desktop
%endif

%files devel
%defattr(-, root, root, 0755)
%dir %{_libdir}/glame/
%{_libdir}/glame/*.a
%exclude %{_libdir}/glame/*.la
%{_infodir}/glame-dev.info*


%changelog
* Thu Jun 15 2006 Matthias Saou <http://freshrpms.net/> 2.0.1-3
- Remove old leftover libglade-devel build requirement.

* Fri Mar 17 2006 Matthias Saou <http://freshrpms.net/> 2.0.1-3
- Release bump to drop the disttag number in FC5 build.

* Thu Jan 12 2006 Matthias Saou <http://freshrpms.net/> 2.0.1-2
- Add modular xorg build conditional.

* Tue Mar 29 2005 Matthias Saou <http://freshrpms.net/> 2.0.1-1
- Update to 2.0.1.
- Requires gtk2 >= 2.6.0, which will only be relased when FC4 is.

* Tue Jan 11 2005 Matthias Saou <http://freshrpms.net/> 2.0.0-1
- Update to 2.0.0.
- Added lame support. Interestingly, build fails when it's not enabled.
- Now convert the desktop file by default.

* Fri Oct 29 2004 Matthias Saou <http://freshrpms.net/> 1.0.3-1
- Update to 1.0.3.
- Added install-info calls.
- Added fftw, libmad, libvorbis and ladspa support.

* Wed Apr 23 2003 Matthias Saou <http://freshrpms.net/>
- Update to 1.0.0.

* Tue Jan 29 2002 Matthias Saou <http://freshrpms.net/>
- Updated to 0.6.1.

* Sun Dec 30 2001 Matthias Saou <http://freshrpms.net/>
- Updated to 0.6.0.

* Mon Dec 10 2001 Matthias Saou <http://freshrpms.net/>
- Updated to 0.5.4.
- Added the locale files.

* Thu Nov  8 2001 Matthias Saou <http://freshrpms.net/>
- Updated to 0.5.3.
- No more files in %{_libdir} directly.

* Tue Jul 17 2001 Matthias Saou <http://freshrpms.net/>
- Updated to 0.5.2.

* Mon May  7 2001 Matthias Saou <http://freshrpms.net/>
- Spec file cleanup.
- Split with a -devel package.
- Put the desktop entry in the %files (why wasn't it there?).

* Thu May 03 2001 Daniel Kobras <kobras@linux.de> 0.4.1-1
- Merge with Mandrake's spec file for GLAME 0.4.0.
- Compile with low-latency enabled.
- Don't use mp3lame support in packages.

