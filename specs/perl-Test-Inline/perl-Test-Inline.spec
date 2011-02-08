# $Id$
# Authority: dag
# Upstream: Adam Kennedy <adamk$cpan,org>


%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Test-Inline

Summary: Embed your tests in your code, next to what is being tested
Name: perl-Test-Inline
Version: 2.212
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Test-Inline/

Source: http://search.cpan.org/CPAN/authors/id/A/AD/ADAMK/Test-Inline-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl(Algorithm::Dependency) >= 1.02
BuildRequires: perl(Config::Tiny) >= 2.00
BuildRequires: perl(ExtUtils::MakeMaker) 
BuildRequires: perl(File::Find::Rule) >= 0.26
BuildRequires: perl(File::Flat) >= 1.00
BuildRequires: perl(File::Remove) >= 0.37
BuildRequires: perl(File::Slurp) >= 9999.04
BuildRequires: perl(File::Spec) >= 0.80
BuildRequires: perl(File::chmod) >= 0.31
BuildRequires: perl(Getopt::Long) >= 2.34
BuildRequires: perl(List::Util) >= 1.19
BuildRequires: perl(Params::Util) >= 0.21
BuildRequires: perl(Pod::Tests) >= 0.18
BuildRequires: perl(Test::ClassAPI) >= 1.02
BuildRequires: perl(Test::More) >= 0.42
BuildRequires: perl(Test::Script) >= 1.02
BuildRequires: perl >= v5.6.0
Requires: perl(Algorithm::Dependency) >= 1.02
Requires: perl(Config::Tiny) >= 2.00
Requires: perl(File::Find::Rule) >= 0.26
Requires: perl(File::Flat) >= 1.00
Requires: perl(File::Remove) >= 0.37
Requires: perl(File::Slurp) >= 9999.04
Requires: perl(File::Spec) >= 0.80
Requires: perl(File::chmod) >= 0.31
Requires: perl(Getopt::Long) >= 2.34
Requires: perl(List::Util) >= 1.19
Requires: perl(Params::Util) >= 0.21
Requires: perl(Pod::Tests) >= 0.18
Requires: perl >= v5.6.0

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup


%description
Test::Inline is a way to embed tests in the same file as your source
code rather than in a seperate file.  The idea is, the closer your
tests are to your code and docs, the more likely you'll keep them up
to date.

%prep
%setup -n %{real_name}-%{version}
%{__cat} <<EOF >%{_tmppath}/%{name}-filter-requirements.sh
#!/bin/bash
%{__perl_requires} $* | grep -v '^perl(script)$'
EOF
%{__chmod} +x %{_tmppath}/%{name}-filter-requirements.sh
%define __perl_requires %{_tmppath}/%{name}-filter-requirements.sh

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}
%{__make} test

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
%doc %{_mandir}/man1/inline2test.1*
%doc %{_mandir}/man3/Test::Inline.3pm*
%doc %{_mandir}/man3/Test::Inline::*.3pm*
%{_bindir}/inline2test
%dir %{perl_vendorlib}/Test/
%{perl_vendorlib}/Test/Inline/
%{perl_vendorlib}/Test/Inline.pm

%changelog
* Tue Feb  8 2011 Christoph Maser <cmaser@gmx.de> - 2.212-1
- Updated to version 2.212.

* Wed Jul 15 2009 Christoph Maser <cmr@financial.com> - 2.211-1
- Updated to version 2.211.

* Thu Jun 11 2009 Christoph Maser <cmr@financial.com> - 2.210-1
- Updated to version 2.210.

* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 2.207-1
- Updated to release 2.207.

* Mon Sep  3 2007 Dries Verachtert <dries@ulyssis.org> - 2.205-2
- Remove the automatic perl(script) requirement, thanks to Kanwar Ranbir Sandhu.

* Tue Aug 07 2007 Dag Wieers <dag@wieers.com> - 2.205-1
- Updated to release 2.205.

* Mon Jun 05 2006 Dag Wieers <dag@wieers.com> - 2.103-1
- Initial package. (using DAR)
