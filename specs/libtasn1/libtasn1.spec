# Authority: dag

Summary: This is the ASN.1 library used in GNUTLS.
Name: libtasn1
Version: 0.2.5
Release: 0
License: LGPL
Group: System Environment/Libraries
URL: http://www.gnu.org/software/gnutls/download.html

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: ftp://ftp.gnutls.org/pub/gnutls/libtasn1/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: bison

%description
This is the ASN.1 library used in GNUTLS.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

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
%doc AUTHORS ChangeLog COPYING* NEWS README THANKS
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%doc doc/TODO doc/*.ps
%{_includedir}/*.h
%{_libdir}/*.a
%{_libdir}/*.so

%changelog
* Wed Dec 03 2003 Dag Wieers <dag@wieers.com> - 0.2.5-0
- Initial package. (using DAR)
