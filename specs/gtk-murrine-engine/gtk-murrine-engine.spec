# $Id$
# Authority: hadams

Summary: Murrine GTK2 engine
Name: gtk-murrine-engine
Version: 0.53.1
Release: 1
License: GPL
Group: System Environment/Libraries
URL: http://cimi.netsons.org/pages/murrine.php
Source0: http://murrine.netsons.org/files/murrine-%{version}.tar.bz2
Source10: http://murrine.netsons.org/files/MurrinaFancyCandy.tar.bz2
Source11: http://murrine.netsons.org/files/MurrinaVerdeOlivo.tar.bz2
Source12: http://murrine.netsons.org/files/MurrinaAquaIsh.tar.bz2
Source13: http://murrine.netsons.org/files/MurrinaGilouche.tar.bz2
Source14: http://murrine.netsons.org/files/MurrinaLoveGray.tar.bz2
Source15: http://murrine.netsons.org/files/MurrineThemePack.tar.bz2
BuildRequires: gtk2-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Murrine is a cairo-based fast gtk2 theme engine.

%prep
%setup -q -n murrine-%{version}

%build
%configure --enable-animation --enable-macmenu
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/themes
(cd $RPM_BUILD_ROOT/%{_datadir}/themes;
bzcat %{SOURCE10} | tar -xvf -;
bzcat %{SOURCE11} | tar -xvf -;
bzcat %{SOURCE12} | tar -xvf -;
bzcat %{SOURCE13} | tar -xvf -;
bzcat %{SOURCE14} | tar -xvf -;
bzcat %{SOURCE15} | tar -xvf -;
)

#remove .la files
find $RPM_BUILD_ROOT -name *.la | xargs rm -f || true
#fix permission
find $RPM_BUILD_ROOT/%{_datadir}/themes -type f | xargs chmod 0644 || true

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog NEWS CREDITS COPYING
%{_libdir}/gtk-2.0/*/engines/*
%{_datadir}/*

%changelog
* Wed Jun  27 2007 Heiko Adams <info@fedora-blog.de> 0.53-1
- 0.53.1

* Mon Jun  25 2007 Heiko Adams <info@fedora-blog.de> 0.52-2
- Rebuild for CentOS

* Thu Apr  5 2007 Leo, Shidai Liu <sdl.web@gmail.com> 0.52-1
- 0.52

* Thu Mar 15 2007 Leo, Shidai Liu <sdl.web@gmail.com> 0.51-2
- fix last change

* Thu Mar 15 2007 Leo, Shidai Liu <sdl.web@gmail.com> 0.51-1
- 0.51

* Fri Jan 12 2007 Shidai Liu, Leo <sdl.web@gmail.com> 0.41-1
- 0.41

* Wed Jan 10 2007 Shidai Liu, Leo <sdl.web@gmail.com> 0.40.1-1
- 0.40.1

* Fri Nov 24 2006 Shidai Liu, Leo <sdl.web@gmail.com> 0.31-4
- Correct changelog entries to include release number

* Tue Nov 21 2006 Shidai Liu, Leo <sdl.web@gmail.com> 0.31-3
- remove themes from gnome-look
- remove CREDITS patch
- add all themes from upstream

* Thu Nov 16 2006 Shidai Liu, Leo <sdl.web@gmail.com> 0.31-2
- 0.31

* Sun Nov 12 2006 Shidai Liu, Leo <sdl.web@gmail.com> 0.30.2-1
- Add three gtk2 themes

* Tue Sep 19 2006 Shidai Liu, Leo <sdl.web@gmail.com> 
- Initial build.

