# $Id: lzo.spec 3101 2005-04-04 20:13:17Z dag $
# Authority: dag
# Upstream: Markus F.X.J. Oberhumer <markus$oberhumer,com>

### EL6 ships with lzo-2.03-3.1.el6
%{?el6:# Tag: rfx}

Summary: Portable lossless data compression library
Name: lzo
Version: 2.06
Release: 1%{?dist}
License: GPL
Group: System Environment/Libraries
URL: http://www.oberhumer.com/opensource/lzo/

Source: http://www.oberhumer.com/opensource/lzo/download/lzo-%{version}.tar.gz
Patch0: lzo-2.06-configure.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: autoconf
BuildRequires: gcc-c++
BuildRequires: zlib-devel
Requires: zlib >= 1.0.0
Obsoletes: lzo2 <= %{version}-%{release}

%description
LZO is a portable lossless data compression library written in ANSI C.
It offers pretty fast compression and *very* fast decompression.
Decompression requires no memory. In addition there are slower
compression levels achieving a quite competitive compression ratio
while still decompressing at this very high speed.

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Obsoletes: lzo2-devel <= %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%package minilzo
Summary: Mini version of lzo for apps which don't need the full version
Group: System Environment/Libraries

%description minilzo
A small (mini) version of lzo for embedding into applications which don't need
full blown lzo compression support.

%prep
%setup
%patch0 -p1 -z .configure

%build
%configure \
    --disable-dependency-tracking \
    --disable-static \
    --enable-shared
%{__make} %{?_smp_mflags}

# build minilzo too (bz 439979)
gcc %{optflags} -fpic -Iinclude/lzo -o minilzo/minilzo.o -c minilzo/minilzo.c
gcc -g -shared -o libminilzo.so.0 -Wl,-soname,libminilzo.so.0 minilzo/minilzo.o


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
install -m 755 libminilzo.so.0 $RPM_BUILD_ROOT%{_libdir}
ln -s libminilzo.so.0 $RPM_BUILD_ROOT%{_libdir}/libminilzo.so
install -p -m 644 minilzo/minilzo.h $RPM_BUILD_ROOT%{_includedir}/lzo

#Remove doc
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/lzo

%check
make check test

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING THANKS NEWS
%{_libdir}/liblzo2.so.*

%files devel
%defattr(-, root, root, 0755)
%doc doc/LZOAPI.TXT doc/LZO.FAQ doc/LZO.TXT
%{_includedir}/lzo/
%{_libdir}/liblzo2.so

%files minilzo
%defattr(-,root,root,-)
%doc minilzo/README.LZO
%{_libdir}/libminilzo.so*

%changelog
* Tue Feb 28 2012 David Hrbáč <david@hrbac.cz> - 2.06-1
- new upstream release
- rfxed for EL6
- added minilzo subpackage
- added patch from Nicolas Chauvet

* Wed Nov 10 2010 Dag Wieers <dag@wieers.com> - 2.04-1
- Updated to release 2.04.

* Sun Aug 12 2007 Dries Verachtert <dries@ulyssis.org> - 2.02-3
- Patch added so it doesn't use an executable stack, thanks to Kenneth Porter.

* Sun Mar 19 2006 Dries Verachtert <dries@ulyssis.org> - 2.02-2
- gcc-c++ buildrequirement added.

* Mon Mar 13 2006 Dag Wieers <dag@wieers.com> - 2.02-1
- Updated to release 2.02.

* Tue May 31 2005 Dag Wieers <dag@wieers.com> - 2.00-1
- Updated to release 2.00.

* Tue Feb  1 2005 Matthias Saou <http://freshrpms.net/> 1.08-4
- Add lzo-1.08-asm.patch to fix asm detection on i386.
- Remove unneeded nasm build dep as build uses only gcc for asm... not sure
  why the configure nasm check is still there, though.

* Wed May 19 2004 Matthias Saou <http://freshrpms.net/> 1.08-3
- Increased release to keep upgrade path.

* Fri Dec 27 2002 Dag Wieers <dag@wieers.com> - 1.08-0
- Updated to 1.08

* Fri Aug 31 2001 Dag Wieers <dag@wieers.com> - 1.04-0
- Made use of macros, made relocatable.

* Thu May 21 1998 Arne Coucheron <arneco@online.no>
- updated to 1.04-1
- using BuildRoot
- using RPM_OPT_FLAGS during make
- using %%{name} and %%{version} macros
- removed Packager: line; use /etc/rpmrc for this if you need it
- using %defattr and %attr macros in filelist. NB! needs rpm 2.5 to build
- simplified the filelist
- removed %pre and added a %postun
- added -q parameter to %setup
- added striping of the library
- removed COPYING file from %doc, copyright is in the header

