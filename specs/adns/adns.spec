# $Id$
# Authority: dag

Summary: Asynchronous-capable resolver library
Name: adns
Version: 1.0
Release: 1
License: GPL
Group: System Environment/Libraries
URL: http://www.chiark.greenend.org.uk/~ian/adns/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.chiark.greenend.org.uk/~ian/adns/ftp/adns-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
adns is a resolver library for C (and C++) programs, and a collection
of useful DNS resolver utilities.

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup
%configure

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d %{buildroot}%{_libdir} \
	%{buildroot}%{_bindir} \
	%{buildroot}%{_includedir}
%makeinstall

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README TODO
%{_bindir}/*
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_libdir}/*.a
%{_includedir}/*.h

%changelog
* Wed Jan 08 2003 Dag Wieers <dag@wieers.com> - 1.0
- Initial package. (using DAR)
