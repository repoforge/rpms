# Authority: dag

Summary: A framework and library for writing RADIUS clients.
Name: radiusclient
Version: 0.3.2
Release: 0
License: Free
Group: Applications/Internet
URL: http://www.cityline.net/~lf/radius/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: ftp://ftp.cityline.net/pub/radiusclient/radiusclient-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

%description
Radiusclient is a framework and library for writing RADIUS clients.
The distribution contains a flexible RADIUS aware login replacement,
a command line program to send RADIUS accounting records and a utility
to query the status of a (Merit) RADIUS server. All these programs
are based on a library which lets you develop your own RADIUS aware
application in less than 50 lines of C code. It is highly portable
and runs at least under Linux, a lot of BSD variants and Solaris. 

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
%makeinstall \
	pkgsysconfdir="%{buildroot}%{_sysconfdir}/radiusclient"

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/*.la

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc BUGS CHANGES COPYRIGHT README* doc/instop.html
%config(noreplace) %{_sysconfdir}/radiusclient/
%{_sbindir}/*
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_libdir}/*.a
%{_libdir}/*.so
%{_includedir}/*.h

%changelog
* Mon Aug 18 2003 Dag Wieers <dag@wieers.com> - 0.3.2-0
- Initial package. (using DAR)
