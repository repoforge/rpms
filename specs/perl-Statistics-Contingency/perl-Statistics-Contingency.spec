# $Id$
# Authority: dries
# Upstream: Ken Williams <ken$mathforum,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Statistics-Contingency

Summary: Calculate precision, recall, F1, accuracy, etc
Name: perl-Statistics-Contingency
Version: 0.08
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Statistics-Contingency/

Source: http://www.cpan.org/modules/by-module/Statistics/Statistics-Contingency-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
The "Statistics::Contingency" class helps you calculate several useful
statistical measures based on 2x2 "contingency tables". I use these measures
to help judge the results of automatic text categorization experiments, but
they are useful in other situations as well.

The general usage flow is to tally a whole bunch of results in the
"Statistics::Contingency" object, then query that object to obtain the
measures you are interested in. When all results have been collected, you
can get a report on accuracy, precision, recall, F1, and so on, with both
macro-averaging and micro-averaging over categories.

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
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Statistics/Contingency.pm

%changelog
* Thu Jun 18 2009 Christoph Maser <cmr@financial.com> - 0.08-1
- Updated to version 0.08.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.06-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.06-1
- Initial package.
