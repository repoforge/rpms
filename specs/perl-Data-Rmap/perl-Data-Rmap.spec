# $Id$
# Authority: dries
# Upstream: Brad Bowman <perl-cpan$bereft,net>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Data-Rmap

Summary: Recursive map, apply a block to a data structure
Name: perl-Data-Rmap
Version: 0.61
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Data-Rmap/

Source: http://search.cpan.org/CPAN/authors/id/B/BO/BOWMANBS/Data-Rmap-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker), perl

%description
Recursively evaluate a BLOCK over a list of data structures (locally
setting $_ to each element) and return the list composed of the results
of such evaluations. $_ can be used to modify the elements.

Data::Rmap currently traverses HASH, ARRAY, SCALAR and GLOB reference
types and ignores others. Depending on which rmap_* wrapper is used, the
BLOCK is called for only scalar values, arrays, hashes, references, all
elements or a customizable combination.

The list of data structures is traversed pre-order in a depth-first
fashion. That is, the BLOCK is called for the container reference before
is it called for it's elements (although see "recurse" below for
post-order). The values of a hash are traversed in the usual "values"
order which may affect some applications.

If the "cut" subroutine is called in the BLOCK then the traversal stops
for that branch, say if you "cut" an array then the code is never called
for it's elements (or their sub-elements). To simultaneously return
values and cut, simply pass the return list to cut:
"cut('add','to','returned');"

The first parameter to the BLOCK is an object which maintains the state
of the traversal. Methods available on this object are described in
"State Object" below.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Data/Rmap.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.61-1.2
- Rebuild for Fedora Core 5.

* Sun Dec 11 2005 Dries Verachtert <dries@ulyssis.org> - 0.61-1
- Initial package.
