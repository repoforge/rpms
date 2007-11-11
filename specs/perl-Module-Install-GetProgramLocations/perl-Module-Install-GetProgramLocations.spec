# $Id$
# Authority: dries
# Upstream: David Coppit <david$coppit,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Module-Install-GetProgramLocations

Summary: Module::Install extension for specifying the location of other programs
Name: perl-Module-Install-GetProgramLocations
Version: 0.3001
Release: 1.2
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Module-Install-GetProgramLocations/

Source: http://www.cpan.org/modules/by-module/Module/Module-Install-GetProgramLocations-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl-Sort-Versions
BuildRequires: perl(ExtUtils::MakeMaker)

%description
A Module::Install extension that allows the user to interactively specify
the location of programs needed by the module to be installed. The specified
program will be converted to a full path and validated. If version information
is supplied, the version number of the program will also be checked.

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
%{perl_vendorlib}/Module/Install/GetProgramLocations.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.3001-1.2
- Rebuild for Fedora Core 5.

* Sun Dec 11 2005 Dries Verachtert <dries@ulyssis.org> - 0.3001-1
- Initial package.
