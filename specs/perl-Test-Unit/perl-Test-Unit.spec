# $Id$
# Authority: dries
# Upstream: Adam Spiers <adam$spiers,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Test-Unit

Summary: Unit testing framework for Perl
Name: perl-Test-Unit
Version: 0.25
Release: 1.2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Test-Unit/

Source: http://www.cpan.org/modules/by-module/Test/Test-Unit-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Test::Unit::* is a sophisticated unit testing framework for Perl
that is derived from the JUnit testing framework for Java by Kent
Beck and Erich Gamma.

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
%doc ChangeLog Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Test

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.25-1.2
- Rebuild for Fedora Core 5.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 0.25-1
- Updated to release 0.25.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.24-1
- Initial package.
