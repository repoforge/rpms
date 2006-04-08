# $Id$
# Authority: dries

Summary: Jump-and-run scrolling game starring Tux the Penguin
Name: supertux
Version: 0.1.3
Release: 1.2
License: GPL
Group: Applications/
URL: http://supertux.berlios.de/

Source: http://download.berlios.de/supertux/supertux-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, SDL-devel, SDL_image-devel, SDL_mixer-devel
BuildRequires: zlib-devel

%description
Super Tux is a jump-and-run scrolling platform game starring Tux the
Penguin (and his girlfriend, Gown). It is similar to games like
Nintendo's Super Mario Bros

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
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%{_bindir}/supertux
%{_datadir}/pixmaps/supertux.png
%{_datadir}/applications/supertux.desktop
%{_datadir}/supertux/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.1.3-1.2
- Rebuild for Fedora Core 5.

* Sun Nov 13 2005 Dries Verachtert <dries@ulyssis.org> - 0.1.3-1
- Initial package.
