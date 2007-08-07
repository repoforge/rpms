# $Id$
# Authority: dries
# Upstream: John Macdonald <john$perlwolf,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Heap

Summary: Perl extensions for keeping data partially sorted
Name: perl-Heap
Version: 0.71
Release: 1.2
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Heap/

Source: http://www.cpan.org/modules/by-module/Heap/Heap-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
This is a collection of routines for managing a heap data structure. There are
two major components: a heap component, and an element component. A heap
package basically keeps a collection of elements and is able to return the
smallest one. The heap component interface is defined in Heap(3) and must be
supported by all heap packages.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} install

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} \
		%{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*.3pm*
%{perl_vendorlib}/Heap/
%{perl_vendorlib}/Heap.pm
%{perl_vendorlib}/auto/Heap/

%changelog
* Mon Dec 06 2004 Dries Verachtert <dries@ulyssis.org> - 0.71-1
- Initial package.
