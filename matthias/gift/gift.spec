# $Id: gift.spec,v 1.1 2004/03/01 15:41:09 driesve Exp $

# Authority: dries

# NeedsCleanup

%define	_name		gift
%define	_version	0.11.5
%define _release	1.dries

Summary: deamon for communicating with filesharing protocols
Summary(nl): daemon om te communiceren met filesharing protocols

BuildRoot:	%{_tmppath}/build-%{_name}-%{_version}
Name:		%{_name}
Version:	%{_version}
Release:	%{_release}
License:	GPL
Group:		Development/Libraries
URL: http://gift.sourceforge.net/
Source: http://prdownloads.sourceforge.net/gift/gift-0.11.5.tar.bz2 
BuildRequires: gcc, make
#Requires: 

#(d) primscreenshot: 
#(d) screenshotsurl: 
#(d) comment:

%description
giFT is a modular daemon capable of abstracting the communication between
the end user and specific filesharing protocols (peer-to-peer or otherwise).

%description -l nl
giFT is een modulaire daemon die een abstractie maakt van het protocol
tussen de gebruiker en specifieke filesharing protocollen (peer-to-peer en
ook andere)

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
#ln -s libgift.so.0.0.0 ${DESTDIR}/usr/lib/libgift.so
ls -l ${DESTDIR}/usr/lib/libgift.so*

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%defattr(-,root,root)
%doc README AUTHORS COPYING HACKING INSTALL QUICKSTART TODO
/usr/bin/gift-setup
/usr/bin/giftd
/usr/include/libgift
/usr/lib/libgift.la
/usr/lib/libgift.so
/usr/lib/libgift.so.0
/usr/lib/libgift.so.0.0.0
/usr/lib/libgiftproto.la
/usr/lib/libgiftproto.so
/usr/lib/libgiftproto.so.0
/usr/lib/libgiftproto.so.0.0.0
/usr/lib/pkgconfig/libgift.pc
/usr/share/giFT/giftd.conf.template
/usr/share/giFT/mime.types
/usr/share/giFT/ui/ui.conf.template
/usr/share/man/man1/giftd.1.gz

%changelog
* Mon Dec 29 2003 Dries Verachtert <dries@ulyssis.org> 0.11.5-1.dries
- first packaging for Fedora Core 1

