# $Id$
# Authority: dag

Summary: Library for dealing with Microsoft ITSS/CHM format files
Name: chmlib
Version: 0.33
Release: 1
License: LGPL
Group: System Environment/Libraries
URL: http://66.93.236.84/~jedwin/projects/chmlib/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://66.93.236.84/~jedwin/projects/chmlib/chmlib-%{version}.tgz
Patch0: chmlib-0.31-morearchs.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libtool

%description
chmlib is a library for dealing with Microsoft ITSS/CHM format files.

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n %{name}
#%patch0 -p1

%build
%{__make} %{?_smp_mflags} all examples \
	CFLAGS="-DCHM_MT -DCHM_USE_PREAD -DCHM_USE_IO64 -L.libs" \
	CC="${CC:-%{__cc}}" \
	LD="${CC:-%{__cc}}" \
	INSTALLPREFIX="%{_prefix}"

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir} \
			%{buildroot}%{_libdir} \
			%{buildroot}%{_includedir}
%makeinstall \
	INSTALLPREFIX="%{buildroot}%{_prefix}"
%{__install} -m0755 *_chmLib chm_http %{buildroot}%{_bindir}

### Fix library symlinks
for lib in $(ls %{buildroot}%{_libdir}); do
        %{__ln_s} -f $lib %{buildroot}%{_libdir}/${lib//%\.?}
        %{__ln_s} -f $lib %{buildroot}%{_libdir}/${lib//%\.?\.?}
done

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING NEWS README
%{_bindir}/*
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%doc ChmLib-ds6.zip
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/*.so
%{_includedir}/*.h

%changelog
* Wed Jun 02 2004 Dag Wieers <dag@wieers.com> - 0.33-1
- Updated to release 0.33.

* Mon Feb 09 2004 Dag Wieers <dag@wieers.com> - 0.31-0
- Initial package. (using DAR)
