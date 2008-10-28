# $Id$
# Authority: dries
# Upstream: David Coppit <david$coppit,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Module-Install-CustomInstallationPath

Summary: Module::Install extension that allows the user to interactively specify custom installation directories
Name: perl-Module-Install-CustomInstallationPath
Version: 0.1040
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Module-Install-CustomInstallationPath/

Source: http://www.cpan.org/modules/by-module/Module/Module-Install-CustomInstallationPath-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::HomeDir)

%description
A Module::Install extension that allows the user to interactively specify
custom installation directories

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
%doc CHANGES LICENSE MANIFEST META.yml README
%doc %{_mandir}/man3/Module::Install::CustomInstallationPath.3pm*
%dir %{perl_vendorlib}/Module/
%dir %{perl_vendorlib}/Module/Install/
#%{perl_vendorlib}/Module/Install/CustomInstallationPath/
%{perl_vendorlib}/Module/Install/CustomInstallationPath.pm

%changelog
* Mon Oct 13 2008 Dag Wieers <dag@wieers.com> - 0.1040-1
- Updated to release 0.1040.

* Sun Dec 11 2005 Dries Verachtert <dries@ulyssis.org> - 0.1030-1
- Initial package.
