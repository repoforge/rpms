# $Id: xvidcore.spec,v 1.2 2004/03/04 00:28:34 thias Exp $

%define prever rc3

Summary: Free reimplementation of the OpenDivX video codec
Name: xvidcore
Version: 1.0.0
Release: %{?prever:0.%{prever}.}1.fr
License: XviD
Group: System Environment/Libraries
URL: http://www.xvid.org/
Source: http://files.xvid.org/downloads/%{name}-%{version}%{?prever:-%{prever}}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
%ifarch %ix86 ia64 x86_64
BuildRequires: nasm
%endif
Provides: lib%{name} = %{version}-%{release}
Provides: lib%{name}-devel = %{version}-%{release}
Provides: %{name}-devel = %{version}-%{release}

%description
Free reimplementation of the OpenDivX video codec. You can play OpenDivX
and DivX4 videos with it, as well as encode compatible files.


%package static
Summary: Static library and API documentation of the XviD video codec
Group: Development/Libraries
Requires: %{name} = %{version}

%description static
Static library and API documentation of the XviD video codec.


%prep
%setup -q -n %{name}-%{version}%{?prever:-%{prever}}


%build
pushd build/generic
    %configure
    make %{?_smp_mflags}
popd


%install
rm -rf %{buildroot}
pushd build/generic
    %makeinstall
popd
# Make a .so symlink to the so.x.x file
pushd %{buildroot}%{_libdir}
    ln -s lib%{name}.so* lib%{name}.so
popd
# Remove unwanted files from the docs
rm -f doc/Makefile


%clean
rm -rf %{buildroot}


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-, root, root)
%doc AUTHORS ChangeLog LICENSE README TODO
%{_includedir}/*
%{_libdir}/*.so*


%files static
%defattr(-, root, root)
%doc CodingStyle doc/* examples
%{_libdir}/*.a


%changelog
* Thu Mar  4 2004 Matthias Saou <http://freshrpms.net/> 1.0.0-0.rc3.1.fr
- Update to 1.0.0-rc3.

* Wed Feb 11 2004 Matthias Saou <http://freshrpms.net/> 1.0.0-0.rc2.1.fr
- Update to 1.0.0-rc2.

* Sun Jan 11 2004 Matthias Saou <http://freshrpms.net/> 1.0.0-0.beta3.1.fr
- Update to 1.0.0-beta3, quite a few spec file changes to match.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 0.9.2-3.fr
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

