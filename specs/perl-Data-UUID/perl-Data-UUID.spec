# $Id$

# Authority: dries
# Upstream: Alexander Golomshtok <agolomsh$cronossystems,com>

%define real_name Data-UUID
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Generates Globally/Universally Unique Identifiers
Name: perl-Data-UUID
Version: 0.11
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Data-UUID/

Source: http://search.cpan.org/CPAN/authors/id/A/AG/AGOLOMSH/Data-UUID-%{version}.tar.gz
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
(echo; echo; ) | %{__perl} Makefile.PL INSTALLDIRS="vendor" destdir=%{buildroot}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README Changes
%doc %{_mandir}/man3/*
%{perl_vendorarch}/Data/UUID.pm
%{perl_vendorarch}/auto/Data/UUID/*
%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/.packlist

# perl_vendorlib: /usr/lib/perl5/vendor_perl/5.8.0
# perl_vendorarch: /usr/lib/perl5/vendor_perl/5.8.0/i386-linux-thread-multi
# perl_archlib: /usr/lib/perl5/5.8.0/i386-linux-thread-multi
# perl_privlib: /usr/lib/perl5/5.8.0

%changelog
* Wed Nov 03 2004 Dries Verachtert <dries@ulyssis.org> - 0.11-1
- Initial package.
