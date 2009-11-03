# $Id$
# Authority: dag

%{?fedora: %{expand: %%define fc%{fedora} 1}}

%{?fc4:%define _without_modxorg 1}
%{?el4:%define _without_modxorg 1}
%{?fc3:%define _without_modxorg 1} 
%{?fc2:%define _without_modxorg 1}
%{?fc1:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}
%{?rh9:%define _without_modxorg 1}
%{?rh7:%define _without_modxorg 1}
%{?el2:%define _without_modxorg 1}
%{?rh6:%define _without_modxorg 1}
%{?yd3:%define _without_modxorg 1}

%{?fc1:%define _without_xorg 1}
%{?el3:%define _without_xorg 1}
%{?rh9:%define _without_xorg 1}
%{?rh8:%define _without_xorg 1}
%{?rh7:%define _without_xorg 1}
%{?el2:%define _without_xorg 1}
%{?rh6:%define _without_xorg 1}
%{?yd3:%define _without_xorg 1}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)
#define _use_internal_dependency_generator 0

%define real_name SDL_Perl

Summary: Simple DirectMedia Layer - Bindings for the perl language
Name: perl-SDL
Version: 2.1.3
Release: 2%{?dist}
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/SDL_Perl/
#URL: http://sdl.perl.org/

Source: http://www.cpan.org/authors/id/D/DG/DGOEHRIG/SDL_Perl-%{version}.tar.gz
Source10: filter-depends.sh
Patch0: http://ftp.debian.org/debian/pool/main/s/sdlperl/sdlperl_2.1.2-1.diff.gz
Patch1: perl-SDL-no-mixertest.patch
Patch2: perl-SDL-gfxPie.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: SDL-devel
BuildRequires: SDL_mixer-devel
BuildRequires: SDL_image-devel
BuildRequires: SDL_net-devel
BuildRequires: SDL_ttf-devel
BuildRequires: SDL_gfx-devel
BuildRequires: smpeg-devel
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
BuildRequires: perl(Module::Build)
BuildRequires: perl(YAML)
%if 0%{?_without_modxorg:1}
%{?_without_xorg:BuildRequires: XFree86-devel, XFree86-Mesa-libGLU}
%{!?_without_xorg:BuildRequires: xorg-x11-devel, xorg-x11-Mesa-libGLU}
%else
BuildRequires: libXt-devel
BuildRequires: mesa-libGLU-devel
%endif
Provides: SDL_perl = %{version}-%{release}
Provides: SDL_Perl = %{version}-%{release}

%define __find_requires %{SOURCE10}

%description
The SDL (Simple DirectMedia Layer) bindings for the perl language.

%prep
%setup -n %{real_name}-%{version}
%patch0 -p1
patch -p1 -b -z .deb < debian/patches/030_glu_nurbs.diff
patch -p1 < debian/patches/030_opengl_fixes.diff
%patch1 -p1 -z .no-mixertest
%patch2 -p0 -z .gfxPie

%build
%{__perl} Build.PL
./Build

### Fix the location from where the modules are to be copied
%{__cp} -av blib/arch/auto/src/SDL* blib/arch/auto/

# This, we don't want since it'll fail the audio dev check in a minimal chroot
#./Build test

%install
%{__rm} -rf %{buildroot}
PERL_INSTALL_ROOT="%{buildroot}" ./Build install installdirs="vendor"

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;
%{__rm} -rf %{buildroot}%{perl_vendorarch}/auto/src/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc BUGS CHANGELOG COPYING MANIFEST META.yml README TODO
%doc %{_mandir}/man3/*.3pm*
%{perl_vendorarch}/auto/SDL/
%{perl_vendorarch}/auto/SDL_perl/
%{perl_vendorarch}/SDL/
%{perl_vendorarch}/SDL.pm
%{perl_vendorarch}/SDL_perl.pm

%changelog
* Mon Apr 27 2009 Dag Wieers <dag@wieers.com> - 2.1.3-2
- Rebuild against SDL_gfx 2.0.19.

* Fri Mar 30 2007 Dag Wieers <dag@wieers.com> - 2.1.3-1
- Move the modules from %%{perl_sitearch} to %{perl_vendorarch}.
- Updated to release 2.1.3.

* Thu Dec 28 2006 Dag Wieers <dag@wieers.com> - 2.1.2-6
- Rebuild against SDL_gfx 2.0.15.

* Fri Mar 17 2006 Matthias Saou <http://freshrpms.net/> 2.1.2-5
- Release bump to drop the disttag number in FC5 build.

* Thu Jan 12 2006 Matthias Saou <http://freshrpms.net/> 2.1.2-4
- Add modular xorg build conditional.

* Thu Apr 21 2005 Matthias Saou <http://freshrpms.net/> 2.1.2-3
- Change PREFIX override to env PERL_INSTALL_ROOT, as perl 5.8.6 requires it.

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

