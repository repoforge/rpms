# $Id$

# Authority: dries

# NeedsCleanup

%define	_name		gift-gnutella
%define	_version	0.0.8
%define _release	1.dries

Summary: gift gnutella plugin
Summary(nl): gnutella plugin voor gift

BuildRoot:	%{_tmppath}/build-%{_name}-%{_version}
Name:		%{_name}
Version:	%{_version}
Release:	%{_release}
License:	GPL
Group:		Development/Libraries
URL: http://apollon.sourceforge.net/
Source: http://dl.sf.net/gift/gift-gnutella-0.0.8.tar.bz2
BuildRequires: gcc, make, gift
Requires: gift

#(d) primscreenshot: 
#(d) screenshotsurl: 
#(d) comment:

%description
Gnutella plugin for gift

%description -l nl
Gnutella plugin voor gift

%prep
%{__rm} -rf "${RPM_BUILD_ROOT}"
%setup

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
/usr/lib/giFT/libGnutella.la
/usr/lib/giFT/libGnutella.so
/usr/share/giFT/Gnutella/Gnutella.conf
/usr/share/giFT/Gnutella/Gnutella.conf.template
/usr/share/giFT/Gnutella/gwebcaches
/usr/share/giFT/Gnutella/hostiles.txt

%changelog
* Mon Dec 29 2003 Dries Verachtert <dries@ulyssis.org> 0.2.1.2-1.dries
- first packaging for Fedora Core 1

