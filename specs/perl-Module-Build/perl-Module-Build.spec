# $Id$
# Authority: dries
# Upstream: Ken Williams <ken$mathforum,org>

# TODO: package YAML, ExtUtils::ParseXS

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Module-Build

Summary: System for building perl modules
Name: perl-Module-Build
Version: 0.3601
Release: 1%{?dist}
Epoch: 1
License: Artistic or GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Module-Build/

Source: http://search.cpan.org/CPAN/authors/id/D/DA/DAGOLDEN/Module-Build-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Cwd)
BuildRequires: perl(Data::Dumper)
BuildRequires: perl(ExtUtils::CBuilder) >= 0.27
BuildRequires: perl(ExtUtils::Install)
BuildRequires: perl(ExtUtils::Manifest)
BuildRequires: perl(ExtUtils::Mkbootstrap)
BuildRequires: perl(ExtUtils::ParseXS) >= 2.21
BuildRequires: perl(File::Basename)
BuildRequires: perl(File::Compare)
BuildRequires: perl(File::Copy)
BuildRequires: perl(File::Find)
BuildRequires: perl(File::Path)
BuildRequires: perl(File::Spec) >= 0.82
#BuildRequires: perl(File::Temp) >= 0.15
BuildRequires: perl(File::Temp)
BuildRequires: perl(Getopt::Long)
BuildRequires: perl(IO::File)
BuildRequires: perl(Test::Harness)
#BuildRequires: perl(Test::More) >= 0.49
BuildRequires: perl(Test::More)
BuildRequires: perl(Text::Abbrev)
BuildRequires: perl(Text::ParseWords)
BuildRequires: perl >= 5.006001
Requires: perl(Cwd)
Requires: perl(Data::Dumper)
Requires: perl(ExtUtils::CBuilder) >= 0.27
Requires: perl(ExtUtils::Install)
Requires: perl(ExtUtils::Manifest)
Requires: perl(ExtUtils::Mkbootstrap)
Requires: perl(ExtUtils::ParseXS) >= 2.21
Requires: perl(File::Basename)
Requires: perl(File::Compare)
Requires: perl(File::Copy)
Requires: perl(File::Find)
Requires: perl(File::Path)
Requires: perl(File::Spec) >= 0.82
Requires: perl(Getopt::Long)
Requires: perl(IO::File)
Requires: perl(Test::Harness)
Requires: perl(Text::Abbrev)
Requires: perl(Text::ParseWords)
Requires: perl >= 5.006001

%filter_from_requires /^perl*/d
%filter_setup


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
%{perl_vendorlib}/inc/latest.pm
%{perl_vendorlib}/inc/latest/private.pm

%changelog
* Tue Dec 22 2009 Christoph Maser <cmr@financial.com> - 0.3601-1
- Updated to version 0.3601.

* Tue Sep  8 2009 Christoph Maser <cmr@financial.com> - 0.35-1
- Updated to version 0.35.

* Thu Jul  9 2009 Christoph Maser <cmr@financial.com> - 0.34-1
- Updated to version 0.34.

* Mon Jun  8 2009 Christoph Maser <cmr@financial.com> - 0.33-2
- Use epoch due to broken version numbers upstream

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
