# $Id$
# Authority: dries
# Upstream: Hiroo HAYASHI <hiroo,hayashi$computer,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define real_name Term-ReadLine-Gnu

# todo mv dir, wrong name

Summary: Extension for the GNU Readline/History library
Name: perl-Term-ReadLine-Gnu
Version: 1.15
Release: 2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Term-ReadLine-Gnu/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://search.cpan.org/CPAN/authors/id/H/HA/HAYASHI/Term-ReadLine-Gnu-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, readline-devel

%description
Term::ReadLine::Gnu (TRG) is an implementation of the
interface to the GNU Readline Library.  This module gives you
input line editing facility, input history management
facility, word completion facility, etc.  It uses the real GNU
Readline Library and has the interface with the almost all
variables and functions which are documented in the GNU
Readline/History Library.  So you can program your custom
editing function, your custom completion function, and so on
with Perl.  TRG may be useful for a C programmer to prototype
a program which uses the GNU Readline Library.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL \
	PREFIX="%{buildroot}%{_prefix}" \
	INSTALLDIRS="vendor"
%{__make} %{?_smp_mflags} \
	OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/*/.packlist

%{__perl} -pi -e "s|^#!/.*bin/perl|#!%{__perl}|i;" %{buildroot}%{perl_vendorarch}/Term/ReadLine/Gnu/*.pm

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%{_mandir}/man3/*
%{perl_vendorarch}/Term/ReadLine/Gnu*
%{perl_vendorarch}/auto/Term/ReadLine/Gnu/*

%changelog
* Sat Jan 01 2005 Dries Verachtert <dries@ulyssis.org> - 1.15-2
- Fixed the license tag (Thanks to David Necas !)

* Wed Oct 20 2004 Dries Verachtert <dries@ulyssis.org> - 1.15-1
- Update to release 1.15.

* Wed Jun 16 2004 Dries Verachtert <dries@ulyssis.org> - 1.14-1
- Initial package.
