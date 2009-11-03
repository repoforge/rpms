# $Id$
# Authority: matthias

%{?dtag: %{expand: %%define %dtag 1}}

%define real_version 1.4rc5

%{?el4:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}
%{?el2:%define _without_modxorg 1}
%{?fc4:%define _without_modxorg 1}
%{?fc3:%define _without_modxorg 1}
%{?fc2:%define _without_modxorg 1}
%{?fc1:%define _without_modxorg 1}

Summary: ASCII art library
Name: aalib
Version: 1.4.0
Release: 5%{?dist}
Group: System Environment/Libraries
License: LGPL
URL: http://aa-project.sourceforge.net/aalib/
Source: http://dl.sf.net/aa-project/%{name}-%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires(post): /sbin/ldconfig, /sbin/install-info
Requires(preun): /sbin/install-info
Requires(postun): /sbin/ldconfig
%{!?_without_modxorg:BuildRequires: libXt-devel}
%{?_without_modxorg:BuildRequires: XFree86-devel}
BuildRequires: ncurses-devel, gpm-devel

%description
AA-lib is a low level graphics library that doesn't require a graphics
device and has no graphics output.  Instead AA-lib replaces those
old-fashioned output methods with a powerful ASCII-art renderer.  The
AA-Project is working on porting important software like DOOM and Quake
to work with AA-lib. If you'd like to help them with their efforts,
you'll also need to install the aalib-devel package.


%package devel
Summary: Header files and static library for the ASCII art library
Group: Development/Libraries
Requires: %{name} = %{version}, ncurses-devel, gpm-devel

%description devel
The aalib-devel package contains the static libraries and header files
for the AA-lib ASCII art library.  If you'd like to develop programs
using AA-lib, you'll need to install aalib-devel.


%prep
%setup


%build
%configure \
    --with-x \
    --with-ncurses \
    --with-curses-driver=yes
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -f %{buildroot}%{_infodir}/dir || :


%post
/sbin/ldconfig
if [ -e %{_infodir}/libaa.info.gz ]; then
    /sbin/install-info %{_infodir}/libaa.info.gz %{_infodir}/dir
fi

%preun
if [ -e %{_infodir}/libaa.info.gz ]; then
    /sbin/install-info --delete %{_infodir}/libaa.info.gz %{_infodir}/dir
fi

%postun -p /sbin/ldconfig


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc ANNOUNCE AUTHORS COPYING ChangeLog NEWS
%{_bindir}/aafire
%{_bindir}/aainfo
%{_bindir}/aasavefont
%{_bindir}/aatest
%{_libdir}/*.so.*
%{_infodir}/*.info*
%{_mandir}/man1/*


%files devel
%defattr(-, root, root, 0755)
%{_bindir}/aalib-config
%{_libdir}/*.a
%{_libdir}/*.so
%{_includedir}/*.h
%{_datadir}/aclocal/*.m4
%exclude %{_libdir}/*.la
%{_mandir}/man3/*


%changelog
* Wed Mar 24 2004 Matthias Saou <http://freshrpms.net/> 1.4.0-5
- Minor spec cleanups.
- Removed explicit dependencies for the binay package.

* Sun Nov  2 2003 Matthias Saou <http://freshrpms.net/> 1.4rc5-4
- Rebuild for Fedora Core 1.

* Tue Oct 21 2003 Matthias Saou <http://freshrpms.net/>
- Added missing ncurses-devel dep to the devel package.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.
- Exclude .la file.

* Wed Oct 23 2002 Matthias Saou <http://freshrpms.net/>
- Update to 1.4rc5, doh!

* Thu Sep 26 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 8.0.

* Mon Aug 19 2002 Matthias Saou <http://freshrpms.net/>
- Dependency fixes.

* Mon Jun 17 2002 Matthias Saou <http://freshrpms.net/>
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

