# $Id$
# Authority: dag
# Upstream: Ian Jackson <adns-maint$chiark,greenend,org,uk>

Summary: Asynchronous-capable resolver library
Name: adns
Version: 1.2
Release: 1%{?dist}
License: GPL
Group: System Environment/Libraries
URL: http://www.chiark.greenend.org.uk/~ian/adns/

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

### FIXME: Adapt buildtools to autotool directories. (Please fix upstream)
%{__perl} -pi.orig -e 's|\$\(lib_dir\)|\$(libdir)|g' Makefile* */Makefile*

### FIXME: Fix conflicting types. (Please fix upstream)
%{__perl} -pi.orig -e 's|adns_queryflags flags,|parsedomain_flags flags,|g' src/parse.c

%build
%configure
%{__make} %{?_smp_mflags} \
	XCFLAGS="-fPIC -fomit-frame-pointer -DPIC"

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_libdir} \
		%{buildroot}%{_bindir} \
		%{buildroot}%{_includedir}
%makeinstall

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README TODO
%{_bindir}/adns*
%{_libdir}/libadns.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/adns.h
%{_libdir}/libadns.a
%{_libdir}/libadns.so

%changelog
* Mon Aug 14 2006 Dag Wieers <dag@wieers.com> - 1.2-1
- Updated to release 1.2.

* Tue Nov 10 2004 Dag Wieers <dag@wieers.com> - 1.1-1
- Updated to release 1.1.

* Wed Jan 08 2003 Dag Wieers <dag@wieers.com> - 1.0-1
- Initial package. (using DAR)
