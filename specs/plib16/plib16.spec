# $Id$
# Authority: matthias

Summary: Set of portable libraries especially useful for games
Name: plib16
Version: 1.6.0
Release: 0%{?dist}
License: LGPL
Group: System Environment/Libraries
URL: http://plib.sourceforge.net/
Source: http://plib.sourceforge.net/dist/plib-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc-c++, Mesa-devel, freeglut-devel, libpng-devel
Provides: plib = %{version}-%{release}

%description
This is a set of OpenSource (LGPL) libraries that will permit programmers
to write games and other realtime interactive applications that are 100%
portable across a wide range of hardware and operating systems. Here is
what you need - it's all free and available with LGPL'ed source code on
the web. All of it works well together.


%package devel
Summary: Set of portable libraries especially useful for games
Group: Development/Libraries
Provides: plib-devel = %{version}-%{release}

%description devel
This is a set of OpenSource (LGPL) libraries that will permit programmers
to write games and other realtime interactive applications that are 100%
portable across a wide range of hardware and operating systems. Here is
what you need - it's all free and available with LGPL'ed source code on
the web. All of it works well together.


%prep
%setup -n plib-%{version}


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}


%clean
%{__rm} -rf %{buildroot}


%files devel
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING ChangeLog NOTICE README
%{_includedir}/*
%{_libdir}/*.a


%changelog
* Fri Jul 23 2004 Matthias Saou <http://freshrpms.net/> 1.6.0-0
- Fork off as plib16 for compatibility, as some apps require 1.6 not newer.
- Downgrade to 1.6.

* Thu Jul 15 2004 Matthias Saou <http://freshrpms.net/> 1.8.3-3
- Only build a devel package now as all files are headers and static libs.

* Wed May 19 2004 Matthias Saou <http://freshrpms.net/> 1.8.3-2
- Rebuild for Fedora Core 2.

* Thu Apr 15 2004 Matthias Saou <http://freshrpms.net/> 1.8.3-1
- Update to 1.8.3.

* Tue Nov 11 2003 Matthias Saou <http://freshrpms.net/> 1.6.0-3
- Rebuild for Fedora Core 1.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.

* Wed Dec  4 2002 Matthias Saou <http://freshrpms.net/>
- Update to 1.6.0.

* Wed Jun 20 2001 Matthias Saou <http://freshrpms.net/>
- Initial RPM release.

