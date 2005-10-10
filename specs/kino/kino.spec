# $Id$
# Authority: dag
# Upstream: Dan Dennedy <ddennedy$users,sf,net>

#define cvs 20040802

Summary: Simple non-linear video editor
Name: kino
Version: 0.7.6
Release: 1%{?cvs:.%{cvs}}
License: GPL
Group: Applications/Multimedia
URL: http://kino.schirmacher.de/
Source: http://dl.sf.net/kino/kino-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: libdv-devel >= 0.102, libavc1394-devel, libraw1394-devel
BuildRequires: libogg-devel, libvorbis-devel, a52dec-devel
BuildRequires: XFree86-devel, libgnomeui-devel >= 2.0, gettext
BuildRequires: libxml2-devel, libsamplerate-devel
# libtool *sigh*
BuildRequires: gcc-c++
%{!?_without_quicktime:BuildRequires: libquicktime-devel}
%{!?_without_ffmpeg:BuildRequires: ffmpeg-devel}
%if %{?cvs:1}0
BuildRequires: automake, autoconf, libtool
%endif

Obsoletes: kino-devel <= %{version}

%description
The new generation of digital camcorders use the Digital Video (DV) data
format. Kino allows you to record, create, edit, and play movies recorded
with DV camcorders. Unlike other editors, this program uses many keyboard
commands for fast navigating and editing inside the movie.

%prep
%setup


%build
%{?cvs:./autogen.sh}
%configure \
    --with-hotplug-script-dir=%{_sysconfdir}/hotplug/usb \
    --with-hotplug-usermap-dir=%{_libdir}/hotplug/kino \
    %{!?_without_quicktime:--with-quicktime} \
    %{!?_without_ffmpeg:--with-avcodec}
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall \
    hotplugscriptdir=%{buildroot}%{_sysconfdir}/hotplug/usb \
    hotplugusermapdir=%{buildroot}%{_libdir}/hotplug/kino
%find_lang %{name}


%post
update-mime-database %{_datadir}/mime &>/dev/null || :

%postun
update-mime-database %{_datadir}/mime &>/dev/null || :


%clean
%{__rm} -rf %{buildroot}


%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS BUGS ChangeLog COPYING NEWS README*
%config %{_sysconfdir}/hotplug/usb/*
%{_bindir}/*
%{_includedir}/kino/
%{_libdir}/hotplug/kino/
%{_datadir}/applications/Kino.desktop
%{_datadir}/kino/
%{_datadir}/mime/packages/kino.xml
%{_datadir}/pixmaps/kino.png
%{_mandir}/man1/*


%changelog
* Mon Jun  6 2005 Matthias Saou <http://freshrpms.net> 0.7.6-1
- Update to 0.7.6.
- Add update-mime-database calls.

* Fri Apr 29 2005 Matthias Saou <http://freshrpms.net> 0.7.5-1
- Disable ffmpeg on FC4 for now.

* Mon Nov 22 2004 Matthias Saou <http://freshrpms.net> 0.7.5-1
- Update to 0.7.5.

* Tue Oct 05 2004 Dag Wieers <dag@wieers.com> - 0.7.4-1
- Update to 0.7.4.

* Mon Aug 16 2004 Matthias Saou <http://freshrpms.net> 0.7.3-1
- Update to 0.7.3.

* Mon Aug  2 2004 Matthias Saou <http://freshrpms.net> 0.7.2-1.20040802
- Update to today's CVS tree to fix various bugs.

* Tue Jul 27 2004 Matthias Saou <http://freshrpms.net> 0.7.2-1
- Update to 0.7.2.
- Spec file changes to match upstream build fixes.

* Tue Jul 20 2004 Dag Wieers <dag@wieers.com> - 0.7.1-3
- Rebuild for x86_64 with quicktime support.

* Mon Jun 14 2004 Matthias Saou <http://freshrpms.net> 0.7.1-2
- Updated the desktop entry creation to the new current method.
- Fixed build requirements.
- Added custom icon for the menu entry (taken from the logo).

* Sun Apr 11 2004 Dag Wieers <dag@wieers.com> - 0.7.1-1
- Updated to release 0.7.1.

* Sun Mar 07 2004 Dag Wieers <dag@wieers.com> - 0.7.0-1
- Obsolete older kino-devel package. (Jeff Moe)

* Fri Dec 19 2003 Dag Wieers <dag@wieers.com> - 0.7.0-0
- Updated to 0.7.0.

* Wed Dec 03 2003 Dag Wieers <dag@wieers.com> - 0.6.5-0
- Updated to 0.6.5.

* Mon Feb 24 2003 Dag Wieers <dag@wieers.com> - 0.6.4-0
- Updated to 0.6.4.

* Wed Feb 12 2003 Dag Wieers <dag@wieers.com> - 0.6.3-0
- Initial package. (using DAR)
