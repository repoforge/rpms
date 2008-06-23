# $Id$
# Authority: dag
# Upstream: Mark Stosberg <mark$summersault,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Data-FormValidator

Summary: Validates user input (usually from an HTML form) based on input profile
Name: perl-Data-FormValidator
Version: 4.61
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Data-FormValidator/

Source: http://www.cpan.org/modules/by-module/Data/Data-FormValidator-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 1:5.008
BuildRequires: perl(Module::Build)
Requires: perl >= 1:5.008

%description
Validates user input (usually from an HTML form) based
on input profile.

%prep
%setup -n %{real_name}-%{version}

%build
#%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
#%{__make} %{?_smp_mflags}
%{__perl} Build.PL
./Build

%install
%{__rm} -rf %{buildroot}
#%{__make} pure_install
PERL_INSTALL_ROOT="%{buildroot}" ./Build install installdirs="vendor"

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST MANIFEST.SKIP META.yml README RELEASE_NOTES
%doc %{_mandir}/man3/Data::FormValidator.3pm*
%doc %{_mandir}/man3/Data::FormValidator::*.3pm*
%dir %{perl_vendorlib}/Data/
%{perl_vendorlib}/Data/FormValidator/
%{perl_vendorlib}/Data/FormValidator.pm

%changelog
* Sun Jun 22 2008 Dag Wieers <dag@wieers.com> - 4.61-1
- Updated to release 4.61.

* Wed Nov 21 2007 Dag Wieers <dag@wieers.com> - 4.57-1
- Initial package. (using DAR)
