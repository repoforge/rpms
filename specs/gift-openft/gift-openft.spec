# $Id: gift-openft.spec,v 1.1 2004/03/01 15:41:09 driesve Exp $

# Authority: dries

# NeedsCleanup

%define	_name		gift-openft
%define	_version	0.2.1.2
%define _release	1.dries

Summary: gift openft plugin
Summary(nl): openft plugin voor gift

BuildRoot:	%{_tmppath}/build-%{_name}-%{_version}
Name:		%{_name}
Version:	%{_version}
Release:	%{_release}
License:	GPL
Group:		Development/Libraries
URL: http://apollon.sourceforge.net/
Source: http://dl.sf.net/gift/gift-openft-0.2.1.2.tar.bz2
BuildRequires: gcc, make, gift
Requires: gift

#(d) primscreenshot: 
#(d) screenshotsurl: 
#(d) comment:

%description
Openft plugin for gift

%description -l nl
Openft plugin voor gift

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
/usr/lib/giFT/libOpenFT.la
/usr/lib/giFT/libOpenFT.so
/usr/share/giFT/OpenFT/OpenFT.conf.template
/usr/share/giFT/OpenFT/nodes

%changelog
* Mon Dec 29 2003 Dries Verachtert <dries@ulyssis.org> 0.2.1.2-1.dries
- first packaging for Fedora Core 1

