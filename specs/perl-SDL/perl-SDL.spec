# $Id$
# Authority: matthias

Summary: Simple DirectMedia Layer - Bindings for the perl language
Name: perl-SDL
Version: 1.20.0
Release: 6
License: GPL
Group: System Environment/Libraries
URL: http://sdlperl.org/
Source: ftp://sdlperl.org/SDL_perl/SDL_perl-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: SDL >= 1.2.3, SDL_mixer >= 1.0.5, SDL_image >= 1.0.0, SDL_net
Requires: SDL_ttf, libjpeg, libpng, smpeg, perl
BuildRequires: SDL-devel, SDL_mixer-devel, SDL_image-devel, SDL_net-devel
BuildRequires: SDL_ttf-devel, libjpeg-devel, libpng-devel, smpeg-devel
# This is to pull in missing libs, to fix the "undefined symbol: _Znwj" problem
%{?!dist:BuildRequires: xorg-x11-Mesa-libGLU}
%{?fc3:BuildRequires: xorg-x11-Mesa-libGLU}
%{?fc2:BuildRequires: xorg-x11-Mesa-libGLU}
%{?fc1:BuildRequires: XFree86-Mesa-libGLU}
BuildRequires: XFree86-devel

%description
The SDL (Simple DirectMedia Layer) bindings for the perl language.


%prep
%setup -n SDL_perl-%{version}


%build
CFLAGS="%{optflags}" perl Makefile.PL PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"


%install
%{__rm} -rf %{buildroot}
eval `%{__perl} '-V:installarchlib'`
%{__mkdir_p} %{buildroot}${installarchlib}
%makeinstall
%{__rm} -f `/usr/bin/find %{buildroot} -type f -name perllocal.pod -o -name .packlist`

# Build the file list to include
find %{buildroot}%{_prefix} -type f -print | \
    %{__sed} "s|^%{buildroot}||g" | \
    %{__sed} "s|3pm$|3pm*|g" > %{name}.list


%clean
%{__rm} -rf %{buildroot}


%files -f %{name}.list
%defattr(-, root, root, 0755)
%doc BUGS CHANGELOG COPYING MANIFEST README TODO


%changelog
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

