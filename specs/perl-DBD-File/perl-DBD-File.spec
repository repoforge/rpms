# $Id$

# Authority: dries
# Upstream: Jeff Zucker <jeff$vpservices,com>

%define real_name DBD-File
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

Summary: Base class for writing DBI drivers for plain files
Name: perl-DBD-File
Version: 0.33
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DBD-File/

Source: http://www.cpan.org/modules/by-module/DBD/DBD-File-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This module is currently not directly usable, rather it is a base subclass
for modules like DBD::CSV and DBD::AnyData.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS="vendor" \
	PREFIX=%{buildroot}%{_prefix}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib} \
	%{buildroot}%{perl_vendorarch}
%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/DBD/File.pm

%changelog
* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 0.33-1
- Updated to release 0.33.

* Tue Mar  1 2005 Dries Verachtert <dries@ulyssis.org> - 0.22-1
- Initial package.
