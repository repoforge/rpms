# $Id$

# Authority: dries
# Upstream: Thomas Linden <tom$daemon,de>

%define real_name Config-General
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Generic config module
Name: perl-Config-General
Version: 2.27
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Config-General/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://search.cpan.org/CPAN/authors/id/T/TL/TLINDEN/Config-General-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
This module opens a config file and parses it's contents
for you. After parsing the module returns a hash structure
which contains the representation of the config file.
       
The format of config files supported by Config::General is
inspired by the well known apache config format, in fact,
this module is 100% read-compatible to apache configs, but
you can also just use simple name/value pairs in your config
files.

In addition to the capabilities of a apache config file
it supports some enhancements such as here-documents, C-
style comments or multiline options. It is also possible to
save the config back to disk, which makes the module a
perfect backend for configuration interfaces.

It is possible to use variables in config files and there
exists also support for object oriented access to the
configuration.

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
%doc README Changelog
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Config/General.pm
%{perl_vendorlib}/Config/General/*
%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/.packlist

%changelog
* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 2.27-1
- Initial package.
