# $Id$
# Authority: dag

%define date 20030428
%define real_version 505

Summary: DivX for Linux codec binaries
Name: divx4linux
Version: 5.0.5
Release: 0
License: Distributable
Group: System Environment/Libraries
URL: http://www.divx.com/divx/linux/

Source: http://download.divx.com/divx/divx4linux-std-%{date}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

#ExclusiveArch: i386

%description
This archive includes the binary release of DivX Codec 5.0.5 for x86 Linux.

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n %{name}-%{date}

%install
%{__rm} -rf %{buildroot}
for file in *.so; do
    %{__install} -Dp -m0755 $file %{buildroot}%{_libdir}/$file.0
    %{__ln_s} -f %{_libdir}/$file.0 %{buildroot}%{_libdir}/$file
done

%{__install} -d -m0755 %{buildroot}%{_includedir}
%{__install} -p -m0644 *.h %{buildroot}%{_includedir}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_libdir}/libdivxdecore.so.*
%{_libdir}/libdivxencore.so.*

%files devel
%defattr(-, root, root, 0755)
%doc *.htm
%{_includedir}/decore.h
%{_includedir}/encore2.h
%{_includedir}/portab.h
%{_libdir}/libdivxdecode.so
%{_libdir}/libdivxencode.so

%changelog
* Thu Aug 14 2003 Dag Wieers <dag@wieers.com>
- Updated to release 5.0.5.
- Split into a seperate devel package.

* Sun Jan 19 2003 Dag Wieers <dag@wieers.com>
- Initial package. (using DAR)
