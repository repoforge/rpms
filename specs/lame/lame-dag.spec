# $Id$
# Authority: matthias
# Distcc: 0

Summary: Quality LGPL MP3 encoder
Name: lame
Version: 3.95.1
Release: 0
License: LGPL
Group: Applications/Multimedia
URL: http://lame.sf.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/lame/lame-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: ncurses-devel, nasm
Provides: mp3encoder

%description
LAME is an educational tool to be used for learning about MP3 encoding.
The goal of the LAME project is to use the open source model to improve
the psycho acoustics, noise shaping and speed of MP3. Another goal of
the LAME project is to use these improvements for the basis of a patent
free audio compression codec for the GNU project.

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build
#%{?rh73:export CC="gcc"}
export CC_OPTS="-O3 -march=i386 -mcpu=i686 -fomit-frame-pointer -fno-strength-reduce -malign-functions=4 -funroll-loops -ffast-math"
%configure \
	--disable-dependency-tracking \
	--disable-debug \
	--enable-nasm \
	--enable-decoder \
	--enable-brhist \
	--with-vorbis 
#	--enable-analyser=no
%{__make} %{?_smp_mflags} test \
	CFLAGS="${CC_OPTS}"

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Some apps still expect to find <lame.h>
%{__ln_s} -f lame/lame.h %{buildroot}%{_includedir}/lame.h

### Clean up documents
%{__rm} -f doc/html/Makefile*

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_docdir}/lame/
%{__rm} -f %{buildroot}%{_libdir}/*.la

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr (-, root, root, 0755)
%doc ChangeLog README TODO USAGE doc/html
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_libdir}/*.so.*

%files devel
%defattr (-, root, root, 0755)
%doc API HACKING STYLEGUIDE
%{_libdir}/*.a
%{_libdir}/*.so
%{_includedir}/lame/
#exclude %{_libdir}/*.la

%changelog
* Mon Jan 12 2004 Dag Wieers <dag@wieers.com> - 3.95.1-0
- Updated to release 3.95.1.

* Wed Feb 19 2003 Dag Wieers <dag@wieers.com> - 3.93.1-1
- Removed --enable-analyze=no for configure.

* Sun Jan 19 2003 Dag Wieers <dag@wieers.com> - 3.93.1-0
- Initial package. (using DAR)
