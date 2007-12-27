# $Id$
# Authority: dag
# Upstream: Adam Kennedy <adamk$cpan,org>

%{?dtag: %{expand: %%define %dtag 1}}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Test-Inline

Summary: Embed your tests in your code, next to what is being tested
Name: perl-Test-Inline
Version: 2.208
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Test-Inline/

Source: http://www.cpan.org/modules/by-module/Test/Test-Inline-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.005
BuildRequires: perl(Test::ClassAPI) >= 1.02
BuildRequires: perl(Test::More) >= 0.42
BuildRequires: perl(Test::Script)
#BuildRequires: perl(Test::Script) >= 1.02
BuildRequires: perl(File::Spec) >= 0.80
BuildRequires: perl(List::Util) >= 1.11
#BuildRequires: perl(GetOpt::Long)
BuildRequires: perl(Getopt::Long) >= 2.34
BuildRequires: perl(File::Slurp) >= 9999.04
BuildRequires: perl(File::Find::Rule) >= 0.26
BuildRequires: perl(Config::Tiny) >= 2.00
BuildRequires: perl(Params::Util) >= 0.05
BuildRequires: perl(Class::Autouse) >= 1.15
BuildRequires: perl(Algorithm::Dependency) >= 1.02
BuildRequires: perl(File::Flat) >= 0.95
BuildRequires: perl(Pod::Tests) >= 0.18
Requires: perl >= 0:5.005

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
* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 2.207-1
- Updated to release 2.207.

* Mon Sep  3 2007 Dries Verachtert <dries@ulyssis.org> - 2.205-2
- Remove the automatic perl(script) requirement, thanks to Kanwar Ranbir Sandhu.

* Tue Aug 07 2007 Dag Wieers <dag@wieers.com> - 2.205-1
- Updated to release 2.205.

* Mon Jun 05 2006 Dag Wieers <dag@wieers.com> - 2.103-1
- Initial package. (using DAR)
