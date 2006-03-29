# $Id$
# Authority: dries
# Upstream: Alexander Golomshtok <agolomsh$cronossystems,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Data-UUID

Summary: Generates Globally/Universally Unique Identifiers
Name: perl-Data-UUID
Version: 0.14
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Data-UUID/

Source: http://www.cpan.org/modules/by-module/Data/Data-UUID-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
This module provides a framework for generating UUIDs (Universally Unique
Identifiers, also known as GUIDs (Globally Unique Identifiers). A UUID is
128 bits long, and is guaranteed to be different from all other UUIDs/GUIDs
generated until 3400 A.D. UUIDs were originally used in the Network
Computing System (NCS) and later in the Open Software Foundation's (OSF)
Distributed Computing Environment. Currently many different technologies rely
on UUIDs to provide unique identity for various software components,
Microsoft COM/DCOM for instance, uses GUIDs very extensively to uniquely
identify classes, applications and components across network-connected
systems.

%prep
%setup -n %{real_name}-%{version}

%build
(echo; echo; ) | CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} \
		%{buildroot}%{perl_vendorarch}/auto/*{,/*{,/*}}/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%dir %{perl_vendorarch}/Data/
%{perl_vendorarch}/Data/UUID.pm
%dir %{perl_vendorarch}/auto/Data/
%{perl_vendorarch}/auto/Data/UUID/

%changelog
* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.14-1
- Updated to release 0.14.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.11-1.2
- Rebuild for Fedora Core 5.

* Wed Nov 03 2004 Dries Verachtert <dries@ulyssis.org> - 0.11-1
- Initial package.
