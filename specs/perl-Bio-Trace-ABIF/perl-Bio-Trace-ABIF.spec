# $Id$
# Authority: dries
# Upstream: Nicola Vitacolonna <vitacolonna$appliedgenomics,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Bio-Trace-ABIF

Summary: Parse ABIF files
Name: perl-Bio-Trace-ABIF
Version: 1.04
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Bio-Trace-ABIF/

Source: http://search.cpan.org/CPAN/authors/id/V/VI/VITA/Bio-Trace-ABIF-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Test::More)
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl
Requires: perl(Test::More)

%filter_from_requires /^perl*/d
%filter_setup

%description
Perl extension for reading and parsing ABIF (Applied Biosystems, 
Inc. Format) files.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}
%{__make} test

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Bio::Trace::ABIF.3pm*
%dir %{perl_vendorlib}/Bio/
%dir %{perl_vendorlib}/Bio/Trace/
#%{perl_vendorlib}/Bio/Trace/ABIF/
%{perl_vendorlib}/Bio/Trace/ABIF.pm

%changelog
* Sat Feb  6 2010 Christoph Maser <cmr@financial.com> - 1.04-1
- Updated to version 1.04.

* Thu Jan  7 2010 Christoph Maser <cmr@financial.com> - 1.02-1
- Updated to version 1.02.

* Tue Nov 06 2007 Dag Wieers <dag@wieers.com> - 1.01-1
- Updated to release 1.01.

* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.02-1
- Initial package.
