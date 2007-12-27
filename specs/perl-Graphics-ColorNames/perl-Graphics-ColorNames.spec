# $Id$
# Authority: dries
# Upstream: Robert Rothenberg <rrwo$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Graphics-ColorNames

Summary: Defines RGB values for common color names
Name: perl-Graphics-ColorNames
Version: 2.04
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Graphics-ColorNames/

Source: http://www.cpan.org/modules/by-module/Graphics/Graphics-ColorNames-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.6.0
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(FileHandle)
BuildRequires: perl(Test::More)
Requires: perl >= 0:5.6.0

%description
This module defines RGB values for common color names. The intention is
to (1) provide a common module that authors can use with other modules
to specify colors; and (2) free module authors from having to "re-invent
the wheel" whenever they decide to give the users the option of
specifying a color by name rather than RGB value.

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
%doc %{_mandir}/man3/Graphics::ColorNames.3pm*
%doc %{_mandir}/man3/Graphics::ColorNames::*.3pm*
%dir %{perl_vendorlib}/Graphics/
%{perl_vendorlib}/Graphics/ColorNames/
%{perl_vendorlib}/Graphics/ColorNames.pm

%changelog
* Thu Dec 27 2007 Dag Wieers <dag@wieers.com> - 2.04-1
- Updated to release 2.04.

* Sat Jun 18 2005 Dries Verachtert <dries@ulyssis.org> - 1.06-1
- Updated to release 1.06.

* Sat Oct 30 2004 Dries Verachtert <dries@ulyssis.org> - 1.05-1
- Updated to release 1.05.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 0.3901-1
- Initial package.
