# $Id$

# Authority: dries

# NeedsCleanup

Summary: Deamon for communicating with filesharing protocols
Summary(nl): daemon om te communiceren met filesharing protocols
Name: gift
Version: 0.11.5
Release: 1.dries
License: GPL
Group: Development/Libraries
URL: http://gift.sf.net/

Source: http://dl.sf.net/gift/gift-%{version}.tar.bz2 
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc, make, gcc-c++

%description
giFT is a modular daemon capable of abstracting the communication between
the end user and specific filesharing protocols (peer-to-peer or otherwise).

%description -l nl
giFT is een modulaire daemon die een abstractie maakt van het protocol
tussen de gebruiker en specifieke filesharing protocollen (peer-to-peer en
ook andere)

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
make install-strip \
	DESTDIR="%{buildroot}"
#ln -s libgift.so.0.0.0 ${DESTDIR}/usr/lib/libgift.so
ls -l ${DESTDIR}/usr/lib/libgift.so*

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%files
%defattr(-,root,root,0755)
%doc README AUTHORS COPYING HACKING INSTALL QUICKSTART TODO
%{_bindir}/gift-setup
%{_bindir}/giftd
%{_includedir}/libgift
%{_libdir}/libgift.la
%{_libdir}/libgift.so
%{_libdir}/libgift.so.0
%{_libdir}/libgift.so.0.0.0
%{_libdir}/libgiftproto.la
%{_libdir}/libgiftproto.so
%{_libdir}/libgiftproto.so.0
%{_libdir}/libgiftproto.so.0.0.0
%{_libdir}/pkgconfig/libgift.pc
%{_datadir}/giFT/giftd.conf.template
%{_datadir}/giFT/mime.types
%{_datadir}/giFT/ui/ui.conf.template
%{_datadir}/man/man1/giftd.1.gz

%changelog
* Mon Dec 29 2003 Dries Verachtert <dries@ulyssis.org> 0.11.5-1.dries
- first packaging for Fedora Core 1
