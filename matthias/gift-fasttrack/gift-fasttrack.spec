# $Id: gift-fasttrack.spec,v 1.1 2004/03/01 15:41:09 driesve Exp $

# Authority: dries

# NeedsCleanup

%define	_name		gift-fasttrack
%define	_version	0.8.5
%define _release	1.dries

Summary: gift fasttrack plugin
Summary(nl): fasttrack plugin voor gift

BuildRoot:	%{_tmppath}/build-%{_name}-%{_version}
Name:		%{_name}
Version:	%{_version}
Release:	%{_release}
License:	GPL
Group:		Development/Libraries
URL: http://developer.berlios.de/projects/gift-fasttrack
Source: http://download.berlios.de/gift-fasttrack/giFT-FastTrack-0.8.5.tar.gz
BuildRequires: gcc, make, gift
Requires: gift

#(d) primscreenshot: 
#(d) screenshotsurl: 
#(d) comment:

%description
Fasttrack plugin for gift

%description -l nl
Fasttrack plugin voor gift

%prep
%{__rm} -rf "${RPM_BUILD_ROOT}"
%setup -n giFT-FastTrack-0.8.5

%build
%configure
make

%install
echo RPM_BUILD_ROOT is $RPM_BUILD_ROOT
export DESTDIR=$RPM_BUILD_ROOT
make install-strip

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

