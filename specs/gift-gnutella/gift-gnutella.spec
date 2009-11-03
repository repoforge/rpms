# $Id$
# Authority: dries

Summary: Gift plugin to access the Gnutella network
Name: gift-gnutella
Version: 0.0.10.1
Release: 1.2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://www.giftproject.org/

Source: http://dl.sf.net/gift/gift-gnutella-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: gift
BuildRequires: gift-devel, gcc-c++, pkgconfig, zlib-devel

%description
giFT is a modular daemon capable of abstracting the communication between the
end user and specific filesharing protocols (peer-to-peer or otherwise). This
packages provides the plugin to access the Gnutella network.


%prep
%setup


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
### .la file is needed for gift at runtime !
%{_libdir}/giFT/libGnutella.la
%{_libdir}/giFT/libGnutella.so
%config(noreplace) %{_datadir}/giFT/Gnutella/Gnutella.conf
%config            %{_datadir}/giFT/Gnutella/Gnutella.conf.template
%{_datadir}/giFT/Gnutella/gwebcaches
%{_datadir}/giFT/Gnutella/hostiles.txt

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.0.10.1-1.2
- Rebuild for Fedora Core 5.

* Thu Nov 03 2005 Dries Verachtert <dries@ulyssis.org> - 0.0.10.1-1
- Update to version 0.0.10.1.

* Wed Feb 02 2005 Dries Verachtert <dries@ulyssis.org> - 0.0.10-1
- Update to version 0.0.10.

* Sat Jul 24 2004 Dag Wieers <dag@wieers.com> - 0.0.9.2-1
- Include .la file because gift requires it. (Willy De la Court)

* Fri Jul 16 2004 Matthias Saou <http://freshrpms.net/> 0.0.9.2-1
- Update to 0.0.9.2.
- Spec file cleanup.

* Mon Dec 29 2003 Dries Verachtert <dries@ulyssis.org> 0.0.8-1
- first packaging for Fedora Core 1

