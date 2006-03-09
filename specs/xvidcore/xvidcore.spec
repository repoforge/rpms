# $Id$
# Authority: matthias

#define prever beta2
%define somaj  4
%define somin  1

Summary: Free reimplementation of the OpenDivX video codec
Name: xvidcore
Version: 1.1.0
Release: 1%{?prever:.%{prever}}
License: XviD
Group: System Environment/Libraries
URL: http://www.xvid.org/
Source: http://downloads.xvid.org/downloads/xvidcore-%{version}%{?prever:-%{prever}}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: yasm
Provides: lib%{name} = %{version}-%{release}

%description
Free reimplementation of the OpenDivX video codec. You can play OpenDivX
and DivX4 videos with it, as well as encode compatible files.


%package devel
Summary: Static library, headers and documentation of the XviD video codec
Group: Development/Libraries
Requires: %{name} = %{version}
Provides: lib%{name}-devel = %{version}-%{release}
Obsoletes: xvidcore-static <= 1.0.0

%description devel
Free reimplementation of the OpenDivX video codec. You can play OpenDivX
and DivX4 videos with it, as well as encode compatible files.

This package contains the static library, header files and API documentation
needed to build applications that will use the XviD video codec.


%prep
%setup -n %{name}-%{version}%{?prever:-%{prever}}


%build
# CFLAGS recommended in the XviD configure script :
# -fstrength-reduce : Enabled at levels -O2, -O3, -Os.
# -finline-functions
# -freduce-all-givs : No longer present in gcc 4.1, so omit.
# -ffast-math
# -fomit-frame-pointer : Enabled at levels -O, -O2, -O3, -Os.
# We use -Wa,--execstack to work with execshield/selinux. See :
# http://www.crypt.gen.nz/selinux/faq.html
export CFLAGS="%{optflags} -finline-functions -ffast-math -Wa,--execstack"
pushd build/generic
    %configure
    %{__make} %{?_smp_mflags}
popd


%install
%{__rm} -rf %{buildroot}
pushd build/generic
    %makeinstall
popd
# Make .so and .so.x symlinks to the so.x.y file
pushd %{buildroot}%{_libdir}
    %{__ln_s} lib%{name}.so.%{somaj}.%{somin} lib%{name}.so.%{somaj}
    %{__ln_s} lib%{name}.so.%{somaj}.%{somin} lib%{name}.so
popd
# Remove unwanted files from the docs
%{__rm} -f doc/Makefile


%clean
%{__rm} -rf %{buildroot}


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog LICENSE README TODO
%{_libdir}/*.so.*


%files devel
%defattr(-, root, root, 0755)
%doc CodingStyle doc/* examples
%{_includedir}/xvid.h
%{_libdir}/*.a
%{_libdir}/*.so


%changelog
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

