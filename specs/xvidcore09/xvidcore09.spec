# $Id: xvidcore09.spec 130 2004-03-17 10:51:35Z dude $
# Authority: matthias

Summary: Free reimplementation of the OpenDivX video codec
Name: xvidcore09
Version: 0.9.2
Release: 5
License: XviD
Group: System Environment/Libraries
URL: http://www.xvid.org/
Source: http://files.xvid.org/downloads/xvidcore-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
%ifarch %ix86 ia64
BuildRequires: nasm
%endif

%description
Free reimplementation of the OpenDivX video codec. You can play OpenDivX
and DivX4 videos with it, as well as encode compatible files.

%prep
%setup -n xvidcore-%{version}

%build
pushd build/generic
    %configure
    make %{?_smp_mflags}
popd

%install
%{__rm} -rf %{buildroot}
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_includedir}
pushd build/generic
    %makeinstall
popd

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%doc LICENSE README.txt authors.txt changelog.txt todo.txt
%exclude %{_includedir}/xvid.h
%exclude %{_libdir}/*.a
%{_libdir}/*.so*

%changelog
* Thu Feb 26 2004 Matthias Saou <http://freshrpms.net/> 0.9.2-5.fr
- Removed the static sub-package headers from the spec file.

* Mon Jan 12 2004 Matthias Saou <http://freshrpms.net/> 0.9.2-4.fr
- Fork as xvidcore09 for binary compatibility.

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

