# $Id$

# Authority: dries
# Upstream: Andy Wardley <abw$wardley,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name AppConfig

Summary: Module for reading configuration files and parsing command line args
Name: perl-AppConfig
Version: 1.66
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/AppConfig/

Source: http://www.cpan.org/modules/by-module/AppConfig/AppConfig-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
AppConfig is a bundle of Perl5 modules for reading configuration files
and parsing command line arguments.  This is a descendant of, and
supercedes the App::Config module.  Functionality is extended over the
final version of App::Config (1.09) and includes many new features.  This
module has been developed and in the process, renamed, as part of an
effort to unify the various Perl modules for parsing configuration files
and command line arguments.

AppConfig has a powerful but easy to use module for parsing configuration
files.  It also has a simple and efficient module for parsing command line
arguments.  For fully-featured command line parsing, a module is provided
for interfacing AppConfig to Johan Vromans' extensive Getopt::Long module.
Johan will continue to develop the functionality of this package and its
features will automatically become available through AppConfig.

All of the modules and features of the AppConfig bundle are easily
accessible through the AppConfig.pm module.

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
%doc Changes LICENSE MANIFEST META.yml README TODO
%doc %{_mandir}/man3/AppConfig.3pm*
%doc %{_mandir}/man3/AppConfig::*.3pm*
%{perl_vendorlib}/AppConfig/
%{perl_vendorlib}/AppConfig.pm

%changelog
* Tue Nov 06 2007 Dag Wieers <dag@wieers.com> - 1.66-1
- Updated to release 1.66.

* Mon Jun 18 2007 Dries Verachtert <dries@ulyssis.org> - 1.65-1
- Updated to release 1.65.

* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 1.64-1
- Updated to release 1.64.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 1.63-1
- Updated to release 1.63.

* Sat Jan 01 2005 Dries Verachtert <dries@ulyssis.org> - 1.56-2
- Fixed the license tag (Thanks to David Necas !)

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 1.56-1
- Initial package.
