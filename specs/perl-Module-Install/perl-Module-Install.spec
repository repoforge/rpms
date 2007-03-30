# $Id$
# Authority: dries
# Upstream: &#9786;&#21776;&#40179;&#9787; <autrijus$autrijus,org>

##Tag: test

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Module-Install

Summary: Installer for perl modules
Name: perl-Module-Install
Version: 0.64
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Module-Install/

Source: http://www.cpan.org/modules/by-module/Module/Module-Install-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(File::Spec) >= 0.87, perl(Test::Harness) >= 2.03
BuildRequires: perl(Test::More) >= 0.42, perl(Module::ScanDeps) >= 0.28
BuildRequires: perl(Module::CoreList), perl(PAR::Dist) >= 0.03
BuildRequires: perl(Archive::Tar), perl(ExtUtils::Install) >= 0.3
BuildRequires: perl(ExtUtils::ParseXS), perl(Module::Build)
# needed for certain older versions of perl-Module-Build
BuildRequires: perl(YAML::Syck)

%description
Module::Install is a standalone, extensible installer for Perl modules.  It is
designed to be a drop-in replacement for ExtUtils::MakeMaker, and is a
descendent of CPAN::MakeMaker.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/Module/
%{perl_vendorlib}/Module/AutoInstall.pm
%{perl_vendorlib}/Module/Install/
%{perl_vendorlib}/Module/Install.p*
%dir %{perl_vendorlib}/inc/
%dir %{perl_vendorlib}/inc/Module/
%{perl_vendorlib}/inc/Module/Install.pm

%changelog
* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.64-1
- Updated to release 0.64.

* Mon May 29 2006 Dag Wieers <dag@wieers.com> - 0.62-1
- Updated to release 0.62.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.61-1
- Updated to release 0.61.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 0.52-1
- Updated to release 0.52.

* Thu Dec 15 2005 Dries Verachtert <dries@ulyssis.org> - 0.44-1
- Initial package.
