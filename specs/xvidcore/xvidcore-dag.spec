# Authority: freshrpms

Summary: Free reimplementation of the OpenDivX video codec
Name: xvidcore
Version: 0.9.2
Release: 3
License: XVID
Group: System Environment/Libraries
URL: http://www.xvid.org/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://files.xvid.org/downloads/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


Provides: lib%{name} = %{version}-%{release}
Obsoletes: libxvidcore <= 0.9.1, libxvid <= 0.9.1

%ifarch %ix86
BuildRequires: nasm > 0.98
%endif

%description
Free reimplementation of the OpenDivX video codec. You can play OpenDivX
and DivX4 videos with it, as well as encode compatible files.

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

Provides: libxvidcore-devel = %{version}-%{release}, libxvid-devel = %{version}-%{release}
Obsoletes: xvidcore-static, libxvidcore-devel <= 0.9.1, libxvid-devel <= 0.9.1

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build
cd build/generic
%configure \
	--enable-divx4compat
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_includedir} \
                        %{buildroot}%{_libdir}
%makeinstall -C build/generic

%{__install} -m0644 src/divx4.h %{buildroot}%{_includedir}
%{__ln_s} -f libxvidcore.so.* %{buildroot}%{_libdir}/libxvidcore.so
%{__ln_s} -f libxvidcore.so.* %{buildroot}%{_libdir}/libxvid.so
%{__ln_s} -f libxvid.a %{buildroot}%{_libdir}/libxvidcore.a

%post
/sbin/ldconfig &>/dev/null

%postun
/sbin/ldconfig &>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc LICENSE README.txt authors.txt changelog.txt todo.txt
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%doc CodingStyle doc/API.dox doc/README doc/*.pdf doc/*.txt doc/xvid-api-ref/ examples/
%{_includedir}/*.h
%{_libdir}/*.a
%{_libdir}/*.so

%changelog
* Fri Jan 09 2004 Dag Wieers <dag@wieers.com> - 0.9.2-3
- Fixed problem with .so symbolic links. (Erik Sunde)

* Sat Dec 20 2003 Dag Wieers <dag@wieers.com> - 0.9.2-2
- Added extra provides to be compatible with FreshRPMS.

* Tue Sep 16 2003 Dag Wieers <dag@wieers.com> - 0.9.2-1
- Fixed the problematic Obsoletes-tag.

* Sat Aug 23 2003 Dag Wieers <dag@wieers.com> - 0.9.2-0
- Renamed package back to "xvidcore". ;)

* Tue Apr 08 2003 Dag Wieers <dag@wieers.com> - 0.9.1-2
- Renamed package to "libxvidcore".

* Sun Apr 06 2003 Dag Wieers <dag@wieers.com> - 0.9.1-1
- Renamed package to "libxvid".

* Thu Feb 20 2003 Dag Wieers <dag@wieers.com> - 0.9.1-0
- Updated to release 0.9.1.

* Fri Feb 07 2003 Dag Wieers <dag@wieers.com> - 0.9.0-1
- Added link to libxvid.so and libxvid.a.

* Fri Feb 07 2003 Dag Wieers <dag@wieers.com> - 0.9.0-0
- Initial package. (using DAR)
