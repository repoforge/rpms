# Authority: freshrpms
Summary: software codec for DV video, used by most digital camcorders
Name: libdv
Version: 0.99
Release: 1
License: GPL
Group: System Environment/Libraries
URL: http://libdv.sourceforge.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: pkgconfig >= 0.9.0, gtk+ >= 1.2.4, glib >= 1.2.4

%description 
The Quasar DV codec (libdv) is a software codec for DV video, the encoding
format used by most digital camcorders, typically those that support the
IEEE 1394 (a.k.a. FireWire or i.Link) interface. Libdv was developed
according to the official standards for DV video: IEC 61834 and SMPTE 314M. 

%package devel
Summary: Development file for programs which use the libdv library
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This is the libraries, include files and other resources that are used to
incorporate libdv into applications.

%prep
%setup

%build
%configure \
	--program-prefix="%{?_program_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/*.la

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING COPYRIGHT NEWS README* TODO
%doc %{_mandir}/man1/*
%{_bindir}/*
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/libdv/
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
#exclude %{_libdir}/*.la

%changelog
* Fri Feb 21 2003 Dag Wieers <dag@wieers.com> - 0.99-1
- Fixed the --program-prefix problem.

* Sun Feb 09 2003 Dag Wieers <dag@wieers.com> - 0.99-0
- Initial package. (using DAR)
