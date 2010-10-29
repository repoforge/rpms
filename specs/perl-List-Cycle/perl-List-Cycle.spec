# $Id$
# Upstream: Andy Lester <andy@petdance.com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)
%define real_name List-Cycle

Summary: Objects for cycling through a list of values
Name: perl-List-Cycle
Version: 1.00
Release: 1%{?dist}
License: unknown
Group: Applications/CPAN
URL: http://search.cpan.org/dist/List-Cycle/

Source: http://search.cpan.org/CPAN/authors/id/P/PE/PETDANCE/List-Cycle-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl(Carp)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More)
Requires: perl(Carp)
Requires: perl(Test::More)

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup


%description


%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}
%{__make} %{?_smp_mflags} test

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/List::Cycle.3pm*
%dir %{perl_vendorlib}/
%{perl_vendorlib}/List/Cycle.pm
%exclude %{perl_vendorarch}/auto/List/Cycle/.packlist


%changelog
* Fri Oct 29 2010 Christoph Maser <cmaser.gmx.de> - 1.00-1
- initial package
