# $Id$

# Authority: dag

# Dists: rhfc1

Summary: A unicode manipulation library.
Name: libunicode
Version: 0.4
Release: 12.0
License: LGPL
Group: System Environment/Libraries

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.pango.org/download/%{name}-%{version}.tar.gz
Patch0: libunicode-0.4-64bit.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: /usr/bin/automake-1.4, /usr/bin/autoconf, libtool

%description
A library to handle unicode strings

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
%patch -p0 -b .64bit

%build
%{__libtoolize} --copy --force
%{__aclocal}-1.4
%{__automake}-1.4
%{__autoconf}

%configure
%{__make} %{?_smp_mflags} \
	RPM_OPT_FLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
#mkdir -p $RPM_BUILD_ROOT%{_prefix}
%makeinstall

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/*.la

%clean
%{__rm} -rf %{buildroot}

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING README TODO
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_bindir}/*
%{_libdir}/*.a
%{_libdir}/*.so
%{_includedir}/*.h

%changelog
* Sat Jan 03 2004 Dag Wieers <dag@wieers.com> - 0.4-12.0
- Initial package. (using DAR)
