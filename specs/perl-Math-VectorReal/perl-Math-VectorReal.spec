# $Id$

# Authority: dries
# Upstream: Anthony Thyssen <anthony$cit,gu,edu,au>

%define real_name Math-VectorReal
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Module to handle 3D Vector Mathematics
Name: perl-Math-VectorReal
Version: 1.02
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Math-VectorReal/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://search.cpan.org/CPAN/authors/id/A/AN/ANTHONY/Math-VectorReal-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
The Math::VectorReal' package defines a 3D mathematical "vector", in a way
that is compatible with the previous CPAN module ath::MatrixReal'.  However
it provides a more vector oriented set of mathematical functions and
overload operators, to the atrixReal' package. For example the normal perl string
functions "x" and "." have been overloaded to allow vector cross and dot
product operations. Vector math formula thus looks like vector math formula
in perl programs using this package.

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
%{perl_vendorlib}/Math/VectorReal.pm
%{perl_vendorlib}/Math/*.pl
%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/.packlist

# perl_vendorlib: /usr/lib/perl5/vendor_perl/5.8.0
# perl_vendorarch: /usr/lib/perl5/vendor_perl/5.8.0/i386-linux-thread-multi
# perl_archlib: /usr/lib/perl5/5.8.0/i386-linux-thread-multi
# perl_privlib: /usr/lib/perl5/5.8.0

%changelog
* Mon Dec 06 2004 Dries Verachtert <dries@ulyssis.org> - 1.02-1
- Initial package.
