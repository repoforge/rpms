# $Id$

Summary: Library for decoding ATSC A/52 (aka AC-3) audio streams
Name: a52dec
Version: 0.7.4
Release: 6
License: GPL
Group: Applications/Multimedia
URL: http://liba52.sourceforge.net/
Source: http://liba52.sf.net/files/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
liba52 is a free library for decoding ATSC A/52 streams. It is released
under the terms of the GPL license. The A/52 standard is used in a
variety of applications, including digital television and DVD. It is
also known as AC-3.


%package devel
Summary: Development header files and static library for liba52
Group: Development/Libraries
Requires: %{name} = %{version}

%description devel
liba52 is a free library for decoding ATSC A/52 streams. It is released
under the terms of the GPL license. The A/52 standard is used in a
variety of applications, including digital television and DVD. It is
also known as AC-3.

These are the header files and static libraries from liba52 that are needed
to build programs that use it.


%prep
%setup


%build
%configure --enable-shared
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
%doc AUTHORS ChangeLog COPYING HISTORY NEWS README TODO doc/liba52.txt
%{_bindir}/*
%{_libdir}/*.so.*
%{_mandir}/man1/*


%files devel
%defattr(-, root, root, 0755)
%{_includedir}/*
%{_libdir}/*.a
%exclude %{_libdir}/*.la
%{_libdir}/*.so


%changelog
* Tue May 18 2004 Matthias Saou <http://freshrpms.net/> 0.7.4-7
- Rebuilt for Fedora Core 2.

* Thu Mar  4 2004 Matthias Saou <http://freshrpms.net/> 0.7.4-6
- Rebuilt.

* Thu Feb 26 2004 Matthias Saou <http://freshrpms.net/> 0.7.4-5
- Added the building of the shared library.

* Sun Nov  2 2003 Matthias Saou <http://freshrpms.net/> 0.7.4-4
- Rebuild for Fedora Core 1.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.
- Exclude .la file.

* Thu Sep 26 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 8.0.
- Added SMP build macro.

* Mon Jul 29 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.7.4.

* Sun Mar 24 2002 Matthias Saou <http://freshrpms.net/>
- Fixed the devel file ownership error.

* Tue Mar 19 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.7.3.

* Mon Dec 17 2001 Matthias Saou <http://freshrpms.net/>
- Update to 0.7.2.

* Mon Oct 29 2001 Matthias Saou <http://freshrpms.net/>
- Spec file cleanup and fixes.

* Thu Sep 20 2001 Martin Norbäck <d95mback@dtek.chalmers.se>
- Added missing .la files
- Building statically

* Thu Sep 20 2001 Martin Norbäck <d95mback@dtek.chalmers.se>
- Initial version

