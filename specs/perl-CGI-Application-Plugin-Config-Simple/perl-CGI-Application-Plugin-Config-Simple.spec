# $Id$
# Upstream: Michael Peters <mpeters$plusthree.com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name CGI-Application-Plugin-Config-Simple

Summary: Add Config::Simple support to CGI::Application
Name: perl-CGI-Application-Plugin-Config-Simple
Version: 1.01
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/CGI-Application-Plugin-Config-Simple/

Source: http://www.cpan.org/modules/by-module/CGI/CGI-Application-Plugin-Config-Simple-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
Requires: perl-CGI-Application >= 3.21
Requires: perl-Config-Simple

%description
This module acts as a plugin for Config::Simple to be easily used inside
of a CGI::Application module. It does not provide every method available
from Config::Simple but rather easy access to your configuration
variables. It does however provide direct access to the underlying
Config::General object created if you want to use it's full power.

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
%dir %{perl_vendorlib}/CGI/Application/Plugin
%dir %{perl_vendorlib}/CGI/Application/Plugin/Config
%{perl_vendorlib}/CGI/Application/Plugin/Config/Simple.pm

%changelog
* Thu Jun 28 2012 IWAI, Masaharu <iwaim.sub@gmail.com> - 1.01
- Initial package.

