# $Id$
# Authority: dries
# Upstream: Chris Mungall <cjm$fruitfly,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Data-Stag

Summary: Structured Tags datastructures
Name: perl-Data-Stag
Version: 0.11
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Data-Stag/

Source: http://www.cpan.org/modules/by-module/Data/Data-Stag-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This module is for manipulating data as hierarchical tag/value pairs
(Structured TAGs or Simple Tree AGgreggates). These datastructures can
be represented as nested arrays, which have the advantage of being
native to perl.

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
%doc Changes INSTALL MANIFEST META.yml README
%doc %{_mandir}/man1/stag-*.1*
%doc %{_mandir}/man3/Data::Stag.3pm*
%doc %{_mandir}/man3/Data::Stag::*.3pm*
%{_bindir}/stag-*.pl
%{perl_vendorlib}/Data/Stag/
%{perl_vendorlib}/Data/Stag.pm

%changelog
* Sun Jun 22 2008 Dag Wieers <dag@wieers.com> - 0.11-1
- Updated to release 0.11.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 0.10-1
- Updated to release 0.10.

* Sun Dec 11 2005 Dries Verachtert <dries@ulyssis.org> - 0.09-1
- Initial package.
