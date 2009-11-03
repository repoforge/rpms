# $Id$
# Authority: matthias

Summary: Library for manipulating ID3v1 and ID3v2 tags
Name: id3lib
Version: 3.8.3
Release: 7%{?dist}
License: LGPL
Group: System Environment/Libraries
Source: http://dl.sf.net/id3lib/id3lib-%{version}.tar.gz
URL: http://id3lib.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc-c++, zlib-devel

%description
This package provides a software library for manipulating ID3v1 and ID3v2 tags.
It provides a convenient interface for software developers to include
standards-compliant ID3v1/2 tagging capabilities in their applications.
Features include identification of valid tags, automatic size conversions,
(re)synchronisation of tag frames, seamless tag (de)compression, and optional
padding facilities.


%package devel
Summary: Headers and libraries for developing programs that will use id3lib
Group: Development/Libraries
Requires: %{name} = %{version}, libstdc++-devel, zlib-devel

%description devel
This package contains the headers that programmers will need to develop
applications which will use id3lib, the software library for ID3v1 and ID3v2
tag manipulation.


%prep
%setup


%build
export LDFLAGS="-lstdc++ -lz ${LDFLAGS}"
%configure --enable-debug="no"
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall
# Clean docs for inclusion
%{__rm} -f doc/{Doxyfile*,Makefile*,*.in}
%{__rm} -rf examples/{Makefile*,.deps/,.libs/,*.o}
%{__rm} -rf examples/{id3convert,id3cp,id3info,id3tag}


%clean
%{__rm} -rf %{buildroot}


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING ChangeLog HISTORY NEWS README THANKS TODO
%{_bindir}/*
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%doc doc/ examples/
%{_includedir}/*
%exclude %{_libdir}/*.la
%{_libdir}/*.a
%{_libdir}/*.so


%changelog
* Fri Nov  5 2004 Matthias Saou <http://freshrpms.net/> 3.8.3-7
- Removed binary stuff from the included examples, leave only source.

* Mon Aug 16 2004 Matthias Saou <http://freshrpms.net/> 3.8.3-7
- Fix linking problem at last by overriding LDFLAGS manually, thanks to
  Pedro Lopez for the tip.

* Tue May 18 2004 Matthias Saou <http://freshrpms.net/> 3.8.3-6
- Rebuild for Fedora Core 2.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 3.8.3-6
- Rebuild for Fedora Core 1.

* Thu Oct 30 2003 Matthias Saou <http://freshrpms.net/> 3.8.3-5
- Also added gcc-c++, libstdc++-devel, zlib-devel deps to the devel package.

* Sat Oct  4 2003 Matthias Saou <http://freshrpms.net/>
- Added gcc-c++, libstdc++-devel and zlib-devel dependencies.

* Tue Apr 15 2003 Matthias Saou <http://freshrpms.net/>
- Move binary files to the main package.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Update to 3.8.3.
- Rebuilt for Red Hat Linux 9.
- Exclude .la file.

* Wed Dec 25 2002 Ville Skyttä <ville.skytta at iki.fi> 3.8.2-fr1
- Update to 3.8.2 (GCC 3.2 patch no longer needed).

* Tue Oct 08 2002 Erich Schraer <erich@wubios.wustl.edu>
- Added patch id3lib-3.8.0-gc-3.2.patch.

* Fri Aug 30 2002 Matthias Saou <http://freshrpms.net/>
- Spec file cleanup for Red Hat Linux.
- Removed examples and docs sub-packages (both are in devel now).

* Sat Sep 08 2001 Cedric Tefft <cedric@earthling.net> 3.8.0pre2
- Version 3.8.0pre2

* Mon Nov 20 2000 Scott Thomas Haug <scott@id3.org> 3.8.0pre1-1
- Version 3.8.0pre1

* Thu Sep 14 2000 Scott Thomas Haug <scott@id3.org> 3.7.13-1
- Version 3.7.13

* Sat Aug 26 2000 Scott Thomas Haug <scott@id3.org> 3.7.12-2
- Removed -mpreferred-stack-boundary option from RPM_OPT_FLAGS for RedHat 6.2

* Fri Jul 07 2000 Scott Thomas Haug <scott@id3.org> 3.7.12-1
- Version 3.7.12

* Fri Jul 05 2000 Scott Thomas Haug <scott@id3.org> 3.7.11-1
- Version 3.7.11

* Fri Jun 23 2000 Scott Thomas Haug <scott@id3.org> 3.7.10-1
- Version 3.7.10

* Wed May 24 2000 Scott Thomas Haug <scott@id3.org> 3.7.9-1
- Version 3.7.9

* Wed May 10 2000 Scott Thomas Haug <scott@id3.org> 3.7.8-1
- Version 3.7.8

* Wed May 10 2000 Scott Thomas Haug <scott@id3.org> 3.7.7-1
- Version 3.7.7

* Wed May 03 2000 Scott Thomas Haug <scott@id3.org> 3.7.6-1
- Version 3.7.6

* Fri Apr 28 2000 Scott Thomas Haug <scott@id3.org> 3.7.5-1
- Version 3.7.5

* Wed Apr 26 2000 Scott Thomas Haug <scott@id3.org> 3.7.4-1
- Version 3.7.4

* Mon Apr 24 2000 Scott Thomas Haug <scott@id3.org> 3.7.3-1
- Version 3.7.3
- Added explicit RPM_OPT_FLAGS def based on arch, since -fno-exceptions and
  -fno-rtti are part of the default flags in rpmrc and we need both exceptions
  and rtti (exceptions uses rtti)

* Fri Apr 21 2000 Scott Thomas Haug <scott@id3.org> 3.7.2-1
- Version 3.7.2
- More conditional blocks for noarch
- More thorough cleaning of files for documentation
- Updated html directory

* Thu Apr 20 2000 Scott Thomas Haug <scott@id3.org> 3.7.1-2
- Fixed date of changelog entry for 3.7.1-1
- Added conditional blocks so docs only get built for noarch target

* Wed Apr 19 2000 Scott Thomas Haug <scott@id3.org> 3.7.1-1
- Version 3.7.1
- Removed zlib-devel requirement from devel
- Added doc package to distribute documentation
- Added examples package to distribute binary examples (id3tag, id3info, ...)
- Moved doc/ and examples/ source files from devel to doc package

* Mon Apr 17 2000 Scott Thomas Haug <scott@id3.org> 3.7.0-1
- First (s)rpm build

