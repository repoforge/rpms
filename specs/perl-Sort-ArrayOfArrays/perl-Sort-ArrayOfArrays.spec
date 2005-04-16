# $Id$
# Authority: dries
# Upstream: Earl Cahill <cpan$spack,net>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Sort-ArrayOfArrays

Summary: Perl extension for sorting an array of arrays
Name: perl-Sort-ArrayOfArrays
Version: 1.00
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Sort-ArrayOfArrays/

Source: http://search.cpan.org/CPAN/authors/id/E/EA/EARL/Sort-ArrayOfArrays-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Sort::ArrayOfArrays was written to sort an arbitrary array of arrays, in
powerful, different ways.
	
%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Sort/ArrayOfArrays.pm

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.00-1
- Initial package.
