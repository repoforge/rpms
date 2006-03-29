# $Id$
# Authority: dries
# Upstream: Nicola Fragale <nicolafragale$libero,it>

Summary: Address book engine
Name: libral
Version: 0.70
Release: 1
License: GPL
Group: Development/Libraries
URL: http://digilander.libero.it/nfragale/

Source: http://download.berlios.de/libral/libral-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libxml2-devel, pkgconfig, gcc-c++
BuildRequires: glib2-devel

%description
Libral is an address book engine. It allows you to create your address books
and to add personal and company cards to them. Data managed in a personal
card include personal data (name, surname, address, etc.), Web links, email
addresses, irc uris, telephone numbers, job information (company where the
contact works, manager, collaborator, etc.), and notes. In a company card
you can manage Web links, email addresses, telephone numbers, and notes.
XML is used to store data. Libral can import addressbooks from GnomeCard,
Kaddressbook, VCard, Evolution, and CSV.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%{_libdir}/libral.so.*
%{_datadir}/gtk-doc/html/libRAL/
#exclude %{_datadir}/doc/libral/libRAL.svg
#exclude %{_datadir}/doc/libral/libRAL.vpp

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/libral-%{version}/
%{_libdir}/libral.a
%{_libdir}/libral.so
%exclude %{_libdir}/*.la
%{_libdir}/pkgconfig/libral.pc

%changelog
* Mon Jan 16 2006 Dries Verachtert <dries@ulyssis.org> - 0.70-1
- Updated to release 0.70.

* Mon Nov 14 2005 Dries Verachtert <dries@ulyssis.org> - 0.50-1
- Initial package.
