# $Id: _template.spec 765 2004-05-20 17:33:53Z dag $
# Authority: dag

Summary: Meanwhile
Name: meanwhile
Version: 0.2
Release: 1
License: LGPL
Group: Applications/Internet
URL: http://meanwhile.sourceforge.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/meanwhile/meanwhile-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Lotus Sametime Community Client library

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

%clean
%{__rm} -rf %{buildroot}

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%files
%defattr(-, root, root, 0755)
%{_libdir}/*.so.*

%files devel
%{_includedir}/meanwhile/
%{_libdir}/*.a
%{_libdir}/*.so
%exclude %{_libdir}/*.la

%changelog
* Fri Jun 25 2004 Dag Wieers <dag@wieers.com> - 0.2-1
- Initial package. (using DAR)
