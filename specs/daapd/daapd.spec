# $Id$

# Authority: dries
# Upstream: <daap$deleet,de>

%define real_version 0.2.4a

# ExcludeDist: fc1 fc2 el3

Summary: Server for DAAP, the digital audio access protocol
Name: daapd
Version: 0.2.4
Release: 0.a.2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://www.deleet.de/projekte/daap/daapd/

Source: http://www.deleet.de/projekte/daap/daapd/daapd-%{real_version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libid3tag-devel, zlib-devel, gcc-c++, howl-devel
# BuildRequires: mpeg4ip-devel

%description
Daapd scans a directory for music files (mp3, aac, uncompressed) and makes
them available via the Apple proprietary protocol DAAP. DAAP clients can
browse the directory and retrieve individual files, either by streaming or
by downloading them.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n daapd-%{real_version}

%build
%{__make} %{?_smp_mflags}
%{__perl} -pi -e 's|/usr/local|%{buildroot}%{_prefix}|g;' libhttpd/src/Makefile.full daaplib/src/makefile
%{__perl} -pi -e 's|/usr/local|%{_prefix}|g;' daapd.rc

%install
%{__rm} -rf %{buildroot}
%{__install} -d %{buildroot}%{_bindir} %{buildroot}%{_libdir} %{buildroot}%{_includedir}
cd libhttpd
%makeinstall
cd ..
cd daaplib/src
%makeinstall
cd ../..
%{__install} -Dp daapd %{buildroot}%{_bindir}/daapd
%{__install} -Dp daapd.8 %{buildroot}%{_mandir}/man8/daapd.8

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING daapd-example.conf daapd.conf daapd.rc FAQ README*
%doc %{_mandir}/man?/*
%{_bindir}/*
#%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/*.h
%{_includedir}/daap
%{_libdir}/*.a
#%{_libdir}/*.so

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.2.4-0.a.2
- Rebuild for Fedora Core 5.

* Thu Jan 06 2005 Dries Verachtert <dries@ulyssis.org> - 0.2.4-0.a
- Initial package.
