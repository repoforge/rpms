# $Id$

# Authority: dries
# Upstream: John Macdonald <john$perlwolf,com>

%define real_name Heap
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Perl extensions for keeping data partially sorted
Name: perl-Heap
Version: 0.71
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Heap/

Source: http://www.cpan.org/modules/by-module/Heap/Heap-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
This is a collection of routines for managing a heap data structure. There are 
two major components: a heap component, and an element component. A heap 
package basically keeps a collection of elements and is able to return the 
smallest one. The heap component interface is defined in Heap(3) and must be
supported by all heap packages.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" destdir=%{buildroot}
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
%{perl_vendorlib}/Heap.pm
%{perl_vendorlib}/Heap
%{perl_vendorlib}/auto/Heap
%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/.packlist

%changelog
* Mon Dec 06 2004 Dries Verachtert <dries@ulyssis.org> - 0.71-1
- Initial package.
