# $Id$
# Authority: dries
# Upstream: Martin Hosken <martin_hosken$sil,org>

### EL6 ships with perl-Font-TTF-0.45-6.el6
%{?el6:# Tag: rfx}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Font-TTF

Summary: TTF Fonts
Name: perl-Font-TTF
Version: 0.45
Release: 1%{?dist}
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Font-TTF/

Source: http://www.cpan.org/modules/by-module/Font/Font-TTF-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
Provides: perl(ttfmod.pl)

%description
Use TTF fonts with Perl.

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
%{__rm} -f %{buildroot}%{perl_vendorlib}/Font/TTF/Win32.pm

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING Changes MANIFEST MANIFEST.SKIP META.yml README.TXT TODO
%doc %{_mandir}/man3/Font::TTF.3pm*
%doc %{_mandir}/man3/Font::TTF::*.3pm*
%dir %{perl_vendorlib}/Font/
%{perl_vendorlib}/Font/TTF/
%{perl_vendorlib}/Font/TTF.pm
%{perl_vendorlib}/ttfmod.pl

%changelog
* Mon Jun 23 2008 Dag Wieers <dag@wieers.com> - 0.45-1
- Updated to release 0.45.

* Sat Nov 24 2007 Dag Wieers <dag@wieers.com> - 0.43-1
- Updated to release 0.43.

* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 0.42-1
- Updated to release 0.42.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.41-1
- Updated to release 0.41.

* Tue Sep 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.40-1
- Updated to release 0.40.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.38.1-1
- Updated to release 0.38.1.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 0.37-1
- Updated to release 0.37.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 0.35-1
- Updated to release 0.35.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.34-1
- Initial package.
