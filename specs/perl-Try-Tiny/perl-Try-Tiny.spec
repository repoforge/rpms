# $Id$
# Authority: shuff
# Upstream: Yuval Kogman <nothingmuch$woobling,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Try-Tiny

Summary: minimal try/catch with proper localization of $@
Name: perl-%{real_name}
Version: 0.04
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Try-Tiny/

Source: http://search.cpan.org/CPAN/authors/id/N/NU/NUFFIN/Try-Tiny-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More)

%description
This module provides bare bones try/catch statements that are designed to
minimize common mistakes with eval blocks, and NOTHING else.

This is unlike TryCatch which provides a nice syntax and avoids adding another
call stack layer, and supports calling return from the try block to return from
the parent subroutine. These extra features come at a cost of a few
dependencies, namely Devel::Declare and Scope::Upper which are occasionally
problematic, and the additional catch filtering uses Moose type constraints
which may not be desirable either.

The main focus of this module is to provide simple and reliable error handling
for those having a hard time installing TryCatch, but who still want to write
correct eval blocks without 5 lines of boilerplate each time.

It's designed to work as correctly as possible in light of the various
pathological edge cases (see BACKGROUND) and to be compatible with any style of
error values (simple strings, references, objects, overloaded objects, etc).

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
%doc Changes MANIFEST META.yml SIGNATURE
%doc %{_mandir}/man?/*
%dir %{perl_vendorlib}/Try/
%{perl_vendorlib}/Try/*

%changelog
* Wed Feb  3 2010 Christoph Maser <cmr@financial.com> - 0.04-1
- Updated to version 0.04.

* Tue Dec 01 2009 Steve Huff <shuff@vecna.org> - 0.02-1
- Initial package.

