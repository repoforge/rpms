# $Id$
# Authority: dries
# Upstream: Vincent LaBella <vlabella$albany,edu>

%{?dtag: %{expand: %%define %dtag 1}}

%{?fc4:%define _without_modxorg 1}
%{?el4:%define _without_modxorg 1}
%{?fc3:%define _without_modxorg 1}
%{?fc2:%define _without_modxorg 1}
%{?fc1:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}
%{?rh9:%define _without_modxorg 1}
%{?rh7:%define _without_modxorg 1}
%{?el2:%define _without_modxorg 1}

Summary: Graphics Layout Engine
Name: gle
Version: 4.2.0
Release: 1
License: BSD
Group: Applications/Multimedia
URL: http://www.gle-graphics.org/

Source: http://dl.sf.net/glx/GLE-%{version}-src.zip
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, libpng-devel, libtiff-devel, ncurses-devel, zlib-devel
BuildRequires: libstdc++-devel >= 3.0
%{?_without_modxorg:BuildRequires: XFree86-devel}
%{!?_without_modxorg:BuildRequires: xorg-x11-proto-devel}

%description
GLE (Graphics Layout Engine) is a high-quality graphics package for
scientists, combining a user-friendly scripting language with a full
range of facilities for producing publication-quality graphs, diagrams,
posters and slides. GLE provides LaTeX quality fonts together with a
flexible graphics module which allows the user to specify any feature of
a graph. Complex pictures can be drawn with user-defined subroutines and
simple looping structures. Current output formats include EPS, PS, PDF,
JPEG, and PNG.

%prep
%setup -n gle4

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall DESTDIR=%{buildroot}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README.txt LICENSE.txt
%doc %{_mandir}/man1/gle.1*
%{_libdir}/pkgconfig/gle-graphics.pc
%{_bindir}/gle
%{_bindir}/manip
%{_datadir}/gle

%changelog
* Tue Apr 14 2009 Dries Verachtert <dries@ulyssis.org> - 4.2.0-1
- Updated to release 4.2.0.

* Thu Mar 13 2008 Dries Verachtert <dries@ulyssis.org> - 4.1.2-1
- Updated to release 4.1.2.

* Tue Jan 15 2008 Dries Verachtert <dries@ulyssis.org> - 4.1.1-1
- Updated to release 4.1.1.

* Sun Oct 15 2006 Jonas Frantz <jonas.frantz@welho.com> - 4.0.12-1
- Updated to release 4.0.12.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 4.0.11-2.2
- Rebuild for Fedora Core 5.

* Sat Dec 17 2005 Dries Verachtert <dries@ulyssis.org> - 4.0.11-1
- Updated to release 4.0.11.

* Sat Nov 19 2005 Jonas Frantz <jonas.frantz@welho.com> - 4.0.10-2
- Fix problem with making inittex.ini

* Mon Nov 08 2005 Dries Verachtert <dries@ulyssis.org> - 4.0.10-1
- Initial package.
