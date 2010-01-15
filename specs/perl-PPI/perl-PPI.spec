# $Id$
# Authority: dries
# Upstream: Adam Kennedy <adamk@cpan.org>
# ExcludeDist: el4

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name PPI

Summary: Parse and manipulate perl code non-destructively
Name: perl-PPI
Version: 1.208
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/PPI/

Source: http://search.cpan.org/CPAN/authors/id/A/AD/ADAMK/PPI-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
# From yaml build_requires
BuildRequires: perl(Clone) >= 0.30
BuildRequires: perl(Digest::MD5) >= 2.35
#BuildRequires: perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Remove) >= 1.42
BuildRequires: perl(File::Spec) >= 0.84
BuildRequires: perl(IO::String) >= 1.07
BuildRequires: perl(List::MoreUtils) >= 0.16
BuildRequires: perl(List::Util) >= 1.20
BuildRequires: perl(Params::Util) >= 1.00
#BuildRequires: perl(Storable) >= 2.17
BuildRequires: perl(Storable)
BuildRequires: perl(Task::Weaken)
BuildRequires: perl(Test::ClassAPI) >= 1.04
#BuildRequires: perl(Test::More) >= 0.86
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::NoWarnings) >= 0.084
BuildRequires: perl(Test::Object) >= 0.07
BuildRequires: perl(Test::SubCalls) >= 1.07
BuildRequires: perl >= 5.6.0
Requires: perl(Clone) >= 0.30
Requires: perl(Digest::MD5) >= 2.35
Requires: perl(File::Spec) >= 0.84
Requires: perl(IO::String) >= 1.07
Requires: perl(List::MoreUtils) >= 0.16
Requires: perl(List::Util) >= 1.20
Requires: perl(Params::Util) >= 1.00
#Requires: perl(Storable) >= 2.17
Requires: perl(Storable)
Requires: perl(Task::Weaken)
Requires: perl >= 5.6.0

%filter_from_requires /^perl*/d
%filter_setup


%description
This is an in-development package for parsing, manipulating and saving
perl code, without using the perl interpreter, the B modules, or any
other hacks that use perl's inbuilt grammar.

Please note that is project it intended as a mechanism for working with
perl content, NOT to actually compile and run working perl applications.
Thus, it provides only an approximation of the detail and flexibility
available to the real perl parser, if a quite close approximation.

It has been shown many times that it is impossible to FULLY "parse" Perl
code without also executing it. We do not intend to fully parse it, just
get enough details to analyse it, alter it, and save it back without
losing details like whitespace, comments and other stuff lost when using
the B:: modules.

%prep
%setup -n %{real_name}-%{version}

%build
echo | %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
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
%doc %{_mandir}/man3/PPI.3pm*
%doc %{_mandir}/man3/PPI::*.3pm*
%{perl_vendorlib}/PPI/
%{perl_vendorlib}/PPI.pm

%changelog
* Fri Jan 15 2010 Christoph Maser <cmr@financial.com> - 1.208-1
- Updated to version 1.208.

* Tue Sep  1 2009 Christoph Maser <cmr@financial.com> - 1.206-1
- Updated to version 1.206.

* Wed Aug  5 2009 Christoph Maser <cmr@financial.com> - 1.205-1
- Updated to version 1.205.

* Wed Jul  1 2009 Christoph Maser <cmr@financial.com> - 1.203-1
- Updated to version 1.203.

* Tue Nov 06 2007 Dag Wieers <dag@wieers.com> - 1.201-1
- Updated to release 1.201.

* Tue Sep 26 2006 Dries Verachtert <dries@ulyssis.org> - 1.118-1
- Updated to release 1.118.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 1.117-1
- Updated to release 1.117.

* Thu Jun 01 2006 Dries Verachtert <dries@ulyssis.org> - 1.114-1
- Updated to release 1.114.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 1.110-1
- Updated to release 1.110.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 1.109-1
- Updated to release 1.109.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 1.103-1
- Updated to release 1.103.

* Mon Aug 15 2005 Dries Verachtert <dries@ulyssis.org> - 1.002-1
- Updated to release 1.002.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 0.990-1
- Updated to release 0.990.

* Fri Mar  4 2005 Dries Verachtert <dries@ulyssis.org> - 0.902-1
- Updated to release 0.902.

* Wed Dec 29 2004 Dries Verachtert <dries@ulyssis.org> - 0.840-1
- Updated to release 0.840.

* Wed Oct 20 2004 Dries Verachtert <dries@ulyssis.org> - 0.830-1
- Update to release 0.830.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 0.824-1
- Initial package.
