# Authority: matthias
# Upstream: David J. Goehrig <dave@goehrig.us>

%define real_name SDL_perl

Summary: Simple DirectMedia Layer - Bindings for the perl language
Name: perl-SDL
Version: 1.20.0
Release: 3
License: LGPL
Group: Applications/CPAN
URL: http://sdlperl.org/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: ftp://sdlperl.org/SDL_perl/SDL_perl-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: SDL-devel, SDL_mixer-devel, SDL_image-devel, SDL_net-devel, SDL_ttf-devel
BuildRequires: perl, libjpeg-devel, libpng-devel, smpeg-devel
BuildRequires: XFree86-Mesa-libGLU

%description
SDL_perl provides multimedia programming support for perl through
use of the Simple DirectMedia Layer http://www.libsdl.org

It provides both a high level, object orient develpment framework,
and a low level C style API.  SDL_perl supports a variety of
additional SDL libraries, such as SDL_image, SDL_mixer, SDL_ttf,
and SDL_net.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL \
	PREFIX="%{buildroot}%{_prefix}" \
	INSTALLDIRS="vendor"
%{__make} %{?_smp_mflags} \
	OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_libdir}/perl5/*/*-linux-thread-multi/
%{__rm} -f %{buildroot}%{_libdir}/perl5/vendor_perl/*/*-linux-thread-multi/auto/*{,/*}/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc BUGS CHANGELOG COPYING MANIFEST README TODO
%doc %{_mandir}/man?/*
%{_libdir}/perl5/vendor_perl/*/*

%changelog
* Tue Dec 09 2003 Dag Wieers <dag@wieers.com> - 1.20.0-3
- Added smpeg-devel and SDL_ttf-devel to BuildRequires. (Kevin Brouelette)

* Sun Feb 14 2003 Dag Wieers <dag@wieers.com> - 1.20.0-0
- Initial package. (using DAR)
