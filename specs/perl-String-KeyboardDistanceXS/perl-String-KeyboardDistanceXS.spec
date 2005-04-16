# $Id$
# Authority: dries
# Upstream: Kyle R. Burton <kyle,burton$gmail,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name String-KeyboardDistanceXS

Summary: Rdpfp Approximate String Comparison
Name: perl-String-KeyboardDistanceXS
Version: 0.02
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/String-KeyboardDistanceXS/

Source: http://search.cpan.org/CPAN/authors/id/K/KR/KRBURTON/String-KeyboardDistanceXS-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
This is an XS implementation of the main qwerty functions for computing
the distance and match probabilities from the String::KeyboardDistance
module. Please see the documentation for String::KeyboardDistance for
more about these functions.

Since these functions are implemented as XS, in C, they are
significantly faster than the Perl based functions in
String::KeyboardDistance. That is the primary reason for this module,
performance.
	
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
%{perl_vendorarch}/String/KeyboardDistanceXS.pm
%{perl_vendorarch}/auto/String/KeyboardDistanceXS

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.02-1
- Initial package.
