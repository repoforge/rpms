# $Id$

# Authority: dries
# Upstream: Ken Williams <ken$mathforum,org>


# Todo: package YAML, ExtUtils::ParseXS

%define real_name Module-Build
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: System for building perl modules
Name: perl-Module-Build
Version: 0.26
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Module-Build/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://search.cpan.org/CPAN/authors/id/K/KW/KWILLIAMS/Module-Build-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl-Archive-Tar
Requires: perl-Archive-Tar

%description
"Module::Build" is a system for building, testing, and installing Perl
modules. It is meant to be an alternative to "ExtUtils::MakeMaker".
Developers may alter the behavior of the module through subclassing in a
much more straightforward way than with "MakeMaker". It also does not
require a "make" on your system - most of the "Module::Build" code is
pure-perl and written in a very cross-platform way.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" destdir="%{buildroot}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README Changes
%doc %{_mandir}/man?/*
%{perl_vendorlib}/Module/Build.pm
%{perl_vendorlib}/Module/Build
%{_bindir}/config_data

%changelog
* Wed Oct 20 2004 Dries Verachtert <dries@ulyssis.org> - 0.26-1
- Update to release 0.26.

* Sat Jun 5 2004 Dries Verachtert <dries@ulyssis.org> - 0.25-1
- Initial package.
