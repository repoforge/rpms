# $Id$
# Authority: dries
# Upstream: Colin Kuskie <ckuskie$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Statistics-Descriptive
%define real_version 3.0100

Summary: Module of basic descriptive statistical functions
Name: perl-Statistics-Descriptive
Version: 3.0.100
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Statistics-Descriptive/

Source: http://www.cpan.org/modules/by-module/Statistics/Statistics-Descriptive-%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{real_version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Module of basic descriptive statistical functions.

%prep
%setup -n %{real_name}-%{real_version}

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
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Statistics/Descriptive.pm

%changelog
* Thu Jun 29 2009 Christoph Maser <cmr@financial.com> - 3.0100-1
- Updated to version 3.0.100.

* Thu Jun 18 2009 Christoph Maser <cmr@financial.com> - 3.0000-1
- Updated to version 3.0.
- Added real_version 

* Thu Jun 18 2009 Christoph Maser <cmr@financial.com> - 3.000-1
- Updated to version 3.000.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 2.6-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 2.6-1
- Initial package.
