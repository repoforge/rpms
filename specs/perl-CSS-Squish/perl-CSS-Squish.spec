# $Id$
# Authority: dag
# Upstream: Thomas Sibley <trs$bestpractical,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name CSS-Squish

Summary: Perl module to compact many CSS files into one big file
Name: perl-CSS-Squish
Version: 0.09
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/CSS-Squish/

Source: http://search.cpan.org/CPAN/authors/id/T/TS/TSIBLEY/CSS-Squish-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Spec)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Test::LongString)
BuildRequires: perl(URI)
BuildRequires: perl(URI::file)
BuildRequires: perl >= 5.008
Requires: perl(File::Spec)
Requires: perl(Scalar::Util)
Requires: perl(Test::LongString)
Requires: perl(URI)
Requires: perl(URI::file)
Requires: perl >= 5.008

%filter_from_requires /^perl*/d
%filter_setup


%description
perl-CSS-Squish is a Perl module to compact many CSS files into one big file.

This package contains the following Perl module:

    CSS::Squish

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
%doc CHANGES MANIFEST META.yml README
%doc %{_mandir}/man3/CSS::Squish.3pm*
%dir %{perl_vendorlib}/CSS/
#%{perl_vendorlib}/CSS/Squish/
%{perl_vendorlib}/CSS/Squish.pm

%changelog
* Sat Feb  6 2010 Christoph Maser <cmr@financial.com> - 0.09-1
- Updated to version 0.09.

* Thu Jul  9 2009 Christoph Maser <cmr@financial.com> - 0.08-1
- Updated to version 0.08.

* Tue Nov 13 2007 Dag Wieers <dag@wieers.com> - 0.07-1
- Updated to release 0.07.

* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 0.05-1
- Initial package. (using DAR)
