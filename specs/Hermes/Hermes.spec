# $Id$
# Authority: matthias

Summary: Pixel format conversion library
Name: Hermes
Version: 1.3.3
Release: 4%{?dist}
License: LGPL
Group: System Environment/Libraries
URL: http://clanlib.org/hermes/
Source: http://clanlib.org/download/files/Hermes-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: autoconf

%description
HERMES is a library designed to convert a source buffer with a specified pixel
format to a destination buffer with possibly a different format at the maximum
possible speed.

On x86 and MMX architectures, handwritten assembler routines are taking over
the job and doing it lightning fast.

On top of that, HERMES provides fast surface clearing, stretching and some
dithering. Supported platforms are basically all that have an ANSI C compiler
as there is no platform specific code but those are supported: DOS, Win32
(Visual C), Linux, FreeBSD (IRIX, Solaris are on hold at the moment), some BeOS
support.


%package devel
Summary: Development tools for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}

%description devel
The %{name}-devel package contains the static libraries and header files
needed for development with %{name}.


%prep
%setup


%build
%configure \
    --with-pic
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall


%clean
%{__rm} -rf %{buildroot}


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING ChangeLog FAQ NEWS README TODO*
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%doc docs/api/*.htm docs/api/*.txt
%{_includedir}/*
%{_libdir}/*.a
%exclude %{_libdir}/*.la
%{_libdir}/*.so


%changelog
* Fri Nov  5 2004 Matthias Saou <http://freshrpms.net/> 1.3.3-4
- Added --with-pic configure option, doesn't seem to help much, though.

* Tue May 18 2004 Matthias Saou <http://freshrpms.net/> 1.3.3-3
- Rebuild for Fedora Core 2.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 1.3.3-2
- Rebuild for Fedora Core 1.

* Wed Jul  9 2003 Matthias Saou <http://freshrpms.net/>
- Update to 1.3.3.
- Rebuilt for Red Hat Linux 9 & Yellow Dog Linux 3.0.
- Exclude .la files.

* Thu Oct 24 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 8.0.

* Fri Feb  8 2002 Matthias Saou <http://freshrpms.net/>
- Spec file cleanup s/Copyright/License/ and fixes.

* Thu Jan  4 2001 Tim Powers <timp@redhat.com>
- fixed bad groups

* Tue Nov 28 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- move to Powertools (was Extrabinge)
- Fix build on alpha
- Don't include INSTALL.DOS in the docs

