# $Id$
# Authority: dries
# Upstream: Randy J Ray <rjray$blackperl,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Devel-Coverage

Summary: Perform coverage analysis
Name: perl-Devel-Coverage
Version: 0.2
Release: 1.2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Devel-Coverage/

Source: http://search.cpan.org/CPAN/authors/id/R/RJ/RJRAY/Devel-Coverage-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Devel::Coverage is a coverage analysis tool for Perl code. It is inspired
by several factors, most notable my personal high consideration for the
PureCoverage tool (formerly of PureAtria, now from Rational Software)
and my frustration at finding bugs in my code that were hidden in blocks
that were never reached in test cases. That's what a coverage analysis tool
does-- it shows you what parts of your code were and were not reached over
the course of one or more runs.

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
%doc ChangeLog README
%doc %{_mandir}/man?/*
%{_bindir}/coverperl
%{perl_vendorlib}/Devel/Coverage.pm
%{perl_vendorlib}/Devel/Coverage

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.2-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.2-1
- Initial package.
