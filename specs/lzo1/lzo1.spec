# $Id$
# Authority: dag
# Upstream: Markus F.X.J. Oberhumer <markus$oberhumer,com>

### EL6 ships with lzo-2.03-3.1.el6

%define real_name lzo

Summary: Portable lossless data compression library
Name: lzo1
Version: 1.08
Release: 5%{?dist}
License: GPL
Group: System Environment/Libraries
URL: http://www.oberhumer.com/opensource/lzo/

Source: http://www.oberhumer.com/opensource/lzo/download/lzo-%{version}.tar.gz
Patch0: lzo1-1.08-asm.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: autoconf
BuildRequires: zlib-devel
Requires: zlib >= 1.0.0

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

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n %{real_name}-%{version}
%patch0 -p0 -b .asm

%build
%configure \
    --disable-dependency-tracking \
    --disable-static \
    --enable-shared
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS BUGS ChangeLog NEWS README THANKS doc/
%{_libdir}/liblzo.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/lzo*.h
%{_libdir}/liblzo.so
%exclude %{_libdir}/liblzo.la

%changelog
* Tue Nov 04 2008 Dag Wieers <dag@wieers.com> - 1.08-5
- Reworked SPEC file.

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

