# $Id$

# Authority: dries
# Upstream: Marcel Grünauer <marcel$cpan,org>

%define real_name YAML-Active
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Combine data and logic in YAML
Name: perl-YAML-Active
Version: 1.00
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/YAML-Active/

Source: http://search.cpan.org/CPAN/authors/id/M/MA/MARCEL/YAML-Active-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl-Module-Build

%description
YAML is an intuitive way to describe nested data structures. This module
extends YAML's capabilities so that it ceases to be a static data
structure and become something more active, with data and logic
combined. This makes the logic reusable since it is bound to the data
structure. Without "YAML::Active", you have to load the YAML data, then
process it in some way. The logic describing which parts of the data
have to be processed and how was separated from the data. Using
"YAML::Active", the description of how to process the data can be
encapsulated in the data structure itself.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" destdir=%{buildroot}
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README Changes
%doc %{_mandir}/man3/*
%{perl_vendorlib}/YAML/Active.pm

%changelog
* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 1.00-1
- Initial package.
