# $Id$
# Authority: dries
# Upstream: Jeff Zucker <jeff$vpservices,com>

# ExcludeDist: el4

%define real_name DBD-File
%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

Summary: Base class for writing DBI drivers for plain files
Name: perl-DBD-File
Version: 0.34
Release: 1.2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DBD-File/

Source: http://www.cpan.org/modules/by-module/DBD/DBD-File-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl-DBI >= 0.42

%description
This module is currently not directly usable, rather it is a base subclass
for modules like DBD::CSV and DBD::AnyData.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install
find %{buildroot} -name .packlist -exec %{__rm} {} \;
%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%doc %{_mandir}/man3/DBD::File*
%{perl_vendorlib}/DBD/File.pm
#%{perl_vendorlib}/DBI/SQL/Nano.pm

%changelog
* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 0.34-1
- Updated to release 0.34.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 0.33-1
- Updated to release 0.33.

* Tue Mar  1 2005 Dries Verachtert <dries@ulyssis.org> - 0.22-1
- Initial package.
