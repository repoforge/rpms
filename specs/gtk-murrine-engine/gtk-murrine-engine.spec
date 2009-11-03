# $Id$
# Authority: hadams

%define real_name murrine

Summary: Murrine GTK2 engine
Name: gtk-murrine-engine
Version: 0.53.1
Release: 1%{?dist}
License: GPL
Group: User Interface/X
URL: http://cimi.netsons.org/pages/murrine.php

Source0: http://murrine.netsons.org/files/murrine-%{version}.tar.bz2
Source10: http://murrine.netsons.org/files/MurrinaFancyCandy.tar.bz2
Source11: http://murrine.netsons.org/files/MurrinaVerdeOlivo.tar.bz2
Source12: http://murrine.netsons.org/files/MurrinaAquaIsh.tar.bz2
Source13: http://murrine.netsons.org/files/MurrinaGilouche.tar.bz2
Source14: http://murrine.netsons.org/files/MurrinaLoveGray.tar.bz2
Source15: http://murrine.netsons.org/files/MurrineThemePack.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtk2-devel >= 2.8

%description
Murrine is a cairo-based fast gtk2 theme engine.

%prep
%setup -n %{real_name}-%{version}

%build
%configure \
    --enable-animation \
    --enable-macmenu
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
#find_lang %{real_name}
%{__install} -d -m0755 %{buildroot}%{_datadir}/themes/
tar -xvj -C %{buildroot}%{_datadir}/themes/ -f %{SOURCE10};
tar -xvj -C %{buildroot}%{_datadir}/themes/ -f %{SOURCE11};
tar -xvj -C %{buildroot}%{_datadir}/themes/ -f %{SOURCE12};
tar -xvj -C %{buildroot}%{_datadir}/themes/ -f %{SOURCE13};
tar -xvj -C %{buildroot}%{_datadir}/themes/ -f %{SOURCE14};
tar -xvj -C %{buildroot}%{_datadir}/themes/ -f %{SOURCE15};

%clean
%{__rm} -rf %{buildroot}

#files -f {real_name}.lang
%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING CREDITS NEWS
%{_datadir}/themes/MurrinaAquaIsh/
%{_datadir}/themes/MurrinaCandy/
%{_datadir}/themes/MurrinaCappuccino/
%{_datadir}/themes/MurrinaEalm/
%{_datadir}/themes/MurrinaFancyCandy/
%{_datadir}/themes/MurrinaGilouche/
%{_datadir}/themes/MurrinaLoveGray/
%{_datadir}/themes/MurrinaNeoGraphite/
%{_datadir}/themes/MurrinaVerdeOlivo/
%{_libdir}/gtk-2.0/*/engines/libmurrine.so
%exclude %{_libdir}/gtk-2.0/*/engines/libmurrine.la

%changelog
* Wed Jun  27 2007 Heiko Adams <info@fedora-blog.de> - 0.53-1
- Updated to release 0.53.

* Mon Jun  25 2007 Heiko Adams <info@fedora-blog.de> - 0.52-2
- Rebuild for RPMforge.

* Thu Apr  5 2007 Leo, Shidai Liu <sdl.web@gmail.com> - 0.52-1
- Updated to release 0.52.

* Thu Mar 15 2007 Leo, Shidai Liu <sdl.web@gmail.com> - 0.51-2
- Fix last change.

* Thu Mar 15 2007 Leo, Shidai Liu <sdl.web@gmail.com> - 0.51-1
- Updated to release 0.51.

* Fri Jan 12 2007 Shidai Liu, Leo <sdl.web@gmail.com> - 0.41-1
- Updated to release 0.41.

* Wed Jan 10 2007 Shidai Liu, Leo <sdl.web@gmail.com> - 0.40.1-1
- Updated to release 0.40.1.

* Fri Nov 24 2006 Shidai Liu, Leo <sdl.web@gmail.com> - 0.31-4
- Correct changelog entries to include release number.

* Tue Nov 21 2006 Shidai Liu, Leo <sdl.web@gmail.com> - 0.31-3
- Remove themes from gnome-look.
- Remove CREDITS patch.
- Add all themes from upstream.

* Thu Nov 16 2006 Shidai Liu, Leo <sdl.web@gmail.com> - 0.31-2
- Updated to release 0.31.

* Sun Nov 12 2006 Shidai Liu, Leo <sdl.web@gmail.com> - 0.30.2-1
- Add three gtk2 themes.

* Tue Sep 19 2006 Shidai Liu, Leo <sdl.web@gmail.com> 
- Initial build.
