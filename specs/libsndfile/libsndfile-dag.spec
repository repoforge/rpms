# Authority: freshrpms
# Upstream: Erik de Castro Lopo <erikd@zip.com.au>

Summary: Library for reading and writing files containing sampled sound.
Name: libsndfile
Version: 1.0.4
Release: 1
License: LGPL
Group: System Environment/Libraries
URL: http://www.zip.com.au/~erikd/libsndfile/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.zip.com.au/~erikd/libsndfile/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


%description
Libsndfile is a C library for reading and writing files containing
sampled sound (such as MS Windows WAV and the Apple/SGI AIFF format)
through one standard library interface.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}, pkgconfig

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

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
%{__rm} -rf %{buildroot}%{_datadir}/octave/

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%doc %{_mandir}/man1/*
%{_bindir}/*
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%doc doc/*.html doc/*.jpg
%{_includedir}/*.h
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
#exclude %{_libdir}/*.la
#exclude %{_datadir}/octave

%changelog
* Tue May 13 2003 Dag Wieers <dag@wieers.com> - 1.0.4-1
- Fixed program-prefix. (for RH73)

* Wed Apr 09 2003 Dag Wieers <dag@wieers.com> - 1.0.4-0
- Initial package. (using DAR)
