
# $Id$

# Authority: dries

Summary: C++ library for rapid development of database applications
Summary(nl): C++ library om snel database applicaties te ontwikkelen
Name: hk_classes
Version: 0.6.3
Release: 1
License: GPL
Group: Development/Libraries
URL: http://hk-classes.sourceforge.net/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://dl.sf.net/hk-classes/hk_classes-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc, make, gcc-c++, postgresql-devel, mysql-devel, unixODBC-devel, python, python-devel

%description
hk_classes is C++ library which allows rapid development of database
applications with all features a modern database application should have
like forms an reports. hk_classes is database and GUI independent.

%description -l nl
hk_classes is een C++ library waarmee snel database toepassingen ontwikkeld
kunnen worden met alle eigenschappen van een modere database applicatie
zoals formulieren en rapporten. hk_classes is onafhankelijk van de GUI en de
database.

%prep
%{__rm} -rf "${RPM_BUILD_ROOT}"
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__make} install-strip DESTDIR=$RPM_BUILD_ROOT

%files
%defattr(-,root,root,0755)
%doc README AUTHORS COPYING NEWS 

%changelog
* Tue Dec 30 2003 Dries Verachtert <dries@ulyssis.org> 0.6.2a-1
- first packaging for Fedora Core 1
