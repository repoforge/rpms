# $Id$
# Authority: matthias

%{?dist: %{expand: %%define %dist 1}}

%define perl_archsitelib %(eval "`%{__perl} -V:installsitearch`"; echo $installsitearch)
%define _use_internal_dependency_generator 0

Summary: Simple DirectMedia Layer - Bindings for the perl language
Name: perl-SDL
Version: 2.1.2
Release: 2
License: GPL
Group: System Environment/Libraries
URL: http://sdl.perl.org/
Source: http://search.cpan.org/CPAN/authors/id/D/DG/DGOEHRIG/SDL_Perl-%{version}.tar.gz
Source10: filter-depends.sh
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: SDL-devel, SDL_mixer-devel, SDL_image-devel, SDL_net-devel
BuildRequires: SDL_ttf-devel, SDL_gfx-devel
BuildRequires: smpeg-devel, libjpeg-devel, libpng-devel, XFree86-devel
BuildRequires: perl(Module::Build)
# This is to pull in missing libs, to fix the "undefined symbol: _Znwj" problem
%{?!dist:BuildRequires: xorg-x11-Mesa-libGLU}
%{?fc3:BuildRequires: xorg-x11-Mesa-libGLU}
%{?fc2:BuildRequires: xorg-x11-Mesa-libGLU}
%{?fc1:BuildRequires: XFree86-Mesa-libGLU}
Provides: SDL_perl = %{version}-%{release}
Provides: SDL_Perl = %{version}-%{release}

%define __find_requires %{SOURCE10}

%description
The SDL (Simple DirectMedia Layer) bindings for the perl language.


%prep
%setup -n SDL_Perl-%{version}


%build
%{__perl} Build.PL
./Build
# This, we don't want since it'll fail the audio dev check in a minimal chroot
#./Build test


%install
%{__rm} -rf %{buildroot}
./Build install destdir=%{buildroot}

# Remove files we don't want to include
%{__rm} -f `/usr/bin/find %{buildroot} -type f \
    -name perllocal.pod -o -name .packlist -o -name '*.bs'`


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc BUGS CHANGELOG COPYING MANIFEST README TODO
%{perl_archsitelib}/auto/SDL/
%{perl_archsitelib}/auto/SDL_perl/
%{perl_archsitelib}/SDL/
%{perl_archsitelib}/SDL.pm
%{perl_archsitelib}/SDL_perl.pm
%{_mandir}/man3/*


%changelog
* Wed Jan  5 2005 Matthias Saou <http://freshrpms.net/> 2.1.2-2
- Rebuild against SDL_gfx 2.0.13.

* Fri Nov  5 2004 Matthias Saou <http://freshrpms.net/> 2.1.2-1
- Update to 2.1.2.
- Add provides of "SDL_perl" and "SDL_Perl".
- Add SDL_gfx dependency.

* Mon Jun 21 2004 Matthias Saou <http://freshrpms.net/> 1.20.0-6
- Bump release number to fix smpeg dependency caused by old headers.

* Wed Jun  9 2004 Matthias Saou <http://freshrpms.net/> 1.20.0-5
- Rebuild for Fedora Core 2.
- Replace XFree86-Mesa-libGLU build dependency with new xorg-x11-Mesa-libGLU.
- Added SDL_ttf and smpeg to the build requirements.

* Wed Dec 10 2003 Matthias Saou <http://freshrpms.net/> 1.20.0-4
- Fix the package at last by adding XFree86-Mesa-libGLU build dep, thanks to
  Ian Burrell.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 1.20.0-3
- Rebuild for Fedora Core 1.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.

* Mon Feb 17 2003 Matthias Saou <http://freshrpms.net/>
- Update to 1.20.0.

* Mon Oct 28 2002 Matthias Saou <http://freshrpms.net/>
- Update to 1.19.0.
- Major spec file adaptation :-/

* Fri Sep 20 2002 Matthias Saou <http://freshrpms.net/>
- Update to 1.18.7.
- Minor spec cleanups.

* Mon Apr 15 2002 Matthias Saou <http://freshrpms.net/>
- Update to 1.16.

* Thu Feb  7 2002 Matthias Saou <http://freshrpms.net/>
- Initial RPM release.

