# $Id$
# Upstream: Eric J. Roode <eric.roode.cpan@gmail.com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)
%define real_name Iterator-Util

Summary: Essential utilities for the Iterator class.
Name: perl-Iterator-Util
Version: 0.02
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Iterator-Util

Source: http://search.cpan.org/CPAN/authors/id/R/RO/ROODE/Iterator-Util-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl(Exception::Class) >= 1.21
BuildRequires: perl(Iterator) >= 0.01
BuildRequires: perl(Test::Simple) >= 0.40
Requires: perl(Exception::Class) >= 1.21
Requires: perl(Iterator) >= 0.01
Requires: perl(Test::Simple) >= 0.40

%filter_from_requires /^perl*/d
%filter_setup

%description
This module implements many useful functions for creating and manipulating iterator objects.

An "iterator" is an object, represented as a code block that generates the "next value" of a sequence, and generally implemented as a closure. For further information, including a tutorial on using iterator objects, see the Iterator documentation.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} 

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Iterator::Util.3pm*
%{perl_vendorlib}/Iterator/Util.pm

%changelog
* Wed Feb 03 2010 Christoph Maser <cmr@financial.com> - 0.03-1
- initial package

