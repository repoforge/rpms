# $Id$
# Authority: matthias

Summary: HERMES pixel format conversion library
Name: Hermes
Version: 1.3.3
Release: 0
License: LGPL
Group: System Environment/Libraries
URL: http://clanlib.org/hermes/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dark.x.dtu.dk/~mbn/clanlib/download/Hermes-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

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
%configure
%{__make} %{_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/*.la

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING FAQ NEWS README TODO*
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%doc docs/api/*.htm docs/api/*.txt
%{_libdir}/*.a
%{_libdir}/*.so
%{_includedir}/Hermes/
#exclude %{_libdir}/*.la

%changelog
* Tue Sep 02 2003 Dag Wieers <dag@wieers.com> - 1.3.3-0
- Taken from Matthias Saou (FreshRPMS) for compatibility.

* Wed Jul  9 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 1.3.3.
- Rebuilt for Red Hat Linux 9 & Yellow Dog Linux 3.0.
- Exclude .la files.

* Thu Oct 24 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Rebuilt for Red Hat Linux 8.0.

* Fri Feb  8 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Spec file cleanup s/Copyright/License/ and fixes.

* Thu Jan  4 2001 Tim Powers <timp@redhat.com>
- fixed bad groups

* Tue Nov 28 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- move to Powertools (was Extrabinge)
- Fix build on alpha
- Don't include INSTALL.DOS in the docs

