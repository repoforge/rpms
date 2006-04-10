# $Id$
# Authority: dries

Summary: BitTorrent library
Name: libtorrent
Version: 0.9.0
Release: 1
License: GPL
Group: Development/Libraries
URL: http://libtorrent.rakshasa.no

Source: http://libtorrent.rakshasa.no/downloads/libtorrent-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, pkgconfig, openssl-devel, libsigc++20-devel

%description
LibTorrent is a BitTorrent library written in C++ for Unix. It is designed to
avoid the redundant buffers and data copying that most (all?) other BitTorrent
implementations suffer from. The library is single-threaded and the client
handles the select loop. An interactive ncurses client is included as an
example.

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

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%{_libdir}/libtorrent.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/torrent/
#%{_libdir}/libtorrent.a
%{_libdir}/libtorrent.so
%exclude %{_libdir}/*.la
%{_libdir}/pkgconfig/libtorrent.pc

%changelog
* Mon Apr 10 2006 Dries Verachtert <dries@ulyssis.org> - 0.9.0-1
- Updated to release 0.9.0.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.8.5-1.2
- Rebuild for Fedora Core 5.

* Thu Mar 02 2006 Dries Verachtert <dries@ulyssis.org> - 0.8.5-1
- Updated to release 0.8.5.

* Thu Jan 12 2006 Dries Verachtert <dries@ulyssis.org> - 0.8.2-1
- Updated to release 0.8.2.

* Wed Dec 21 2005 Dries Verachtert <dries@ulyssis.org> - 0.8.1-1
- Initial package.
