# $Id$
# Authority: cmr
# Upstream: Ricardo SIGNES <rjbs$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Data-Section

Summary: Perl module named Data-Section
Name: perl-Data-Section
Version: 0.100270
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Data-Section/

Source: http://search.cpan.org/CPAN/authors/id/R/RJ/RJBS/Data-Section-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(MRO::Compat) >= 0.09
BuildRequires: perl(Sub::Exporter) >= 0.979
#BuildRequires: perl(Test::More) >= 0.88
BuildRequires: perl(Test::More)
Requires: perl(ExtUtils::MakeMaker) >= 6.11
Requires: perl(MRO::Compat) >= 0.09
Requires: perl(Sub::Exporter) >= 0.979
#Requires: perl(Test::More) >= 0.88
Requires: perl(Test::More)

%filter_from_requires /^perl*/d
%filter_setup



%description
perl-Data-Section is a Perl module.

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
%doc Changes LICENSE MANIFEST README
%doc %{_mandir}/man3/Data::Section.3pm*
%dir %{perl_vendorlib}/Data/
#%{perl_vendorlib}/Data/Section/
%{perl_vendorlib}/Data/Section.pm

%changelog
* Sat Feb  6 2010 Christoph Maser <cmr@financial.com> - 0.100270-1
- Updated to version 0.100270.

* Thu Dec 31 2009 Christoph Maser <cmr@financial.com> - 0.093410-1
- Updated to version 0.093410.

* Sun Aug 02 2009 Christoph Maser <cmr@financial.com> - 0.091820-1
- Initial package. (using DAR)
