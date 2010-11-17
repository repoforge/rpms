# $Id$
# Authority: dries
# Upstream: Adam Kennedy <adamk$cpan,org>

### EL6 ships with perl-Config-Tiny-2.12-7.1.el6
%{?el6:# Tag: rfx}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Config-Tiny

Summary: Read/Write .ini style files with as little code as possible
Name: perl-Config-Tiny
Version: 2.12
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Config-Tiny/

Source: http://www.cpan.org/modules/by-module/Config/Config-Tiny-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.004
#BuildRequires: perl(ExtUtils::MakeMaker) >= 6.11
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(FindBin) >= 1.42
BuildRequires: perl(Test::More) >= 0.47
Requires: perl >= 0:5.004

%description
Config::Tiny is a perl class to read and write .ini style configuration
files with as little code as possible, reducing load time and memory
overhead. Memory usage is normally scoffed at in Perl, but in my opinion
should be at least kept in mind.

This module is primarily for reading human written files, and anything
we write shouldn't need to have documentation/comments. If you need
something with more power, move up to Config::Simple, Config::General or
one of the many other Config:: modules. To rephrase, Config::Tiny does
not preserve your comments, whitespace, or the order of your config
file.

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
%doc Changes LICENSE MANIFEST META.yml README
%doc %{_mandir}/man3/Config::Tiny.3pm*
%dir %{perl_vendorlib}/Config/
#%{perl_vendorlib}/Config/Tiny/
%{perl_vendorlib}/Config/Tiny.pm

%changelog
* Tue Nov 06 2007 Dag Wieers <dag@wieers.com> - 2.12-1
- Updated to release 2.12.

* Tue Nov 14 2006 Dries Verachtert <dries@ulyssis.org> - 2.10-1
- Updated to release 2.10.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 2.08-1
- Updated to release 2.08.

* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 2.07-1
- Updated to release 2.07.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 2.05-1
- Updated to release 2.05.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 2.04-1
- Updated to release 2.04.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 2.02-1
- Updated to release 2.02.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 2.01-1
- Updated to release 2.01.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 2.00-1
- Initial package.
