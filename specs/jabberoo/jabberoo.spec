# $Id$

# Authority: dag

%define rname JabberOO

Summary: Library implementing the Jabber instant messaging system.
Name: jabberoo
Version: 1.9.3
Release: 0
License: GPL
Group: System Environment/Libraries
URL: http://gabber.jabberstudio.org/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.jabberstudio.org/files/gabber/jabberoo-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: libsigc++-devel

%description
JabberOO is a library implementing the Jabber instant messaging system.

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
%configure \
	--disable-dependency-tracking
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/*.la

%post
/sbin/ldconfig &>/dev/null

%postun
/sbin/ldconfig &>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING* NEWS README
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/jabberoo/

%changelog
* Thu Feb 19 2004 Dag Wieers <dag@wieers.com> - 1.9.3-0
- Initial package. (using DAR)
