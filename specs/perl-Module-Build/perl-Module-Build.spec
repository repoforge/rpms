# $Id$
# Authority: dries
# Upstream: Ken Williams <ken$mathforum,org>

# TODO: package YAML, ExtUtils::ParseXS

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Module-Build

Summary: System for building perl modules
Name: perl-Module-Build
Version: 0.33
Release: 1
License: Artistic or GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Module-Build/

Source: http://www.cpan.org/modules/by-module/Module/Module-Build-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Archive::Tar)
BuildRequires: perl(ExtUtils::CBuilder), perl(ExtUtils::Manifest)

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
%doc Changes README
%doc %{_mandir}/man?/*
%{_bindir}/config_data
%dir %{perl_vendorlib}/Module/
%{perl_vendorlib}/Module/Build/
%{perl_vendorlib}/Module/Build.pm

%changelog
* Mon Jun  8 2009 Christoph Maser <cmr@financial.com> - 0.33-1
- Updated to version 0.33.

* Mon Jun 18 2007 Dries Verachtert <dries@ulyssis.org> - 0.2808-1
- Updated to release 0.2808.

* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 0.2806-2
- Rebuild against perl(ExtUtils::CBuilder).

* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 0.2806-1
- Updated to release 0.2806.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 0.2611-1
- Updated to release 0.2611.

* Fri Mar  4 2005 Dries Verachtert <dries@ulyssis.org> - 0.2608-1
- Updated to release 0.2608.

* Wed Dec 29 2004 Dries Verachtert <dries@ulyssis.org> - 0.2607-1
- Updated to release 0.2607.

* Fri Nov  5 2004 Matthias Saou <http://freshrpms.net/> 0.26-2
- Update to 0.2601.
- Change deps to be "perl style".

* Wed Oct 20 2004 Dries Verachtert <dries@ulyssis.org> - 0.26-1
- Update to release 0.26.

* Sat Jun 5 2004 Dries Verachtert <dries@ulyssis.org> - 0.25-1
- Initial package.
