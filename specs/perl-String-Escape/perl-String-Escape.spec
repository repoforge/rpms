# $Id$
# Authority: dries
# Upstream: Matthew Simon Cavalletto <simonm$cavalletto,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name String-Escape

Summary: Registry of string functions, including backslash escapes
Name: perl-String-Escape
Version: 2010.002
Release: 1%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/String-Escape/

Source: http://search.cpan.org/CPAN/authors/id/E/EV/EVO/String-Escape-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More)
Requires: perl(Test::More)

%filter_from_requires /^perl*/d
%filter_setup

%description
This module provides a flexible calling interface to some
frequently-performed string conversion functions, including applying
and expanding standard C/Unix-style backslash escapes like \n and \t,
wrapping
and removing double-quotes, and truncating to fit within a desired length.

The escape() function provides for dynamic selection of operations by
using a package hash variable to map escape specification strings to the
functions which implement them. The lookup imposes a bit of a performance
penalty, but allows for some useful late-binding behaviour. Compound
specifications (ex. 'quoted uppercase') are expanded to a list of
functions to be applied in order. Other modules may also register their
functions here for later general use.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}
%{__make} %{?_smp_mflags} test

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/String/Escape.pm

%changelog
* Wed Feb  3 2010 Christoph Maser <cmr@financial.com> - 2010.002-1
- Updated to version 2010.002.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 2002.001-1.2
- Rebuild for Fedora Core 5.

* Sun Mar  6 2005 Dries Verachtert <dries@ulyssis.org> - 2002.001-1
- Initial package.
