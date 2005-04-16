# $Id$
# Authority: dries
# Upstream: Hugo WL ter Doest <terdoest$cs,utwente,nl>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Statistics-MaxEntropy

Summary: Maximum Entropy Modeling and Feature Induction
Name: perl-Statistics-MaxEntropy
Version: 0.9
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Statistics-MaxEntropy/

Source: http://search.cpan.org/CPAN/authors/id/T/TE/TERDOEST/Statistics-MaxEntropy-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This module is an implementation of the Generalised and Improved
Iterative Scaling (GIS, IIS) algorithms and the Feature
Induction (FI) algorithm as defined in (Darroch and Ratcliff
1972) and (Della Pietra et al. 1997). The purpose of the scaling
algorithms is to find the maximum entropy distribution given a
set of events and (optionally) an initial distribution. Also a
set of candidate features may be specified; then the FI
algorithm may be applied to find and add the candidate
feature(s) that give the largest `gain' in terms of Kullback
Leibler divergence when it is added to the current set of
features.
	
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
%doc %{_mandir}/man?/*
%{_bindir}/ME.wrapper.pl
%{perl_vendorlib}/Statistics
%{perl_vendorlib}/auto/Statistics

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.9-1
- Initial package.
