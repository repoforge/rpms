# $Id: aalib.spec,v 1.1 2004/02/24 16:18:09 thias Exp $

%define real_version 1.4.0

Summary: An ASCII art library.
Name: aalib
Version: 1.4rc5
Release: 4.fr
Group: System Environment/Libraries
License: LGPL
URL: http://aa-project.sourceforge.net/aalib/
Source: http://dl.sf.net/aa-project/%{name}-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-root
Prereq: /sbin/ldconfig /sbin/install-info
Requires: XFree86, ncurses, gpm
BuildRequires: XFree86-devel, ncurses-devel, gpm-devel

%description
AA-lib is a low level graphics library that doesn't require a graphics
device and has no graphics output.  Instead AA-lib replaces those
old-fashioned output methods with a powerful ASCII-art renderer.  The
AA-Project is working on porting important software like DOOM and Quake
to work with AA-lib. If you'd like to help them with their efforts,
you'll also need to install the aalib-devel package.


%package devel
Summary: The static libraries and header files for AA-lib.
Group: Development/Libraries
Requires: %{name} = %{version}, ncurses-devel, gpm-devel

%description devel
The aalib-devel package contains the static libraries and header files
for the AA-lib ASCII art library.  If you'd like to develop programs
using AA-lib, you'll need to install aalib-devel.


%prep
%setup -q -n %{name}-%{real_version}

%build
%configure --with-x --with-curses-driver=yes --with-ncurses
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%makeinstall 
rm -f %{buildroot}%{_infodir}/dir || :

%post
if [ -e %{_infodir}/libaa.info.gz ]; then
    /sbin/install-info %{_infodir}/libaa.info.gz %{_infodir}/dir
fi
/sbin/ldconfig

%preun
if [ -e %{_infodir}/libaa.info.gz ]; then
    /sbin/install-info --delete %{_infodir}/libaa.info.gz %{_infodir}/dir
fi

%postun -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc ANNOUNCE AUTHORS COPYING ChangeLog NEWS
%{_bindir}/aafire
%{_bindir}/aainfo
%{_bindir}/aasavefont
%{_bindir}/aatest
%{_libdir}/*.so.*
%{_infodir}/*.info*
%{_mandir}/man1/*

%files devel
%defattr(-, root, root)
%{_bindir}/aalib-config
%{_libdir}/*.a
%exclude %{_libdir}/*.la
%{_libdir}/*.so
%{_includedir}/*.h
%{_datadir}/aclocal/*.m4
%{_mandir}/man3/*

%changelog
* Sun Nov  2 2003 Matthias Saou <http://freshrpms.net/> 1.4rc5-4.fr
- Rebuild for Fedora Core 1.

* Tue Oct 21 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Added missing ncurses-devel dep to the devel package.

* Mon Mar 31 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Rebuilt for Red Hat Linux 9.
- Exclude .la file.

* Wed Oct 23 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 1.4rc5, doh!

* Thu Sep 26 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Rebuilt for Red Hat Linux 8.0.

* Mon Aug 19 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Dependency fixes.

* Mon Jun 17 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Spec file cleanup and update to 1.4rc4.

* Mon Aug 7 2000 Tim Powers <timp@redhat.com>
- use patch submitted in bug #15193 by bob@ccl.kuleuven.ac.be for sparc only.

* Mon Jul 24 2000 Prospector <prospector@redhat.com>
- rebuilt

* Mon Jul 10 2000 Tim Powers <timp@redhat.com>
- rebuilt

* Fri Jun 2 2000 Tim Powers <timp@redhat.com>
- fix man page location to be FHS compliant
- spec file cleanups for RPM 4.0 macros

* Tue Apr 25 2000 Tim Powers <timp@redhat.com>
- general spec file cleanups. No more useless defines
- use percent configure instead of ./configure
* Thu Dec 23 1999 Tim Powers <timp@redhat.com>
- rebuilt for 6.2

* Tue Jul 6 1999 Tim Powers <timp@redhat.com>
- built package for 6.1

* Wed Apr 21 1999 Michael Maher <mike@redhat.com>
- built package for 6.0

