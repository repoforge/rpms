# $Id$
# Authority: dries
# Upstream: Thomas Linden <tom$daemon,de>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Config-General

Summary: Generic config module
Name: perl-Config-General
Version: 2.44
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Config-General/

Source: http://search.cpan.org/CPAN/authors/id/T/TL/TLINDEN/Config-General-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(File::Glob)
BuildRequires: perl(File::Spec::Functions)
BuildRequires: perl(FileHandle)
BuildRequires: perl(IO::File)
Requires: perl(File::Glob)
Requires: perl(File::Spec::Functions)
Requires: perl(FileHandle)
Requires: perl(IO::File)

%filter_from_requires /^perl*/d
%filter_setup

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
#%patch -p1

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
%doc Changelog MANIFEST README
%doc %{_mandir}/man3/Config::General.3pm*
%doc %{_mandir}/man3/Config::General::*.3pm*
%dir %{perl_vendorlib}/Config/
%{perl_vendorlib}/Config/General/
%{perl_vendorlib}/Config/General.pm

%changelog
* Thu Dec 31 2009 Christoph Maser <cmr@financial.com> - 2.44-1
- Updated to version 2.44.

* Sat Aug 22 2009 Christoph Maser <cmr@financial.com> - 2.43-1
- Updated to version 2.43.

* Tue Mar 17 2009 Dries Verachtert <dries@ulyssis.org> - 2.42-1
- Updated to release 2.42.

* Sun Jun 22 2008 Dag Wieers <dag@wieers.com> - 2.40-1
- Updated to release 2.40.

* Thu Mar 06 2008 Dag Wieers <dag@wieers.com> - 2.38-1
- Updated to release 2.38.

* Tue Dec 04 2007 Dag Wieers <dag@wieers.com> - 2.37-1
- Updated to release 2.37.

* Mon Oct 22 2007 Dries Verachtert <dries@ulyssis.org> - 2.36-1
- Updated to release 2.36.

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
