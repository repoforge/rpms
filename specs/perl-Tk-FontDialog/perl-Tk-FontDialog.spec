# $Id$
# Authority: dries
# Upstream: Slaven Rezi&#263; <slaven$rezic,de>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Tk-FontDialog

Summary: Font dialog widget for perl/Tk
Name: perl-Tk-FontDialog
Version: 0.15
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Tk-FontDialog/

Source: http://www.cpan.org/modules/by-module/Tk/Tk-FontDialog-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Tk::FontDialog is a font chooser for perl/Tk.

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
%doc %{_mandir}/man3/Tk::FontDialog.3pm*
%dir %{perl_vendorlib}/Tk/
#%{perl_vendorlib}/Tk/FontDialog/
%{perl_vendorlib}/Tk/FontDialog.pm

%changelog
* Wed Jun 10 2009 Christoph Maser <cmr@financial.com> - 0.15-1
- Updated to version 0.15.

* Mon Nov 19 2007 Dag Wieers <dag@wieers.com> - 0.14-1
- Updated to release 0.14.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.13-1
- Updated to release 0.13.

* Tue Nov 14 2006 Dries Verachtert <dries@ulyssis.org> - 0.12-1
- Updated to release 0.12.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 0.11-1
- Updated to release 0.11.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.10-1
- Initial package.
