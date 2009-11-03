# $Id$
# Authority: matthias
# Upstream: <libdvdplay-devel$videolan,org>

Summary: Library designed for DVD navigation
Name: libdvdplay
Version: 1.0.1
Release: 5%{?dist}
License: GPL
Group: System Environment/Libraries
URL: http://developers.videolan.org/libdvdplay/
Source: http://download.videolan.org/pub/libdvdplay/%{version}/libdvdplay-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: libdvdread >= 0.9.4
BuildRequires: libdvdread-devel >= 0.9.4

%description
A a simple library designed for DVD navigation. It is based on libdvdread and
optionally libdvdcss.


%package devel
Summary: Development files from the libdvdplay DVD navigation library
Group: Development/Libraries
Requires: %{name} = %{version}

%description devel
A a simple library designed for DVD navigation. It is based on libdvdread and
optionally libdvdcss.

You will need to install these development files if you intend to rebuild
programs that use libdvdplay.


%prep
%setup


%build
%configure \
    --disable-static
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall


%clean
%{__rm} -rf %{buildroot}


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING ChangeLog README
%{_libdir}/%{name}.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/*
%exclude %{_libdir}/%{name}.la
%{_libdir}/%{name}.so


%changelog
* Fri Mar 17 2006 Matthias Saou <http://freshrpms.net/> 1.0.1-5
- Disable/remove static library, nothing seems to use it.

* Wed May 19 2004 Matthias Saou <http://freshrpms.net/> 1.0.1-4
- Rebuild for Fedora Core 2.

* Tue Nov 11 2003 Matthias Saou <http://freshrpms.net/> 1.0.1-3
- Rebuild for Fedora Core 1.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.

* Tue Mar 11 2003 Matthias Saou <http://freshrpms.net/>
- Update to 1.0.1.
- Now exclude .la file.

* Tue Feb 10 2003 Matthias Saou <http://freshrpms.net/>
- Rebuild against new libdvdread.

* Tue Feb  4 2003 Matthias Saou <http://freshrpms.net/>
- Initial rpm release, 1.0.0.

