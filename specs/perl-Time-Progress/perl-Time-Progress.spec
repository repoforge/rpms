# $Id$
# Authority: cmr
# Upstream: Vladi Belperchinov-Shabanski <cade$biscom,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Time-Progress

Summary: Elapsed and estimated finish time reporting
Name: perl-Time-Progress
Version: 1.7
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Time-Progress/

Source: http://search.cpan.org/CPAN/authors/id/C/CA/CADE/Time-Progress-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
Elapsed and estimated finish time reporting.

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
%doc %{_mandir}/man3/Time::Progress.3pm*
%dir %{perl_vendorlib}/Time/
#%{perl_vendorlib}/Time/Progress/
%{perl_vendorlib}/Time/Progress.pm

%changelog
* Tue Feb  8 2011 Christoph Maser <cmaser@gmx.de> - 1.7-1
- Updated to version 1.7.

* Mon Jul 20 2009 Christoph Maser <cmr@financial.com> - 1.5-1
- Initial package. (using DAR)
