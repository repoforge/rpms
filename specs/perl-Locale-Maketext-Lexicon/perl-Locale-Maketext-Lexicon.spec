# $Id$
# Authority: dries
# Upstream: Audrey Tang <cpan$audreyt,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Locale-Maketext-Lexicon

Summary: Extract translatable strings from source
Name: perl-Locale-Maketext-Lexicon
Version: 0.66
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Locale-Maketext-Lexicon/

Source: http://www.cpan.org/modules/by-module/Locale/Locale-Maketext-Lexicon-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.004
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl >= 0:5.004

%description
Locale::Maketext::Lexicon is a module providing lexicon-handling backends,
for "Locale::Maketext" to read from other localization formats, such as
PO files, MO files, or from databases via the "Tie" interface.

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

### Clean up docs
find docs/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS Changes MANIFEST META.yml README SIGNATURE docs/
%doc %{_mandir}/man1/xgettext.pl.1*
%doc %{_mandir}/man3/Locale::Maketext::*.3pm*
%{_bindir}/xgettext.pl
%dir %{perl_vendorlib}/Locale/
%{perl_vendorlib}/Locale/Maketext/

%changelog
* Wed Feb 20 2008 Dag Wieers <dag@wieers.com> - 0.66-1
- Updated to release 0.66.

* Thu Dec 27 2007 Dag Wieers <dag@wieers.com> - 0.65-1
- Updated to release 0.65.

* Mon Jun 18 2007 Dries Verachtert <dries@ulyssis.org> - 0.64-1
- Updated to release 0.64.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.62-1
- Updated to release 0.62.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.55-1
- Updated to release 0.55.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 0.53-1
- Updated to release 0.53.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 0.49-1
- Updated to release 0.49.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.48-1
- Initial package.
