# $Id$
# Authority: matthias

%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}

%define desktop_vendor freshrpms

Summary: Frontend for the xine multimedia library
Name: gxine
Version: 0.3.3
Release: 2
License: GPL
Group: Applications/Multimedia
URL: http://xinehq.de/

Source:http://dl.sf.net/xine/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtk2-devel >= 2.0, xine-lib-devel >= 1.0.0
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}
Requires: gtk2 >= 2.0, xine-lib >= 1.0.0

%description
xine is a fully-featured free audio/video player for unix-like systems which
uses libxine for audio/video decoding and playback. For more informations on
what formats are supported, please refer to the libxine documentation.
gxine is a gtk based gui for this xine-library alternate to xine-ui.

Available rpmbuild rebuild options :
--without : freedesktop

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}

# We don't want those...
%{__rm} -f %{buildroot}%{_libdir}/gxine/{*.a,*.la}

%if %{!?_without_freedesktop:1}0
# Desktop entry
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install --vendor %{desktop_vendor} --delete-original \
  --dir %{buildroot}%{_datadir}/applications                      \
  --add-category GNOME                                            \
  --add-category X-Red-Hat-Extra                                  \
  --add-category Application                                      \
  --add-category AudioVideo                                       \
  %{buildroot}%{_datadir}/gnome/apps/Multimedia/gxine.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING README TODO
%{_bindir}/*
%{_libdir}/gxine/
%{_mandir}/man1/*
%lang(de) %{_mandir}/de/man1/*
%{!?_without_freedesktop:%{_datadir}/applications/%{desktop_vendor}-gxine.desktop}
%{?_without_freedesktop:%{_datadir}/gnome/apps/Multimedia/gxine.desktop}
%{_datadir}/gxine/

%changelog
* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 0.3.3-2.fr
- Rebuild for Fedora Core 1.

* Wed Apr  9 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.3.3.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.

* Sun Mar 23 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.3.2.

* Sun Mar 16 2003 Matthias Saou <http://freshrpms.net/>
- Added freedesktop build option.

* Mon Mar 10 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.3.1.

* Sun Mar  2 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.3.

* Tue Feb 25 2003 Matthias Saou <http://freshrpms.net/>
- Spec file cleanup.
- Converted desktop entry.

* Mon Dec 16 2002 Manfred Tremmel <Manfred.Tremmel@iiv.de>
- removed alle packman specific and added to gnome-xine cvs

* Sat Dec 07 2002 Manfred Tremmel <Manfred.Tremmel@iiv.de>
- Update to gxine 0.2

* Thu Dec 05 2002 Manfred Tremmel <Manfred.Tremmel@iiv.de>
- initial release

