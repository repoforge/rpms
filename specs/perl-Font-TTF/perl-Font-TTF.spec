# $Id$
# Authority: dries
# Upstream: Martin Hosken <martin_hosken$sil,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Font-TTF

Summary: TTF Fonts
Name: perl-Font-TTF
Version: 0.41
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Font-TTF/

Source: http://search.cpan.org/CPAN/authors/id/M/MH/MHOSKEN/Font-TTF-%{version}.tar.gz
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
%doc README.TXT
%doc %{_mandir}/man?/Font::TTF*
%{perl_vendorlib}/Font/TTF.pm
%{perl_vendorlib}/Font/TTF/
%{perl_vendorlib}/ttfmod.pl

%changelog
* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.41-1
- Updated to release 0.41.

* Tue Sep 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.40-1
- Updated to release 0.40.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.38.1-1
- Updated to release 0.38.1.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.37-1.2
- Rebuild for Fedora Core 5.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 0.37-1
- Updated to release 0.37.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 0.35-1
- Updated to release 0.35.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.34-1
- Initial package.
