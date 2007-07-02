# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Test-Inline

Summary: Inlining your tests next to the code being tested
Name: perl-Test-Inline
Version: 2.103
Release: 1
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Test-Inline/

Source: http://www.cpan.org/modules/by-module/Test/Test-Inline-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(Test::More) >= 0.47, perl(Test::ClassAPI) >= 1.02
BuildRequires: perl(File::Spec) >= 0.80, perl(List::Util) >= 1.11
BuildRequires: perl(GetOpt::Long) >= 2.34, perl(File::Slurp) >= 9999.04
BuildRequires: perl(File::Find::Rule) >= 0.26, perl(Config::Tiny) >= 2.00
BuildRequires: perl(Params::Util) >= 0.05, perl(Class::Autouse) >= 1.15
BuildRequires: perl(Algorithm::Dependency) >= 1.02, perl(File::Flat) >= 0.95
BuildRequires: perl(Pod::Tests) >= 0.18

Requires: perl

%description
Test::Inline is a way to embed tests in the same file as your source
code rather than in a seperate file.  The idea is, the closer your
tests are to your code and docs, the more likely you'll keep them up
to date.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL PREFIX="%{buildroot}%{_prefix}" INSTALLDIRS="vendor"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES LICENSE MANIFEST README
%doc %{_mandir}/man3/*.3*
%dir %{perl_vendorlib}/Apache/
%{perl_vendorlib}/Apache/ASP/

%changelog
* Mon Jun 05 2006 Dag Wieers <dag@wieers.com> - 2.103-1
- Initial package. (using DAR)
