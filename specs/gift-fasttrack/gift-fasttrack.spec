# $Id$

# Authority: dries

# NeedsCleanup

Summary: gift fasttrack plugin
Summary(nl): fasttrack plugin voor gift
Name: gift-fasttrack
Version: 0.8.5
Release: 1
License: GPL
Group: Development/Libraries
URL: http://developer.berlios.de/projects/gift-fasttrack

Source: http://download.berlios.de/gift-fasttrack/giFT-FastTrack-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc, make, gift
Requires: gift

%description
Fasttrack plugin for gift

%description -l nl
Fasttrack plugin voor gift

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
/usr/lib/giFT/libFastTrack.la
/usr/lib/giFT/libFastTrack.so
/usr/share/giFT/FastTrack/FastTrack.conf
/usr/share/giFT/FastTrack/banlist
/usr/share/giFT/FastTrack/nodes

%changelog
* Mon Dec 29 2003 Dries Verachtert <dries@ulyssis.org> 0.8.5-1.dries
- first packaging for Fedora Core 1
