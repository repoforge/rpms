# $Id$
# Authority: matthias

Summary: DVD ripping and encoding graphical user interface
Name: ogmrip
Version: 0.13.4
Release: 1%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://ogmrip.sourceforge.net/

Source: http://dl.sf.net/ogmrip/ogmrip-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: dbus-glib-devel
BuildRequires: enchant-devel
BuildRequires: gcc-c++
BuildRequires: GConf2-devel
Buildrequires: gettext-devel
BuildRequires: glib2-devel >= 2.14
BuildRequires: gocr-devel
BuildRequires: gtk2-devel >= 2.14
Buildrequires: hal-devel
BuildRequires: intltool
Buildrequires: libdvdread-devel
BuildRequires: libglade2-devel
BuildRequires: libtheora-devel
BuildRequires: libvorbis-devel
BuildRequires: libxml2-devel
### Not technically build required, but configure checks for it...
BuildRequires: lame
BuildRequires: mencoder
BuildRequires: mkvtoolnix
BuildRequires: mplayer
BuildRequires: ogmtools
BuildRequires: theora-tools
BuildRequires: vorbis-tools
### Now, all the same as runtime requirements
Requires: lame
Requires: mencoder
Requires: mkvtoolnix
Requires: mplayer
Requires: ogmtools
Requires: theora-tools
Requires: vorbis-tools
### We should normally provide the built srttool program, but it conflicts
Requires: mencoder
Requires: mplayer
Requires: subtitleripper
Requires: GConf2

%description
OGMRip is an application and a set of libraries for ripping and encoding DVDs
into AVI, OGM MP4 or Matroska files using a wide variety of codecs. It relies
on mplayer, mencoder, ogmtools, mkvtoolnix, oggenc, lame and faac to perform
its tasks.

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

### Remove -Werror since build fails because of warn_unused_result otherwise
%{__perl} -pi -e 's|-Wall -Werror|-Wall|g' configure*

%build
%configure \
    --disable-schemas-install \
    --disable-static
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%post
/sbin/ldconfig
export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
gconftool-2 --makefile-install-rule \
    %{_sysconfdir}/gconf/schemas/ogmrip.schemas &>/dev/null || :

%preun
if [ "$1" -eq 0 ]; then
    export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
    gconftool-2 --makefile-uninstall-rule \
        %{_sysconfdir}/gconf/schemas/ogmrip.schemas &>/dev/null || :
fi

%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING ChangeLog README TODO
%doc %{_mandir}/man1/dvdcpy.1*
%doc %{_mandir}/man1/srtutil.1*
%doc %{_mandir}/man1/subp2pgm.1*
%doc %{_datadir}/gtk-doc/html/ogmdvd/
%doc %{_datadir}/gtk-doc/html/ogmdvd-gtk/
%doc %{_datadir}/gtk-doc/html/ogmjob/
%doc %{_datadir}/gtk-doc/html/ogmrip/
%doc %{_datadir}/gtk-doc/html/ogmrip-gtk/
%{_sysconfdir}/gconf/schemas/ogmrip.schemas
%{_bindir}/dvdcpy
%{_bindir}/ogmrip
%{_bindir}/srtutil
%{_bindir}/subp2pgm
%{_bindir}/theoraenc
%{_datadir}/applications/ogmrip.desktop
%{_datadir}/ogmrip/
%{_datadir}/pixmaps/ogmrip.png
%{_libdir}/libogm*.so.*
%{_libdir}/ogmrip/

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/ogmdvd/
%{_includedir}/ogmjob/
%{_includedir}/ogmrip/
%{_libdir}/libogm*.so
%{_libdir}/pkgconfig/ogm*.pc
%exclude %{_libdir}/libogm*.la

%changelog
* Mon Mar 22 2010 Dag Wieers <dag@wieers.com> - 0.13.4-1
- Updated to release 0.13.4.

* Sat Dec 26 2009 Dag Wieers <dag@wieers.com> - 0.13.3-1
- Updated to release 0.13.3.

* Thu Sep 24 2009 Dag Wieers <dag@wieers.com> - 0.13.1-1
- Updated to release 0.13.1.

* Fri Jul 17 2009 Dag Wieers <dag@wieers.com> - 0.13.0-1
- Updated to release 0.13.0.

* Tue Sep 30 2008 Dag Wieers <dag@wieers.com> - 0.11.2-1
- Updated to release 0.11.2.

* Tue Mar 13 2007 Matthias Saou <http://freshrpms.net/> 0.10.3-1
- Update to 0.10.3.
- Remove exclude for no longer included srttool binary.
- Include new srtutil binary.
- Remove empty NEWS file.
- Add missing ldconfig calls.

* Wed Feb 14 2007 Matthias Saou <http://freshrpms.net/> 0.10.2-1
- Update to 0.10.2.

* Mon Oct 23 2006 Matthias Saou <http://freshrpms.net/> 0.10.0-1
- Initial RPM release.

