# $Id: $

# Authority: dries
# Upstream: rekless@fastmail.fm

Summary: Clone of skyroads, jump and speed along platforms to reach the goal
Name: skystreets
Version: 0.2.3
Release: 1
License: GPL
Group: Amusements/Games
URL: http://skystreets.kaosfusion.com/
Source: http://skystreets.kaosfusion.com/skystreets-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc-c++, SDL-devel, SDL_image-devel, libtiff-devel, libtiff, libjpeg, zlib, XFree86-Mesa-libGL, XFree86-Mesa-libGLU
Requires: SDL, SDL_image, libtiff

# Screenshot: http://skystreets.kaosfusion.com/screenshot3.png
# ScreenshotUrl: http://skystreets.kaosfusion.com/

%description
A modernised remake of the popular old game, Skyroads, by Bluemoon software.
The objective is to go along the tracks, and try to reach the objective
before either your fuel or oxygen run out, whilst trying to get as fast a
time as possible. Some obstacles require more thought or tact. 

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%{_bindir}/skystreets
%{_datadir}/skystreets

%changelog
* Wed Mar 31 2004 Dries Verachtert <dries@ulyssis.org> 0.2.3-1
- initial packaging
