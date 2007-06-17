# $Id$
# Authority: dries
# Upstream: Jonathan Leto <jonathan$leto,net>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Math-Gsl

Summary: Interface to The GNU Scientific Library
Name: perl-Math-Gsl
Version: 0.08
Release: 1.2
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Math-Gsl/

Source: http://search.cpan.org/CPAN/authors/id/L/LE/LETO/Math-Gsl-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

#BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
Currently this module implements the GSL Special function library and the
single GSL function poly_complex_solve.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
#%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
#%{perl_vendorlib}/Math/Gsl.pm
#%{perl_vendorlib}/Math/Gsl/*
#%exclude %{perl_archlib}/perllocal.pod
#%exclude %{perl_vendorarch}/auto/*/*/.packlist

# perl_vendorlib: /usr/lib/perl5/vendor_perl/5.8.0
# perl_vendorarch: /usr/lib/perl5/vendor_perl/5.8.0/i386-linux-thread-multi
# perl_archlib: /usr/lib/perl5/5.8.0/i386-linux-thread-multi
# perl_privlib: /usr/lib/perl5/5.8.0

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.08-1.2
- Rebuild for Fedora Core 5.

* Tue Apr 05 2005 Dries Verachtert <dries@ulyssis.org> - 0.08-1
- Initial package.
