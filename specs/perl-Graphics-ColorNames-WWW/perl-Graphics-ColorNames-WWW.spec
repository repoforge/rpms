# $Id$
# Authority: dries
# Upstream: Claus Färber <CFAERBER$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Graphics-ColorNames-WWW

Summary: WWW color names and equivalent RGB values
Name: perl-Graphics-ColorNames-WWW
Version: 1.13
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Graphics-ColorNames-WWW/

Source: http://search.cpan.org/CPAN/authors/id/C/CF/CFAERBER/Graphics-ColorNames-WWW-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Graphics::ColorNames) >= 0.32
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::NoWarnings)
Requires: perl(Graphics::ColorNames) >= 0.32

%filter_from_requires /^perl*/d
%filter_setup

%description
WWW color names and equivalent RGB values.

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
%doc MANIFEST META.yml
%doc %{_mandir}/man3/Graphics::ColorNames::IE.3pm*
%doc %{_mandir}/man3/Graphics::ColorNames::SVG.3pm*
%doc %{_mandir}/man3/Graphics::ColorNames::WWW.3pm*
%doc %{_mandir}/man3/Graphics::ColorNames::CSS.3pm*
%dir %{perl_vendorlib}/Graphics/
%dir %{perl_vendorlib}/Graphics/ColorNames/
%{perl_vendorlib}/Graphics/ColorNames/CSS.pm
%{perl_vendorlib}/Graphics/ColorNames/IE.pm
%{perl_vendorlib}/Graphics/ColorNames/SVG.pm
%{perl_vendorlib}/Graphics/ColorNames/WWW.pm

%changelog
* Wed Dec 30 2009 Christoph Maser <cmr@financial.com> - 1.13-1
- Updated to version 1.13.

* Tue Oct 07 2008 Dag Wieers <dag@wieers.com> - 1.00-1
- Updated to release 1.00.

* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.01-1
- Initial package.
