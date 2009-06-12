# $Id$
# Authority: dries
# Upstream: Hiroo HAYASHI <hiroo,hayashi$computer,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Term-ReadLine-Gnu

# todo mv dir, wrong name

Summary: Extension for the GNU Readline/History library
Name: perl-Term-ReadLine-Gnu
Version: 1.19
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Term-ReadLine-Gnu/

Source: http://www.cpan.org/modules/by-module/Term/Term-ReadLine-Gnu-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: readline-devel

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
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

### Clean up docs
find eg/ -type f -exec %{__chmod} a-x {} \;

%{__perl} -pi -e "s|^#!/.*bin/perl|#!%{__perl}|i;" %{buildroot}%{perl_vendorarch}/Term/ReadLine/Gnu/*.pm

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc INSTALL MANIFEST META.yml README eg/
%doc %{_mandir}/man3/Term::ReadLine::Gnu.3pm*
%dir %{perl_vendorarch}/auto/Term/
%dir %{perl_vendorarch}/auto/Term/ReadLine/
%{perl_vendorarch}/auto/Term/ReadLine/Gnu/
%dir %{perl_vendorarch}/Term/
%dir %{perl_vendorarch}/Term/ReadLine/
%{perl_vendorarch}/Term/ReadLine/Gnu/
%{perl_vendorarch}/Term/ReadLine/Gnu.pm

%changelog
* Fri Jun 12 2009 Christoph Maser <cmr@financial.com> - 1.19-1
- Updated to version 1.19.

* Thu Feb 21 2008 Dag Wieers <dag@wieers.com> - 1.17a-1
- Updated to release 1.17a.

* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 1.16-1
- Updated to release 1.16.

* Sat Jan 01 2005 Dries Verachtert <dries@ulyssis.org> - 1.15-2
- Fixed the license tag (Thanks to David Necas !)

* Wed Oct 20 2004 Dries Verachtert <dries@ulyssis.org> - 1.15-1
- Update to release 1.15.

* Wed Jun 16 2004 Dries Verachtert <dries@ulyssis.org> - 1.14-1
- Initial package.
