# $Id: $

# Authority: dries
# Upstream: 

%define real_name Pike
%define real_version v7.6.6

Summary: General purpose programming language
Name: pike
Version: 7.6.6
Release: 1
License: GPL/LGPL/MPL
Group: Development/Languages
URL: http://pike.ida.liu.se/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: ftp://pike.ida.liu.se/pub/pike/latest-stable/%{real_name}-%{real_version}.tar.gz
Source1: ftp://pike.ida.liu.se/pub/pike/latest-stable/%{real_name}-%{real_version}-doc.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: nettle-devel, gmp-devel, autoconf, XFree86-devel
BuildRequires: gdbm-devel, gettext, zlib-devel, nasm, fftw-devel
BuildRequires: mysql-devel, unixODBC-devel, perl, postgresql-devel
BuildRequires: sane-backends-devel, openssl-devel, ffmpeg-devel
BuildRequires: freetype-devel, libjpeg-devel, libtiff-devel
BuildRequires: pcre-devel, bzip2-devel, freeglut-devel, gtk2-devel
BuildRequires: SDL-devel, pkgconfig, gtkglarea2-devel
BuildRequires: gtkglarea, gtk+, gtk+-devel, SDL_mixer-devel
%{?fc2:BuildRequires:xorg-x11-Mesa-libGLU,xorg-x11-Mesa-libGL}
%{?fc1:BuildRequires: XFree86-Mesa-libGL, XFree86-Mesa-libGLU}

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
%{_includedir}/pike

%changelog
* Tue Jun 08 2004 Dries Verachtert <dries@ulyssis.org> - 7.6.6-1
- Initial package.
