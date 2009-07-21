# $Id$
# Authority: matthias

%{?dtag: %{expand: %%define %dtag 1}}

%{?fc1:%define _without_selinux 1}
%{?el3:%define _without_selinux 1}
%{?rh9:%define _without_selinux 1}
%{?rh7:%define _without_selinux 1}
%{?el2:%define _without_selinux 1}

Summary: Free reimplementation of the OpenDivX video codec
Name: xvidcore
Version: 1.2.2
Release: 1
License: XviD
Group: System Environment/Libraries
URL: http://www.xvid.org/

Source: http://downloads.xvid.org/downloads/xvidcore-%{version}.tar.bz2
Patch0: xvidcore-1.1.0-verbose-build.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: yasm
%{!?_without_selinux:BuildRequires: prelink}
Obsoletes: libxvidcore <= %{version}-%{release}
Provides: libxvidcore = %{version}-%{release}

%description
Free reimplementation of the OpenDivX video codec. You can play OpenDivX
and DivX4 videos with it, as well as encode compatible files.

%package devel
Summary: Static library, headers and documentation of the XviD video codec
Group: Development/Libraries
Requires: %{name} = %{version}

Obsoletes: xvidcore-static <= 1.0.0
Obsoletes: libxvidcore-devel <= %{version}-%{release}
Provides: libxvidcore-devel = %{version}-%{release}

%description devel
Free reimplementation of the OpenDivX video codec. You can play OpenDivX
and DivX4 videos with it, as well as encode compatible files.

This package contains the static library, header files and API documentation
needed to build applications that will use the XviD video codec.

%prep
%setup -n %{name}
%patch0 -p1 -b .verbose-build

%build
cd build/generic/
%configure --disable-static
%{__make} %{?_smp_mflags}
cd -

%install
%{__rm} -rf %{buildroot}
cd build/generic/
%{__make} install DESTDIR="%{buildroot}"
cd -
### Make .so and .so.x symlinks to the so.x.y file, +x to get proper stripping
%{__ln_s} -f libxvidcore.so.4.2 %{buildroot}%{_libdir}/libxvidcore.so.4
%{__ln_s} -f libxvidcore.so.4.2 %{buildroot}%{_libdir}/libxvidcore.so
%{__chmod} +x %{buildroot}%{_libdir}/libxvidcore.so.4.2
### Remove unwanted files from the docs
%{__rm} -f doc/Makefile
### Clear executable stack flag bit (should not be needed)
#execstack -c %{buildroot}%{_libdir}/*.so.*.* || :

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog LICENSE README TODO
%{_libdir}/libxvidcore.so.*

%files devel
%defattr(-, root, root, 0755)
%doc CodingStyle doc/* examples/
%{_includedir}/xvid.h
%{_libdir}/libxvidcore.so
%exclude %{_libdir}/libxvidcore.a

%changelog
* Tue Jul 21 2009 Dag Wieers <dag@wieers.com> - 1.2.2-1
- Updated to release 1.2.2.

* Wed Dec 17 2008 Dag Wieers <dag@wieers.com> - 1.2.1-1
- Updated to release 1.2.1.

* Tue Dec 02 2008 Dag Wieers <dag@wieers.com> - 1.2.0-1
- Updated to release 1.2.0.

* Fri Jun 29 2007 Dag Wieers <dag@wieers.com> - 1.1.3-1
- Updated to release 1.1.3.

* Wed Nov  8 2006 Matthias Saou <http://freshrpms.net/> 1.1.2-1
- Update to 1.1.2.
- Chmod +x the shared library to get it stripped and proper debuginfo created.

* Wed May 17 2006 Matthias Saou <http://freshrpms.net/> 1.1.0-3
- Clear executable stack flag bit from the library (should not be needed).

* Fri Mar 17 2006 Matthias Saou <http://freshrpms.net/> 1.1.0-2
- Release bump to drop the disttag number in FC5 build.
- Note that the execshield/selinux seems to still not be fixed. Help welcome.

* Thu Mar  9 2006 Matthias Saou <http://freshrpms.net/> 1.1.0-1
- Update to 1.1.0 final.
- Increase somin from 0 to 1 (we now have libxvidcore.so.4.1).
- Add -Wa,--execstack to CFLAGS to work with execshield/selinux.
- Add relevant CFLAGS from the XviD defaults.
- Require yasm on all archs, since it's also available on PPC (maybe not used,
  though).
- Update Source URL.

* Sun Apr 17 2005 Matthias Saou <http://freshrpms.net/> 1.1.0-0.1.beta2
- Update to 1.1.0-beta2.

* Fri Jan 28 2005 Matthias Saou <http://freshrpms.net/> 1.1.0-0.beta1.1
- Fork off the devel branch.
- Switch from using nasm to yasm for improved x86_64 and ppc support.

* Fri Jan 28 2005 Matthias Saou <http://freshrpms.net/> 1.0.3-1
- Update to 1.0.3.

* Fri Nov  5 2004 Matthias Saou <http://freshrpms.net/> 1.0.2-2
- Further manually symlink libs to get things back to "ldconfig style".

* Wed Oct 13 2004 Matthias Saou <http://freshrpms.net/> 1.0.2-1
- Update to 1.0.2.

* Tue Jun  8 2004 Matthias Saou <http://freshrpms.net/> 1.0.1-1
- Update to 1.0.1.

* Mon May 17 2004 Matthias Saou <http://freshrpms.net/> 1.0.0-1
- Update to 1.0.0 final.
- Change the -static sub-package to -devel.
- Updated descriptions.

* Wed May  5 2004 Matthias Saou <http://freshrpms.net/> 1.0.0-0.rc4.1
- Update to 1.0.0-rc4.

* Thu Mar  4 2004 Matthias Saou <http://freshrpms.net/> 1.0.0-0.rc3.1
- Update to 1.0.0-rc3.

* Wed Feb 11 2004 Matthias Saou <http://freshrpms.net/> 1.0.0-0.rc2.1
- Update to 1.0.0-rc2.

* Sun Jan 11 2004 Matthias Saou <http://freshrpms.net/> 1.0.0-0.beta3.1
- Update to 1.0.0-beta3, quite a few spec file changes to match.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 0.9.2-3
- Rebuild for Fedora Core 1.
- Added libxvidcore provides for compatibility.

* Mon Sep 15 2003 Matthias Saou <http://freshrpms.net/>
- Added a .so symlink to the lib for proper detection.

* Thu Aug  7 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.9.2.
- The .so file has now a version appended.

* Mon Apr  7 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.9.1.
- Build and install changes since there is now a nice configure script.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.

* Wed Jan 29 2003 Matthias Saou <http://freshrpms.net/>
- Fixed the location of the .h files... doh!

* Sun Jan 12 2003 Matthias Saou <http://freshrpms.net/>
- Remove the decore.h and encore2.h inks as divx4linux 5.01 will provide them.
- Rename -devel to -static as it seems more logic.

* Fri Dec 27 2002 Matthias Saou <http://freshrpms.net/>
- Initial RPM release.

