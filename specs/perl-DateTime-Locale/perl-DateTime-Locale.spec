# $Id$
# Authority: dries
# Upstream: Dave Rolsky <autarch$urth,org>

### EL6 includes perl-DateTime-Local in perl-DateTime-1:0.5300-1.el6
# ExclusiveDist: el2 el3 el4 el5

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name DateTime-Locale

Summary: Localization support for DateTime.pm
Name: perl-DateTime-Locale
Version: 0.45
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DateTime-Locale/

Source: http://search.cpan.org/CPAN/authors/id/D/DR/DROLSKY/DateTime-Locale-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Module::Build)
# From yaml requires
BuildRequires: perl(Class::ISA)
BuildRequires: perl(List::MoreUtils)
BuildRequires: perl(Params::Validate) >= 0.91
BuildRequires: perl >= 0:5.6
Requires: perl >= 0:5.6

Conflicts: perl(DateTime::Format::Strptime) <= 1.1000
Obsoletes: perl-DateTime-Locale = 0.4001

%description
The DateTime::Locale modules provide localization data for the
DateTime.pm class.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Build.PL
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
%doc Changes LICENSE LICENSE.cldr MANIFEST MANIFEST.SKIP MANIFEST.base META.yml README SIGNATURE
%doc %{_mandir}/man?/*
%dir %{perl_vendorlib}/DateTime/
%{perl_vendorlib}/DateTime/Locale/
%{perl_vendorlib}/DateTime/Locale.pm
%{perl_vendorlib}/DateTime/LocaleCatalog.pm

%changelog
* Wed Jun 30 2010 Steve Huff <shuff@vecna.org> - 0.45-1
- Updated to versioN 0.45.

* Mon Sep 14 2009 Christoph Maser <cmr@financial.com> - 0.44-1
- Updated to version 0.44.

* Fri Jul 10 2009 Christoph Maser <cmr@financial.com> - 0.43-1
- Updated to version 0.43.

* Sun Jun 22 2008 Dag Wieers <dag@wieers.com> - 0.4001-1
- Updated to release 0.4001.

* Mon Nov 05 2007 Dag Wieers <dag@wieers.com> - 0.35-1
- Updated to release 0.35.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 0.22-1
- Updated to release 0.22.

* Fri Mar  4 2005 Dries Verachtert <dries@ulyssis.org> - 0.21-1
- Updated to release 0.21.

* Mon Dec 06 2004 Dries Verachtert <dries@ulyssis.org> - 0.09-1
- Initial package.
