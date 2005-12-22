# $Id$
# Authority: dries
# Upstream: J. J. Merelo-Guerv&#243;s <jmerelo%20(at)%20geneura,ugr,es>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Algorithm-Evolutionary

Summary: Performs paradigm-free evolutionary algorithms
Name: perl-Algorithm-Evolutionary
Version: 0.53
Release: 1
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Algorithm-Evolutionary/

Source: http://search.cpan.org/CPAN/authors/id/J/JM/JMERELO/Algorithm-Evolutionary-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Perl extension for performing paradigm-free evolutionary algorithms.

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
%{perl_vendorlib}/Algorithm/Evolutionary.pm
%{perl_vendorlib}/Algorithm/Evolutionary/*

%changelog
* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.53-1
- Initial package.
