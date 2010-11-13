# $Id$
# Authority: dries
# Upstream: Jeff Zucker <jeff$vpservices,com>

# ExclusiveDist: el4

%define real_name DBD-File
%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

Summary: Base class for writing DBI drivers for plain files
Name: perl-DBD-File
Version: 0.22
Release: 1.2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DBD-File/

Source: http://www.cpan.org/modules/by-module/DBD/DBD-File-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Patch0: perl-DBD-File-el4fix.patch

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
This module is currently not directly usable, rather it is a base subclass
for modules like DBD::CSV and DBD::AnyData.

%prep
%setup -n %{real_name}-%{version}
%patch0 -p1

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
* Sun Jan 29 2006 Dries Verachtert <dries@ulyssis.org> - 0.22-2
- Added a patch made by Peter Bieringer so it works on el4, thanks!

* Tue Mar  1 2005 Dries Verachtert <dries@ulyssis.org> - 0.22-1
- Initial package.
