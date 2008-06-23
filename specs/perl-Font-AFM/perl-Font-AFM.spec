# $Id$
# Authority: dries
# Upstream: Gisle Aas <gisle$ActiveState,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Font-AFM

Summary: Interface to Adobe Font Metrics files
Name: perl-Font-AFM
Version: 1.20
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Font-AFM/

Source: http://www.cpan.org/modules/by-module/Font/Font-AFM-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This module implements the Font::AFM class. Objects of this
class are initialised from an AFM-file and allows you to obtain
information about the font and the metrics of the various glyphs
in the font.

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
%doc %{_mandir}/man3/Font::AFM.3pm*
%dir %{perl_vendorlib}/Font/
#%{perl_vendorlib}/Font/AFM/
%{perl_vendorlib}/Font/AFM.pm
%{perl_vendorlib}/Font/Metrics/

%changelog
* Mon Jun 23 2008 Dag Wieers <dag@wieers.com> - 1.20-1
- Updated to release 1.20.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.19-1
- Initial package.
