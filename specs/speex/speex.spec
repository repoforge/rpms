# $Id$

Summary: An open-source, patent-free speech codec
Name: speex
Version: 1.0.3
Release: 1.fr
License: BSD
Group: System Environment/Libraries
URL: http://www.speex.org/
Source: http://www.speex.org/download/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Provides: libspeex = %{version}-%{release}
Obsoletes: libspeex <= 1.0.0
Requires: libogg
BuildRequires: libogg-devel

%description
Speex is a patent-free audio codec designed especially for voice (unlike 
Vorbis which targets general audio) signals and providing good narrowband 
and wideband quality. This project aims to be complementary to the Vorbis
codec.


%package devel
Summary: Speex development files.
Group: Development/Libraries
Provides: libspeex-devel = %{version}-%{release}
Requires: %{name} = %{version}

%description devel
Speex development files.


%prep
%setup -q

%build
export CFLAGS='%{optflags} -DRELEASE'
%configure --enable-shared --enable-static
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc COPYING AUTHORS ChangeLog NEWS README doc/manual.pdf
%{_bindir}/*
%{_libdir}/*.so.*
%{_mandir}/man1/*

%files devel
%defattr(-, root, root)
%{_includedir}/*
%{_libdir}/*.a
%exclude %{_libdir}/*.la
%{_libdir}/*.so

%changelog
* Thu Nov 20 2003 Matthias Saou <http://freshrpms.net/> 1.0.3-1.fr
- Update to 1.0.3.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 1.0.2-2.fr
- Rebuild for Fedora Core 1.

* Thu Sep 25 2003 Matthias Saou <http://freshrpms.net/>
- Update to 1.0.2.

* Wed Aug 13 2003 Matthias Saou <http://freshrpms.net/>
- Added libspeex provides and obsoletes.

* Thu Jul 24 2003 Matthias Saou <http://freshrpms.net/>
- Update (at last!) to 1.0.1 and rebuilt with mach.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.

* Mon Mar 24 2003 Matthias Saou <http://freshrpms.net/>
- Spec file cleanup.
- Now exclude .la file.

* Thu Oct 03 2002 Jean-Marc Valin 
- Added devel package inspired from PLD spec file

* Tue Jul 30 2002 Fredrik Rambris <boost@users.sourceforge.net> 0.5.2
- Added buildroot and docdir and ldconfig. Makes it builadble by non-roots
  and also doesn't write to actual library paths when building.

