# $Id$
# Authority: dries
# Upstream: Robin Houston <robin-cpan$kitsite,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Want

Summary: Implement the 'want' command
Name: perl-Want
Version: 0.08
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Want/

Source: http://search.cpan.org/CPAN/authors/id/R/RO/ROBIN/Want-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
This module generalises the mechanism of the wantarray
function, allowing a function to determine in some detail
how its return value is going to be immediately used.
	   
%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorarch}/Want.pm
%{perl_vendorarch}/auto/Want

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.08-1
- Initial package.
