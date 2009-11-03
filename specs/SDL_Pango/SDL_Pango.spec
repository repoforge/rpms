# $Id$
# Authority: dag

Summary: Rendering of internationalized text for SDL (Simple DirectMedia Layer)
Name: SDL_Pango
Version: 0.1.2
Release: 1%{?dist}
License: LGPL
Group: System Environment/Libraries
URL: http://sdlpango.sourceforge.net/

Source0: http://dl.sf.net/sdlpango/SDL_Pango-%{version}.tar.gz
Source1: doxygen.png
Patch0: SDL_Pango-0.1.2-suppress-warning.patch
Patch1: SDL_Pango-0.1.2-API-adds.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: pango-devel, SDL-devel, dos2unix
BuildRequires: autoconf, automake, libtool

%description
Pango is the text rendering engine of GNOME 2. SDL_Pango connects that engine
to SDL, the Simple DirectMedia Layer.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: pango-devel, SDL-devel, pkgconfig

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup
%patch0 -p1 -b .suppress-warning

dos2unix src/SDL_Pango.c src/SDL_Pango.h

%patch1 -p1 -b .API-adds

# Clean up, we include the entire "docs/html" content for the devel package
%{__rm} -rf docs/html/CVS/

# Replace the corrupt doxygen.png file with a proper one
%{__install} -m 0644 -p %{SOURCE1} docs/html/doxygen.png

# Fix the (many) DOS encoded files, not *.png since they get corrupt
find . -not -name \*.png -type f -exec dos2unix -k {} \;

# For FC-5 x86_64 this is required, or the shared library doesn't get built
autoreconf
libtoolize --copy --force

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%doc docs/html/*
%{_includedir}/SDL_Pango.h
%{_libdir}/pkgconfig/SDL_Pango.pc
%exclude %{_libdir}/*.a
%exclude %{_libdir}/*.la
%{_libdir}/*.so

%changelog
* Fri Sep 29 2006 Matthias Saou <http://freshrpms.net/> 0.1.2-4
- Add autoreconf and libtoolize calls since on FC5 x86_64 the shared library
  isn't build otherwise.
- Add API-adds patch (submitted upstream), required for the only project known
  to use SDL_Pango, so it does makes kind of sense...

* Tue Sep 26 2006 Matthias Saou <http://freshrpms.net/> 0.1.2-3
- Use dos2unix to convert all DOS encoded files.
- Replace the corrupt doxygen.png file with a proper one.

* Tue Sep 26 2006 Matthias Saou <http://freshrpms.net/> 0.1.2-2
- Change %%makeinstall to using DESTDIR, according to the guidelines.
- Include patch from Mamoru Tasaka to remove all compilation warnings.

* Fri Sep 22 2006 Matthias Saou <http://freshrpms.net/> 0.1.2-1
- Initial RPM release.
