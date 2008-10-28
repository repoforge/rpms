# $Id$
# Authority: dries
# Upstream: David Coppit <david$coppit,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Module-Install-GetProgramLocations

Summary: Module::Install extension for specifying the location of other programs
Name: perl-Module-Install-GetProgramLocations
Version: 0.3003
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Module-Install-GetProgramLocations/

Source: http://www.cpan.org/modules/by-module/Module/Module-Install-GetProgramLocations-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.004
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(IO::CaptureOutput)
BuildRequires: perl(Sort::Versions)
BuildRequires: perl(Test::More)
Requires: perl >= 0:5.004

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
%doc CHANGES LICENSE MANIFEST META.yml README
%doc %{_mandir}/man3/Module::Install::GetProgramLocations.3pm*
%dir %{perl_vendorlib}/Module/
%dir %{perl_vendorlib}/Module/Install/
#%{perl_vendorlib}/Module/Install/GetProgramLocations/
%{perl_vendorlib}/Module/Install/GetProgramLocations.pm

%changelog
* Wed Oct 15 2008 Dag Wieers <dag@wieers.com> - 0.3003-1
- Updated to release 0.3003.

* Sun Dec 11 2005 Dries Verachtert <dries@ulyssis.org> - 0.3001-1
- Initial package.
