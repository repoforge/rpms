# $Id$

# Authority: dries
# Upstream: Andy Wardley <abw$wardley,org>

%define real_name AppConfig
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Module for reading configuration files and parsing command line args
Name: perl-AppConfig
Version: 1.56
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/AppConfig/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://search.cpan.org/CPAN/authors/id/A/AB/ABW/AppConfig-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

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
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README TODO Changes
%doc %{_mandir}/man3/*
%{perl_vendorlib}/AppConfig.pm
%{perl_vendorlib}/AppConfig/*

%changelog
* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 1.56
- Initial package.

