# $Id$

# Authority: dries

# NeedsCleanup

Summary: Gift openft plugin
Name: gift-openft
Version: 0.2.1.2
Release: 1
License: GPL
Group: Development/Libraries
URL: http://apollon.sourceforge.net/

Source: http://dl.sf.net/gift/gift-openft-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc, make, gift, gcc-c++, pkgconfig
Requires: gift

%description
Openft plugin for gift

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
make install-strip \
	DESTDIR="%{buildroot}"

%files
%defattr(-,root,root,0755)
%doc README AUTHORS ChangeLog COPYING NEWS TODO
%{_libdir}/giFT/libOpenFT.*
%{_datadir}/giFT/OpenFT/OpenFT.conf.template
%{_datadir}/giFT/OpenFT/nodes

%changelog
* Mon Dec 29 2003 Dries Verachtert <dries@ulyssis.org> 0.2.1.2-1
- first packaging for Fedora Core 1

