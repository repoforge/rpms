# $Id$
# Authority: yury
# Upstream: Jari "Rakshasa" Sundell <sundell,software$gmail,com>

### Only build for RHEL5,6 for newer rtorrent
# ExcludeDist: el2 el3 el4

Name: libtorrent
License: GPLv2+
Group: System Environment/Libraries
Version: 0.13.2
Release: 1%{?dist}
Summary: BitTorrent library with a focus on high performance & good code
URL: http://libtorrent.rakshasa.no/
Source0: http://libtorrent.rakshasa.no/downloads/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: pkgconfig
BuildRequires: openssl-devel
BuildRequires: libsigc++20-devel

Requires: libsigc++20

%description
LibTorrent is a BitTorrent library written in C++ for *nix, with a focus 
on high performance and good code. The library differentiates itself 
from other implementations by transfering directly from file pages to 
the network stack. On high-bandwidth connections it is able to seed at 
3 times the speed of the official client.

%package devel
Summary: Libtorrent development environment
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
Header and library definition files for developing applications
with the libtorrent libraries.

%prep
%setup

%build

# avoid gcc-4.1 bug
%ifarch i386
    %{?el5:export CFLAGS="$CFLAGS -pthread -march=i486"}
    %{?el5:export CXXFLAGS="$CXXFLAGS -pthread -march=i486"}
%endif

%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}
%{__rm} -f %{buildroot}/%{_libdir}/*.la

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING INSTALL README NEWS
%{_libdir}/libtorrent.so.*

%files devel
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/libtorrent.pc
%{_includedir}/torrent
%{_libdir}/*.so


%changelog
* Mon May 07 2012 Denis Fateyev <denis@fateyev.com> - 0.13.2-1
- libtorrent 0.13.2 version

* Fri Mar 30 2012 Denis Fateyev <denis@fateyev.com> - 0.12.9-2
- Some fixes for unification in spec.

* Mon Aug 01 2011 Dag Wieers <dag@wieers.com> - 0.12.9-1
- Updated to release 0.12.9.

* Tue Dec 15 2009 Yury V. Zaytsev <yury@shurup.com> - 0.12.6-1
- Updated to release 0.12.6.

* Tue Oct 27 2009 Steve Huff <shuff@vecna.org> - 0.12.5-1
- Updated to release 0.12.5.

* Thu Jan 1 2009 Dries Verachtert <dries@ulyssis.org> - 0.12.4-1
- Updated to release 0.12.4.

* Tue Jan 29 2008 Dries Verachtert <dries@ulyssis.org> - 0.12.0-1
- Updated to release 0.12.0.

* Mon Dec 17 2007 Dries Verachtert <dries@ulyssis.org> - 0.11.9-1
- Updated to release 0.11.9.

* Fri Aug 03 2007 Dries Verachtert <dries@ulyssis.org> - 0.11.6-1
- Updated to release 0.11.6.

* Wed Apr 25 2007 Dag Wieers <dag@wieers.com> - 0.11.4-1
- Updated to release 0.11.4.

* Mon Jan 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.11.1-1
- Updated to release 0.11.1.

* Fri Dec 15 2006 Dries Verachtert <dries@ulyssis.org> - 0.11.0-1
- Updated to release 0.11.0.

* Mon Nov 13 2006 Dag Wieers <dag@wieers.com> - 0.10.4-1
- Updated to release 0.10.4.

* Sun Nov 12 2006 Dries Verachtert <dries@ulyssis.org> - 0.10.3-1
- Updated to release 0.10.3.

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
