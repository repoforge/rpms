# $Id$
# Authority: dries

Summary: Gift openft plugin
Name: gift-openft
Version: 0.2.1.2
Release: 1
License: GPL
Group: Development/Libraries
URL: http://apollon.sourceforge.net/

Source: http://dl.sf.net/gift/gift-openft-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gift, gcc-c++, pkgconfig, zlib-devel
Requires: gift

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

%description
Openft plugin for gift

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

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%dir %{_libdir}/giFT/
%dir %{_datadir}/giFT/
%config (noreplace) %{_datadir}/giFT/OpenFT/
%exclude %{_libdir}/giFT/libOpenFT.la
%{_libdir}/giFT/libOpenFT.so

%changelog
* Mon Dec 29 2003 Dries Verachtert <dries@ulyssis.org> 0.2.1.2-1
- first packaging for Fedora Core 1
