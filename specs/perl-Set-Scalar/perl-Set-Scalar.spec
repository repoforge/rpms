# $Id$
# Authority: dries
# Upstream: Jarkko Hietaniemi <jhi$iki,fi>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Set-Scalar

Summary: Basic set operations
Name: perl-Set-Scalar
Version: 1.25
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Set-Scalar/

Source: http://search.cpan.org/CPAN/authors/id/J/JH/JHI/Set-Scalar-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Basic set operations.

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
%doc ChangeLog MANIFEST META.yml README
%doc %{_mandir}/man3/Set::Scalar.3pm*
%doc %{_mandir}/man3/Set::Scalar::*.3pm*
%dir %{perl_vendorlib}/Set/
%{perl_vendorlib}/Set/Scalar
%{perl_vendorlib}/Set/Scalar.pm

%changelog
* Mon Dec 28 2009 Christoph Maser <cmr@financial.com> - 1.25-1
- Updated to version 1.25.

* Thu Jun 18 2009 Christoph Maser <cmr@financial.com> - 1.24-1
- Updated to version 1.24.

* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 1.22-1
- Updated to release 1.22.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 1.20-1
- Updated to release 1.20.

* Sat Apr  2 2005 Dries Verachtert <dries@ulyssis.org> - 1.19-1
- Initial package.
