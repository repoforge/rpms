# $Id$

# Authority: dries

# NeedsCleanup

Summary: Gift openft plugin
Summary(nl): openft plugin voor gift
Name: gift-openft
Version: 0.2.1.2
Release: 1.dries
License: GPL
Group: Development/Libraries
URL: http://apollon.sourceforge.net/

Source: http://dl.sf.net/gift/gift-openft-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc, make, gift
Requires: gift

%description
Openft plugin for gift

%description -l nl
Openft plugin voor gift

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
%defattr(-,root,root)
%doc README AUTHORS ChangeLog COPYING NEWS TODO
/usr/lib/giFT/libOpenFT.la
/usr/lib/giFT/libOpenFT.so
/usr/share/giFT/OpenFT/OpenFT.conf.template
/usr/share/giFT/OpenFT/nodes

%changelog
* Mon Dec 29 2003 Dries Verachtert <dries@ulyssis.org> 0.2.1.2-1.dries
- first packaging for Fedora Core 1

