# $Id$
# Authority: dag
# Upstream: Sergio Sigala <sergio$sigala,it>

Summary: Unix port of Borland TurboVision library
Name: tvision
Version: 0.8
Release: 1.2%{?dist}
License: BSD-like
Group: Development/Libraries
URL: http://tvision.sourceforge.net/

Source: http://www.sigala.it/sergio/tvision/mysource/tvision-%{version}.tar.gz
#Patch0: tvision-info.patch
#Patch1: tvision-am_fixes.patch
#Patch2: tvision-endian.h.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, gpm-devel, ncurses-devel >= 5.3
Requires: /sbin/ldconfig

%description
Turbo Vision (or TV, for short) is a library that provides an
application framework. With TV you can write a beautiful
object-oriented character-mode user interface in a short time.

TV is available in C++ and Pascal and is a product of Borland
International. It was developed to run on MS-DOS systems, but today it
is available for many other platforms (ported by independent
programmers).

This port is based on the Borland 2.0 version with fixes.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup
#%patch0 -p1
#%patch1 -p1
#%patch2 -p1

%{__perl} -pi.orig -e 's|<sys/time.h>|<time.h>|' demo/puzzle.cc

%build
CXXFLAGS="-I%{_includedir}/ncurses -fno-exceptions -fno-rtti -fno-implicit-templates"
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

#%{__make} install \
#	DESTDIR=$RPM_BUILD_ROOT

%{__install} -Dp -m0644 doc/tvision.info %{buildroot}%{_infodir}

# some cleaning
%{__make} -C tutorial mostlyclean
%{__make} -C demo     mostlyclean

### Clean up docdir
%{__rm} -f demo/Makefile* tutorial/Makefile* doc/{*.info,*.texi,*.tex,*.sed,*.kdoc,Makefile*}

%{__cat} <<'EOF' >tutorial/Makefile
CPPFLAGS = -g
LDFLAGS = -lncurses -lgpm -ltvision

SOURCES := $(wildcard *.cc)
PROGS   := $(patsubst %.cc,%,$(SOURCES))

all: $(PROGS)
EOF

%clean
%{__rm} -rf %{buildroot}

%post
/sbin/ldconfig 2>/dev/null
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
/sbin/ldconfig 2>/dev/null
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(-, root, root, 0755)
%doc Announce ChangeLog COPYRIGHT README TODO
%doc %{_infodir}/*
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%doc demo/ doc/* tutorial/
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/lib*.a
%exclude %{_libdir}/lib*.la
#%{_examplesdir}/%{name}

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.8-1.2
- Rebuild for Fedora Core 5.

* Wed Jun 02 2004 Dag Wieers <dag@wieers.com> - 0.8-1
- Initial package. (using DAR)
