# $Id: $

# Authority: dries
# Upstream:

# Todo: package YAML, ExtUtils::ParseXS

%define real_name Module-Build

Summary: System for building perl modules
Name: perl-Module-Build
Version: 0.25
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Module-Build/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://search.cpan.org/CPAN/authors/id/K/KW/KWILLIAMS/Module-Build-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

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
%{__perl} Makefile.PL INSTALLDIRS="vendor" destdir=%{buildroot}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README Changes
%doc %{_mandir}/man?/*
%{_libdir}/perl5/vendor_perl/*/Module/Build.pm
%{_libdir}/perl5/vendor_perl/*/Module/Build

%changelog
* Sat Jun 5 2004 Dries Verachtert <dries@ulyssis.org> - 0.25-1
- Initial package.
