# $Id$

%define desktop_vendor freshrpms
#define cvs -cvs

Summary: A DVD player that supports DVD menus
Name: ogle
Version: 0.9.2
Release: 1.fr
License: GPL
Group: Applications/Multimedia
Source0: http://www.dtek.chalmers.se/groups/dvd/dist/%{name}-%{version}%{?cvs}.tar.gz
Source1: bluecurve-xine.png
URL: http://www.dtek.chalmers.se/groups/dvd/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: libdvdread >= 0.9.4, libjpeg, libxml2 >= 2.4.19
%{!?_without_alsa:Requires: alsa-lib}
BuildRequires: XFree86-devel
BuildRequires: libdvdread-devel >= 0.9.4, libjpeg-devel, a52dec-devel >= 0.7.3
BuildRequires: libxml2-devel >= 2.4.19, libmad-devel, perl
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}
%{!?_without_alsa:BuildRequires: alsa-lib-devel}

%description
Ogle is a DVD player. It's features are: Supports DVD menus and navigation,
reads encrypted and unencrypted DVDs using libdvdread/libdvdcss, normal X11
and XFree86 Xvideo display support with subpicture overlay, audio and
subpicture selection, advanced subpicture commands such as fade/scroll and
wipe, detects and uses correct aspect for movie and menus, playing AC3 via
S/PDIF with an external command, fullscreen mode, screenshots with and
without subpicture overlay...

Available rpmbuild rebuild options :
--with : alsadefaultdriver
--without : alsa freedesktop altivec


%package devel
Summary: Header files and static libraries from the Ogle DVD player
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: libdvdread-devel >= 0.9.4, libxml2-devel >= 2.4.19

%description devel
These are the header files and static libraries from Ogle that are needed
to build programs that use it (like GUIs).


%prep
%setup -q -n %{name}-%{version}%{?cvs}

%build
%configure %{?_without_altivec:--disable-altivec}
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
# Needed for library dependencies
export LIBRARY_PATH=%{buildroot}/usr/lib/ogle
make DESTDIR=%{buildroot} install
install -m 644 -D %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/%{name}.png

# Change the ALSA default to OSS, unless "alsa-default" was chosen
%{!?_with_alsadefaultdriver:perl -pi -e 's|<driver>alsa</driver>|<driver>oss</driver>|g' %{buildroot}%{_datadir}/ogle/oglerc}

cat << EOF > %{name}.desktop
[Desktop Entry]
Name=Ogle DVD Player
Comment=Play all DVDs including encrypted ones with full menu support
Icon=%{name}.png
Exec=%{_bindir}/%{name}
Terminal=false
Type=Application
EOF

%if %{!?_without_freedesktop:1}%{?_without_freedesktop:0}
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install --vendor %{desktop_vendor} \
  --dir %{buildroot}%{_datadir}/applications    \
  --add-category X-Red-Hat-Base                 \
  --add-category Application                    \
  --add-category AudioVideo                     \
  %{name}.desktop
%else
install -D -m644 %{name}.desktop \
  %{buildroot}/etc/X11/applnk/Multimedia/%{name}.desktop
%endif


%clean
rm -rf %{buildroot}

%post
/sbin/ldconfig
# If the /dev/dvd link doesn't exist, create a default one
test -e /dev/dvd || test -L /dev/dvd || ln -s cdrom /dev/dvd || :

%postun -p /sbin/ldconfig

%files
%defattr(-, root, root)
%doc AUTHORS COPYING README
%{_bindir}/*
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*.so.*
%{_libdir}/%{name}/%{name}_*
%{_mandir}/man?/*
%{!?_without_freedesktop:%{_datadir}/applications/*%{name}.desktop}
%dir %{_datadir}/%{name}
%config %{_datadir}/%{name}/oglerc
%{_datadir}/%{name}/ogle_conf.dtd
%{_datadir}/pixmaps/%{name}.png
%{?_without_freedesktop:/etc/X11/applnk/Multimedia/%{name}.desktop}

%files devel
%defattr(-, root, root)
%{_includedir}/%{name}
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*.so
%exclude %{_libdir}/%{name}/*.la
%{_libdir}/%{name}/*.a

%changelog
* Thu Nov  6 2003 Matthias Saou <http://freshrpms.net/> 0.9.2-1.fr
- Update to 0.9.2.

* Sun Nov  2 2003 Matthias Saou <http://freshrpms.net/> 0.9.1-7.fr
- Rebuild for Fedora Core 1.

* Fri Sep 19 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to today's CVS snapshot that will become 0.9.2.
- Change build dep from libmad to libmad-devel.

* Wed May 14 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Added --without altivec build option for ppc < G4 users.

* Mon Apr 14 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Added libdvdread and libxml devel deps.

* Mon Mar 31 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Rebuilt for Red Hat Linux 9.
- Exclude .la file.

* Sat Mar 15 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Add freedesktop build option.

* Tue Mar 11 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 0.9.1.

* Tue Feb 25 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 0.9.0.

* Sun Feb 16 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to CVS version, "release imminent" :-)

* Fri Oct  4 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Moved the /dev/dvd link creation to the %%post script.
- Enabled ALSA by default in the build, but OSS as default in the config
  unless rebuilt with --with alsadefaultdriver.

* Fri Sep 27 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Rebuilt for Red Hat Linux 8.0.
- Added the new desktop entry to this main ogle package, it makes more sense.
- Shameless ripoff of the cool BlueCurve Xine icon for the menu entry.
- Added default /dev/dvd -> cdrom symlink.

* Fri Aug 30 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Now build with support for ALSA by default.
- Updated description and URLs.

* Tue Aug  6 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 0.8.5.

* Mon Jul  1 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 0.8.4.

* Wed Jun 12 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 0.8.3.
- Spec file cleanup and inclusion of the Ogle team changes (Björn & Martin).

* Wed May 15 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Rebuilt for Red Hat Linux 7.3 (added a workaround for libxml2).
- Added the %%{?_smp_mflags} expansion.

* Tue Mar 19 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 0.8.2 current CVS version.

* Sat Dec  8 2001 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 0.8.2.

* Sun Nov  4 2001 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Added an ugly hack to prevent the need to build the package twice to
  have it work done correctly.

* Wed Oct 31 2001 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Spec file cleanup and fixes.

* Fri Oct 26 2001 Martin Norbäck <d95mback@dtek.chalmers.se>
- Updated version to 0.8.1
* Thu Oct 11 2001 Martin Norbäck <d95mback@dtek.chalmers.se>
- Updated version to 0.8.0
* Thu Sep 20 2001 Martin Norbäck <d95mback@dtek.chalmers.se>
- Added missing .la files
* Thu Sep 20 2001 Martin Norbäck <d95mback@dtek.chalmers.se>
- Updated version to 0.7.5
- Split into normal and devel package
* Thu Sep 6 2001 Martin Norbäck <d95mback@dtek.chalmers.se>
- Updated version to 0.7.4
* Fri Aug 10 2001 Martin Norbäck <d95mback@dtek.chalmers.se>
- Updated version to 0.7.2
* Sun Jul 22 2001 Martin Norbäck <d95mback@dtek.chalmers.se>
- initial version
