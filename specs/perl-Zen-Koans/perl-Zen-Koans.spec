# $Id$
# Authority: dag
# Upstream: Luke Closs <lukec@cpan.org> is the author of this module, but not of the

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Zen-Koans

Summary: Perl module that implements a library containing over 100 Zen Koans
Name: perl-Zen-Koans
Version: 0.05
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Zen-Koans/

Source: http://www.cpan.org/authors/id/L/LU/LUKEC/Zen-Koans-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More) >= 0.42

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
perl-Zen-Koans is a Perl module that implements a library containing
over 100 Zen Koans.

This package contains the following Perl modules:

    Zen::Koan
    Zen::Koans

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
%doc MANIFEST META.yml
%doc %{_mandir}/man3/Zen::Koan.3pm*
%doc %{_mandir}/man3/Zen::Koans.3pm*
%dir %{perl_vendorlib}/Zen/
%{perl_vendorlib}/Zen/Koan.pm
%{perl_vendorlib}/Zen/Koans.pm

%changelog
* Mon Feb  7 2011 Christoph Maser <cmaser@gmx.de> - 0.05-1
- Updated to version 0.05.

* Thu Oct 11 2007 Dag Wieers <dag@wieers.com> - 0.04-1
- Initial package. (using DAR)
