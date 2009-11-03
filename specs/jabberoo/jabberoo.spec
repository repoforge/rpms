# $Id$
# Authority: dag

%define real_name JabberOO

Summary: Library implementing the Jabber instant messaging system
Name: jabberoo
Version: 1.9.4
Release: 1.2%{?dist}
License: GPL
Group: System Environment/Libraries
URL: http://gabber.jabberstudio.org/

Source: http://www.jabberstudio.org/files/gabber/jabberoo-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: pkgconfig >= 0.9, libsigc++-devel

%description
JabberOO is a library implementing the Jabber instant messaging system.

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
%configure \
	--disable-dependency-tracking
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING* NEWS README
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_libdir}/*.a
%exclude %{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/jabberoo/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.9.4-1.2
- Rebuild for Fedora Core 5.

* Tue Jun 29 2004 Dag Wieers <dag@wieers.com> - 1.9.4-1
- Updated to release 1.9.4.

* Thu Feb 19 2004 Dag Wieers <dag@wieers.com> - 1.9.3-0
- Initial package. (using DAR)
