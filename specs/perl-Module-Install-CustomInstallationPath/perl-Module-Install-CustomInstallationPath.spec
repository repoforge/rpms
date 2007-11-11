# $Id$
# Authority: dries
# Upstream: David Coppit <david$coppit,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Module-Install-CustomInstallationPath

Summary: Module::Install extension for custom installation directories
Name: perl-Module-Install-CustomInstallationPath
Version: 0.1030
Release: 1.2
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Module-Install-CustomInstallationPath/

Source: http://www.cpan.org/modules/by-module/Module/Module-Install-CustomInstallationPath-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)-File-HomeDir

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
%doc CHANGES README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Module/Install/CustomInstallationPath.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.1030-1.2
- Rebuild for Fedora Core 5.

* Sun Dec 11 2005 Dries Verachtert <dries@ulyssis.org> - 0.1030-1
- Initial package.
