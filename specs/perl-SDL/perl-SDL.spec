# $Id$
# Authority: matthias

Summary: Simple DirectMedia Layer - Bindings for the perl language
Name: perl-SDL
Version: 1.20.0
Release: 4
License: GPL
Group: System Environment/Libraries
URL: http://sdlperl.org/

Source: ftp://sdlperl.org/SDL_perl/SDL_perl-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: SDL >= 1.2.3, SDL_mixer >= 1.0.5, SDL_image >= 1.0.0
Requires: SDL_net
Requires: libjpeg, libpng, perl
BuildRequires: SDL-devel, SDL_mixer-devel, SDL_image-devel, SDL_net-devel
BuildRequires: libjpeg-devel, libpng-devel, perl, XFree86-Mesa-libGLU

%description
The SDL (Simple DirectMedia Layer) bindings for the perl language.

%prep
%setup -n SDL_perl-%{version}

%build
CFLAGS="%{optflags}" perl Makefile.PL PREFIX=%{buildroot}%{_prefix}
%{__make} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
eval `perl '-V:installarchlib'`
mkdir -p %{buildroot}$installarchlib
%makeinstall
%{__rm} -f `find %{buildroot} -type f -name perllocal.pod -o -name .packlist`

# Build the file list to include
find %{buildroot}%{_prefix} -type f -print | \
    sed "s|^%{buildroot}||g" | \
    sed "s|3pm$|3pm*|g" > %{name}.list

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.list
%defattr(-, root, root, 0755)
%doc BUGS CHANGELOG COPYING MANIFEST README TODO

%changelog
* Wed Dec 10 2003 Matthias Saou <http://freshrpms.net/> 1.20.0-4.fr
- Fix the package at last by adding XFree86-Mesa-libGLU build dep, thanks to
  Ian Burrell.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 1.20.0-3.fr
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

