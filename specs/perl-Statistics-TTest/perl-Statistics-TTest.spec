# $Id$
# Authority: shuff
# Upstream: Yun-Fang Juan <yunfangjuan$yahoo,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Statistics-TTest

Summary: Perl module to perform T-test on 2 independent samples
Name: perl-%{real_name}
Version: 1.1.0
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Statistics-TTest/

Source: http://search.cpan.org/CPAN/authors/id/Y/YU/YUNFANG/Statistics-TTest-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Statistics::Descriptive) >= 2.6
BuildRequires: perl(Statistics::Distributions) >= 0.07
BuildRequires: rpm-macros-rpmforge
Requires: perl
Requires: perl(Statistics::Descriptive) >= 2.6
Requires: perl(Statistics::Distributions) >= 0.07


### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
This is the Statistical T-Test module to compare 2 independent samples. It
takes 2 array of point measures, compute the confidence intervals using the
PointEstimation module (which is also included in this package) and use the
T-statistic to test the null hypothesis. If the null hypothesis is rejected,
the difference will be given as the lower_clm and upper_clm of the TTest
object.

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
%doc Makefile.PL
%doc %{_mandir}/man?/*
%dir %{perl_vendorlib}/Statistics/
%{perl_vendorlib}/Statistics/*

%changelog
* Fri Nov 13 2009 Steve Huff <shuff@vecna.org> - 1.1.0-1
- Initial package.
