# $Id$
# Authority: dries

Summary: Gift plugin to access the openft network
Name: gift-openft
Version: 0.2.1.6
Release: 1.2%{?dist}
License: GPL
Group: Development/Libraries
URL: http://www.giftproject.org/

Source: http://dl.sf.net/gift/gift-openft-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gift-devel, gcc-c++, pkgconfig, zlib-devel
Requires: gift

%description
giFT is a modular daemon capable of abstracting the communication between the
end user and specific filesharing protocols (peer-to-peer or otherwise). This
packages provides the plugin to access the openft network.

%prep
%setup

%{__perl} -pi.orig -e '
                s|\@plugindir\@|\$(libdir)/giFT|g;
                s|\$\(datadir\)|\$(datadir)/giFT|g;
        ' Makefile.in */Makefile.in

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%dir %{_libdir}/giFT/
%dir %{_datadir}/giFT/
%config (noreplace) %{_datadir}/giFT/OpenFT/
### .la file is needed for gift at runtime !
%{_libdir}/giFT/libOpenFT.la
%{_libdir}/giFT/libOpenFT.so

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.2.1.6-1.2
- Rebuild for Fedora Core 5.

* Thu Nov 03 2005 Dries Verachtert <dries@ulyssis.org> - 0.2.1.6-1
- Update to release 0.2.1.6.

* Wed Feb 02 2005 Dries Verachtert <dries@ulyssis.org> - 0.2.1.5-1
- Update to release 0.2.1.5.

* Sat Aug 21 2004 Dries Verachtert <dries@ulyssis.org> - 0.2.1.4-1
- Update to version 0.2.1.4.

* Sat Jul 24 2004 Dag Wieers <dag@wieers.com> - 0.2.1.2-2
- Include .la file because gift requires it. (Willy De la Court)

* Mon Dec 29 2003 Dries Verachtert <dries@ulyssis.org> 0.2.1.2-1
- first packaging for Fedora Core 1

