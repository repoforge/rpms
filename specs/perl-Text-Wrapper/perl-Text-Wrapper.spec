# $Id$
# Authority: dries
# Upstream: Christopher J. Madsen <perl$cjmweb,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Text-Wrapper

Summary: Simple word wrapping routine
Name: perl-Text-Wrapper
Version: 1.02
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Text-Wrapper/

Source: http://www.cpan.org/modules/by-module/Text/Text-Wrapper-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.004
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Spec)
BuildRequires: perl(FindBin)
BuildRequires: perl(Module::Build) >= 0.21
BuildRequires: perl(Test::More)
Requires: perl >= 0:5.004

%description
This module provides simple word wrapping.  It breaks long lines,
but does not alter spacing or remove existing line breaks.  If
you're looking for more sophisticated text formatting, try the
Text::Format module.

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

### Clean up docs
find example/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README example/
%doc %{_mandir}/man3/Text::Wrapper.3pm*
%dir %{perl_vendorlib}/Text/
#%{perl_vendorlib}/Text/Wrapper/
%{perl_vendorlib}/Text/Wrapper.pm

%changelog
* Thu May 15 2008 Dag Wieers <dag@wieers.com> - 1.02-1
- Updated to release 1.02.

* Mon Nov 19 2007 Dag Wieers <dag@wieers.com> - 1.01-1
- Updated to release 1.01.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.000-1
- Initial package.
