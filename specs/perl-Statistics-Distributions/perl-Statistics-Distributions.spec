# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Statistics-Distributions

Summary: Calculate critical values and upper probabilities of statistics
Name: perl-Statistics-Distributions
Version: 1.02
Release: 1.2%{?dist}
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Statistics-Distributions/

Source: http://www.cpan.org/modules/by-module/Statistics/Statistics-Distributions-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker) >= 0:5.00503
Requires: perl >= 0:5.00503

%description
Perl module for calculating critical values and upper probabilities of
common statistical distributions

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/Statistics/
%{perl_vendorlib}/Statistics/Distributions.pm
%dir %{perl_vendorlib}/auto/Statistics/
%dir %{perl_vendorlib}/auto/Statistics/Distributions/
%{perl_vendorlib}/auto/Statistics/Distributions/autosplit.ix

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.02-1.2
- Rebuild for Fedora Core 5.

* Thu Mar 31 2005 Dag Wieers <dag@wieers.com> - 1.02-1
- Initial package. (using DAR)
