# $Id$
# Authority: dries
# Upstream: Robert Sedlacek <phaylon$dunkelheit,at>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Declare-Constraints-Simple

Summary: Declarative Validation of Data Structures
Name: perl-Declare-Constraints-Simple
Version: 0.03
Release: 2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Declare-Constraints-Simple/

Source: http://www.cpan.org/authors/id/P/PH/PHAYLON/Declare-Constraints-Simple-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More)

### Provides required by package itself
Provides: perl(Declare::Constraints::Simple-Library)

%description
Declarative Validation of Data Structures.

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Declare::Constraints::Simple.3pm*
%doc %{_mandir}/man3/Declare::Constraints::Simple::*.3pm*
%dir %{perl_vendorlib}/Declare/
%dir %{perl_vendorlib}/Declare/Constraints/
%{perl_vendorlib}/Declare/Constraints/Simple/
%{perl_vendorlib}/Declare/Constraints/Simple.pm

%changelog
* Sat Nov 24 2007 Dag Wieers <dag@wieers.com> - 0.03-2
- Added selfcontained provides.

* Fri Nov 09 2007 Dag Wieers <dag@wieers.com> - 0.03-1
- Updated to release 0.03.

* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.01-1
- Initial package.
