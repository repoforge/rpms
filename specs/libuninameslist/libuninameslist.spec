# Authority: dag

%define rversion 030116

Summary: Library of Unicode annotation data.
Name: libuninameslist
Version: 0.20030713
Release: 0
License: BSD
Group: System Environment/Libraries
URL: http://libuninameslist.sf.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/libuninameslist/%{name}_src-%{rversion}.tgz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

%description
The Unicode consortium provides a file containing annotations
on many unicode characters.
This library contains a compiled version of this file so that
programs can access these data easily.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n %{name}

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall \
	incdir="%{buildroot}%{_includedir}"

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/*.la

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING LICENSE
%_libdir/*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/*.h
%{_libdir}/*.so
#%exclude %{_libdir}/*.la

%changelog
* Mon Jul 28 2003 Dag Wieers <dag@wieers.com> - 0.20030713-0
- Initial package. (using DAR)
