# $Id$

# Authority: dries

# NeedsCleanup

Summary: Gift gnutella plugin
Summary(nl): gnutella plugin voor gift
Name: gift-gnutella
Version: 0.0.8
Release: 1.dries
License: GPL
Group: Development/Libraries
URL: http://apollon.sourceforge.net/

Source: http://dl.sf.net/gift/gift-gnutella-0.0.8.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc, make, gift
Requires: gift

%description
Gnutella plugin for gift

%description -l nl
Gnutella plugin voor gift

%prep
%setup

%build
%configure
%{__make} %{_smp_mflags}

%install
%{__rm} -rf %{buildroot}
make install-strip \
	DESTDIR="%{buildroot}"

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
