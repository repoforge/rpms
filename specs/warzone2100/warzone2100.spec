# $Id$
# Authority: dries

Summary: 3D real time strategy game
Name: warzone2100
Version: 2.0.10
Release: 1
License: GPL
Group: Amusements/Games
URL: http://wz2100.net/

Source: http://download.gna.org/warzone/releases/2.0/warzone2100-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: physfs-devel, SDL_net-devel, openal-devel, bison, libvorbis-devel, flex, libjpeg-devel

%description
Warzone 2100 Resurrection is an effort to continue maintainence and 
publishing of Warzone 2100. Warzone 2100 was one of the first 3D RTS 
games ever. It was released commercially by Pumpkin Studies in 1999, 
and released in 2004 under the GPL.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING* INSTALL TODO doc/*
%{_bindir}/warzone2100
%{_datadir}/icons/warzone2100.png
%{_datadir}/applications/warzone2100.desktop
%{_datadir}/warzone2100/
%exclude %{_docdir}/warzone2100/

%changelog
* Sun Feb  3 2008 Dries Verachtert <dries@ulyssis.org> - 2.0.10-1
- Initial package.
