# $Id$
# Authority: dag

%{?dtag: %{expand: %%define %dtag 1}}

%{?el4:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}

Summary: Lightweight, purely OSD based xine frontend
Name: oxine
Version: 0.6
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://oxine.sourceforge.net/

Source: http://dl.sf.net/oxine/oxine-%{version}.tar.gz
Patch0: oxine-0.6-install.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: xine-lib-devel >= 1.0.1, gettext
BuildRequires: curl-devel, ImageMagick-devel, lirc-devel
BuildRequires: eject
%{!?_without_modxorg:BuildRequires: libX11-devel, libXtst-devel, libXinerama-devel}
%{?_without_modxorg:BuildRequires: XFree86-devel}
%{!?_without_lirc:BuildRequires: lirc-devel}

%description
oxine is a lightweight gui for the famous xine engine which uses the on screen
display functionality of xine to display its user interface elements like
buttons, lists sliders and so on. Due to this, oxine can easily be ported to
any video output device the xine library provides (e.g. frame buffer, dxr3,...)
and is particularly suitable for appliances like set-top boxes, home
entertainment systems or kiosk systems.

%prep
%setup
%patch0 -p1 -b .install

%build
# --disable-weather until we get libmetar packaged
# --without-jsw until we get libjsw packaged
%configure \
%{?_without_lirc:--disable-lirc} \
    --disable-rpath \
    --disable-weather \
    --enable-vdr \
    --without-jsw
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING ChangeLog NEWS README TODO doc/doc.html
%{_bindir}/oxine
%{_datadir}/oxine/

%changelog
* Mon Dec 18 2006 Matthias Saou <http://freshrpms.net/> 0.6-1
- Update to 0.6.
- Include install patch.
- Enable VDR.
- Disable (at least for now) weather and jsw because of not-yet-packaged libs.

* Wed Aug 31 2005 Matthias Saou <http://freshrpms.net/> 0.3.5-0.1.cvs
- Update to CVS snapshot.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 0.2-3.fr
- Rebuild for Fedora Core 1.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.

* Mon Mar 24 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.2.

* Tue Mar 18 2003 Matthias Saou <http://freshrpms.net/>
- Initial RPM release.

