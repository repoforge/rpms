# $Id$
# Authority: dries
# Upstream:

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

%define real_name Pike
%define real_version v7.6.24

Summary: General purpose programming language
Name: pike
Version: 7.6.24
Release: 1.2%{?dist}
License: GPL/LGPL/MPL
Group: Development/Languages
URL: http://pike.ida.liu.se/

Source: http://pike.ida.liu.se/pub/pike/latest-stable/Pike-v%{version}.tar.gz
Source1: http://pike.ida.liu.se/pub/pike/latest-stable/Pike-v%{version}-doc.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: nettle-devel, gmp-devel, autoconf
BuildRequires: gdbm-devel, gettext, zlib-devel, nasm, fftw-devel
BuildRequires: mysql-devel, unixODBC-devel, perl, postgresql-devel
BuildRequires: sane-backends-devel, openssl-devel, ffmpeg-devel
BuildRequires: freetype-devel, libjpeg-devel, libtiff-devel
BuildRequires: pcre-devel, bzip2-devel, freeglut-devel, gtk2-devel
BuildRequires: SDL-devel, pkgconfig, gtkglarea2-devel
BuildRequires: gtkglarea, gtk+, gtk+-devel, SDL_mixer-devel
%if 0%{?_without_modxorg:1}
%{?_without_xorg:BuildRequires: XFree86-devel, XFree86-Mesa-libGLU}
%{!?_without_xorg:BuildRequires: xorg-x11-devel, xorg-x11-Mesa-libGLU}
%else
BuildRequires: libXt-devel, mesa-libGLU-devel
%endif

%description
Pike is a general purpose programming language, which means that you can put
it to use for almost any task. Its application domain spans anything from
the world of the Net to the world of multimedia applications, or
environments where your shell could use some spicy text processing or system
administration tools.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n %{real_name}-%{real_version}

%build
STARTPWD=`pwd`
cd src
./run_autoconfig
mkdir ../build; cd ../build
${STARTPWD}/src/configure \
  --prefix=/usr
%{__make} %{?_smp_mflags}
%{__make} documentation %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
cd build
%makeinstall INSTALLARGS="--traditional"
%{__mkdir_p} %{buildroot}%{_bindir}
%{__mv} %{buildroot}/usr/pike %{buildroot}%{_bindir}
%{__mv} %{buildroot}/usr/pike.syms %{buildroot}%{_bindir}
%{__mv} %{buildroot}/usr/rsif %{buildroot}%{_bindir}
%{__mv} %{buildroot}/usr/doc/pike ../pikedocs
%{__install} -d -m0755 %{buildroot}%{_mandir}/man1/
%{__mv} %{buildroot}/usr/man/man1/pike.1 %{buildroot}%{_mandir}/man1/
cd %{buildroot}
find . -type f | xargs perl -pi -e "s|/usr/local/bin/pike|%{_bindir}/pike|g"


%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ANNOUNCE CHANGES COMMITTERS COPYING COPYRIGHT README README-CVS
%doc %{_mandir}/man?/*
%doc pikedocs/*
%exclude /usr/hilfe
%{_bindir}/*
%{_libdir}/pike

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/pike
### FIXME : some libs needs to be moved from the main to here?

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 7.6.24-1.2
- Rebuild for Fedora Core 5.

* Mon Aug 15 2005 Dries Verachtert <dries@ulyssis.org> - 7.6.24-1
- Update to release 7.6.24.

* Tue Jun 08 2004 Dries Verachtert <dries@ulyssis.org> - 7.6.6-1
- Initial package.

