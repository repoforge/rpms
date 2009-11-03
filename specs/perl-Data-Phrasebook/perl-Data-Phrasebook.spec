# $Id$
# Authority: dries
# Upstream: Barbie <barbie$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Data-Phrasebook

Summary: Base class for Phrasebook Models
Name: perl-Data-Phrasebook
Version: 0.29
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Data-Phrasebook/

Source: http://www.cpan.org/modules/by-module/Data/Data-Phrasebook-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More) >= 0.47

%description
Base class for Phrasebook Models.

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
%doc Artistic COPYING ChangeLog Changes INSTALL LICENSE MANIFEST MANIFEST.SKIP META.yml README
%doc %{_mandir}/man3/Data::Phrasebook.3pm*
%doc %{_mandir}/man3/Data::Phrasebook::*.3pm*
%dir %{perl_vendorlib}/Data/
%{perl_vendorlib}/Data/Phrasebook/
%{perl_vendorlib}/Data/Phrasebook.pm

%changelog
* Thu Nov 08 2007 Dag Wieers <dag@wieers.com> - 0.29-1
- Updated to release 0.29.

* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.26-1
- Initial package.
