# $Id$
# Authority: dries
# Upstream: Thomas Linden <tom$daemon,de>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Config-General

Summary: Generic config module
Name: perl-Config-General
Version: 2.33
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Config-General/

Source: http://www.cpan.org/modules/by-module/Config/Config-General-%{version}.tar.gz
Patch: carp-heavy.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
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
%patch -p1

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changelog README
%doc %{_mandir}/man3/Config::General*
%{perl_vendorlib}/Config/General.pm
%{perl_vendorlib}/Config/General/

%changelog
* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 2.33-1
- Updated to release 2.33.

* Tue Apr 17 2007 Dries Verachtert <dries@ulyssis.org> - 2.32-1
- Updated to release 2.32.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 2.31-1
- Updated to release 2.31.

* Sun Dec 04 2005 Dries Verachtert <dries@ulyssis.org> - 2.30-2
- Applied a patch made by Ralph Angenendt which removes the
  dependency on Carp::Heavy.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 2.30-1
- Updated to release 2.30.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 2.29-1
- Updated to release 2.29.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 2.27-1
- Initial package.
