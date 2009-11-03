# $Id$
# Authority: dag
# Upstream: Phil Howard

# Distcc: 0

Summary: The virtual ring buffer library
Name: vrb
Version: 0.4.0
Release: 0.2%{?dist}
License: LGPL
Group: System Environment/Libraries
URL: http://vrb.slashusr.org/

Source: http://vrb.slashusr.org/vrb-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
The VRB library is a virtual ring buffer. It uses 2 mirrored ranges of
memory to avoid most needs to check for buffer wraparound. This allows
the caller to have direct access to buffer space and buffer data as a
linear contiguous block.

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

%build
./Configure \
	--prefix="%{buildroot}%{_prefix}" \
	--prefixlib="%{buildroot}%{_libdir}"
%{__perl} -pi.orig -e 's|-Wl,-S,-soname,libvrb.so([^ ]*) |-Wl,-S,-soname,libvrb.so.0 |' Makefile
%{__make} %{?_smp_mflags} \
	COPTS="%{optflags} -fPIC"

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_libdir}
%makeinstall

%{__install} -d -m0755 %{buildroot}%{_mandir}/man3/ \
			%{buildroot}%{_includedir}/libvrb/
%{__install} -p -m0644 vrb/man/man3/*.3 %{buildroot}%{_mandir}/man3/
%{__ln_s} -f %{_includedir}/vrb.h %{buildroot}%{_includedir}/libvrb/

%clean
%{__rm} -rf %{buildroot}

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%files
%defattr(-, root, root, 0755)
%doc LICENSE README vrb/doc/ChangeLog
%{_bindir}/*
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%doc %{_mandir}/man?/*
%{_includedir}/*.h
%{_includedir}/libvrb/
%{_libdir}/*.so

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.4.0-0.2
- Rebuild for Fedora Core 5.

* Tue Sep 02 2003 Dag Wieers <dag@wieers.com> - 0.4.0-0
- Initial package. (using DAR)
