# $Id$

# Authority: dries

# NeedsCleanup

Summary: gift fasttrack plugin
Name: gift-fasttrack
Version: 0.8.5
Release: 1
License: GPL
Group: Development/Libraries
URL: http://developer.berlios.de/projects/gift-fasttrack

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://download.berlios.de/gift-fasttrack/giFT-FastTrack-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc, make, gift, pkgconfig
Requires: gift

%description
Fasttrack plugin for gift

%prep
%setup -n giFT-FastTrack-0.8.5

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
make install-strip \
	DESTDIR="%{buildroot}"

%files
%defattr(-,root,root)
%doc README AUTHORS ChangeLog COPYING NEWS TODO
%{_libdir}/giFT/libFastTrack.la
%{_libdir}/giFT/libFastTrack.so
%{_datadir}/giFT/FastTrack/FastTrack.conf
%{_datadir}/giFT/FastTrack/banlist
%{_datadir}/giFT/FastTrack/nodes

%changelog
* Mon Dec 29 2003 Dries Verachtert <dries@ulyssis.org> 0.8.5-1
- first packaging for Fedora Core 1
