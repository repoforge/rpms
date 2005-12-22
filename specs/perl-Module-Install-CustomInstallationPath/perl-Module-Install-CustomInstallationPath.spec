# $Id$
# Authority: dries
# Upstream: David Coppit <david$coppit,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Module-Install-CustomInstallationPath

Summary: Module::Install extension for custom installation directories
Name: perl-Module-Install-CustomInstallationPath
Version: 0.1030
Release: 1
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Module-Install-CustomInstallationPath/

Source: http://search.cpan.org/CPAN/authors/id/D/DC/DCOPPIT/Module-Install-CustomInstallationPath-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

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
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Module/Install/CustomInstallationPath.pm

%changelog
* Sun Dec 11 2005 Dries Verachtert <dries@ulyssis.org> - 0.1030-1
- Initial package.
