# $Id$
# Authority: matthias

Summary: DVD ripping and encoding graphical user interface
Name: ogmrip
Version: 0.10.3
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://ogmrip.sourceforge.net/
Source: http://dl.sf.net/ogmrip/ogmrip-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: mplayer, mencoder
BuildRequires: gtk2-devel, libglade2-devel, GConf2-devel, libxml2-devel
Buildrequires: hal-devel, dbus-glib-devel, enchant-devel
Buildrequires: libdvdread-devel, libtheora-devel, libvorbis-devel, gocr-devel
Buildrequires: gettext-devel, intltool, gcc-c++
# Not technically build required, but configure checks for it...
Buildrequires: mplayer, mencoder, ogmtools, vorbis-tools, theora-tools
BuildRequires: mkvtoolnix, lame
# Now, all the same as runtime requirements
Requires: mplayer, mencoder, ogmtools, vorbis-tools, theora-tools
Requires: mkvtoolnix, lame
# We should normally provide the built srttool program, but it conflicts
Requires: subtitleripper
Requires(post): GConf2
Requires(postun): GConf2

%description
OGMRip is an application and a set of libraries for ripping and encoding DVDs
into AVI, OGM MP4 or Matroska files using a wide variety of codecs. It relies
on mplayer, mencoder, ogmtools, mkvtoolnix, oggenc, lame and faac to perform
its tasks.


%package devel
Summary: Development files for ogmrip
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
Development headers and libraries for ogmrip.


%prep
%setup
# Remove -Werror since build fails because of warn_unused_result otherwise
%{__perl} -pi -e 's|-Wall -Werror|-Wall|g' configure*


%build
%configure \
    --disable-static \
    --disable-schemas-install
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall
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
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog README TODO
%{_sysconfdir}/gconf/schemas/ogmrip.schemas
%{_bindir}/dvdcpy
%{_bindir}/ogmrip
%{_bindir}/srtutil
%{_bindir}/subp2pgm
%{_bindir}/theoraenc
%{_libdir}/*.so.*
%{_datadir}/applications/ogmrip.desktop
%{_datadir}/ogmrip/
%{_datadir}/pixmaps/ogmrip.png

%files devel
%defattr(-,root,root,-)
%{_includedir}/*
%exclude %{_libdir}/*.la
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so


%changelog
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

