# $Id$
# Authority: dries
# Upstream: Nathan Wiger <nate$wiger,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Apache-ConfigFile

Summary: Parse an Apache style httpd.conf configuration file
Name: perl-Apache-ConfigFile
Version: 1.18
Release: 1.2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Apache-ConfigFile/

Source: http://search.cpan.org/CPAN/authors/id/N/NW/NWIGER/Apache-ConfigFile-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This module parses the Apache httpd.conf, or any compatible config file,
and provides methods for you to access the values from the config file.
The above examples show basic usage of this module, which boils down to
reading a given config file and then using the "cmd_config()" and
"cmd_context()" functions to access its information.

By default, the config file is parsed more or less "verbatim", meaning
that directives are case-sensitive, variables are not interpolated, and
so forth. These features can be changed by options given to the "read()"
function (see below).

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
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Apache/ConfigFile.pm

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.18-1
- Initial package.
