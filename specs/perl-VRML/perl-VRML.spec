# $Id$
# Authority: dries
# Upstream: Hartmut Palm <palm$gfz-potsdam,de>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name VRML

Summary: Specification independent VRML methods
Name: perl-VRML
Version: 1.04
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/VRML/

Source: http://search.cpan.org/CPAN/authors/id/H/HP/HPALM/VRML-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Specification independent VRML methods (1.0, 2.0, 97).

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README.TXT
%doc %{_mandir}/man3/*
%{perl_vendorlib}/VRML.pm
%{perl_vendorlib}/VRML

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.04-1
- Initial package.
