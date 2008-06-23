# $Id$
# Authority: dries
# Upstream: Ken Williams <ken$mathforum,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Algorithm-NaiveBayes

Summary: Bayesian prediction of categories
Name: perl-Algorithm-NaiveBayes
Version: 0.04
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Algorithm-NaiveBayes/

Source: http://www.cpan.org/modules/by-module/Algorithm/Algorithm-NaiveBayes-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Bayesian prediction of categories.

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
%{perl_vendorlib}/Algorithm/NaiveBayes.pm
%{perl_vendorlib}/Algorithm/NaiveBayes

%changelog
* Mon Jun 18 2007 Dries Verachtert <dries@ulyssis.org> - 0.04-1
- Updated to release 0.04.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.03-1
- Initial package.
