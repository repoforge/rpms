# $Id$
# Authority: dries
# Upstream: Adam Kennedy <adamk$cpan,org>

### EL6 ships with perl-Module-Install-0.91-4.el6
### RFXed since requires Archive::Tar >= 1.44 from RFX
# Tag: rfx

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Module-Install

Summary: Standalone, extensible Perl module installer
Name: perl-Module-Install
Version: 1.06
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Module-Install/

Source: http://search.cpan.org/CPAN/authors/id/A/AD/ADAMK/Module-Install-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Archive::Tar) >= 1.44
#BuildRequires: perl(Devel::PPPort) >= 3.16
BuildRequires: perl(Devel::PPPort)
#BuildRequires: perl(ExtUtils::Install) >= 1.52
BuildRequires: perl(ExtUtils::Install)
#BuildRequires: perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(ExtUtils::ParseXS) >= 2.19
BuildRequires: perl(File::Remove) >= 1.42
#BuildRequires: perl(File::Spec) >= 3.2701
BuildRequires: perl(File::Spec)
BuildRequires: perl(JSON) >= 2.14
BuildRequires: perl(Module::Build) >= 0.2804
BuildRequires: perl(Module::CoreList) >= 2.17
BuildRequires: perl(Module::ScanDeps) >= 0.89
BuildRequires: perl(PAR::Dist) >= 0.29
BuildRequires: perl(Parse::CPAN::Meta) >= 1.39
#BuildRequires: perl(Test::Harness) >= 3.13
BuildRequires: perl(Test::Harness)
#BuildRequires: perl(Test::More) >= 0.86
BuildRequires: perl(Test::More)
BuildRequires: perl(YAML::Tiny) >= 1.38
BuildRequires: perl >= 5.005
Requires: perl(Archive::Tar) >= 1.44
#Requires: perl(Devel::PPPort) >= 3.16
Requires: perl(Devel::PPPort)
#Requires: perl(ExtUtils::Install) >= 1.52
Requires: perl(ExtUtils::Install)
Requires: perl(ExtUtils::ParseXS) >= 2.19
Requires: perl(File::Remove) >= 1.42
#Requires: perl(File::Spec) >= 3.2701
Requires: perl(File::Spec)
Requires: perl(JSON) >= 2.14
Requires: perl(Module::Build) >= 0.2804
Requires: perl(Module::CoreList) >= 2.17
Requires: perl(Module::ScanDeps) >= 0.89
Requires: perl(PAR::Dist) >= 0.29
Requires: perl(Parse::CPAN::Meta) >= 1.39
Requires: perl(YAML::Tiny) >= 1.38
Requires: perl >= 5.005

%filter_from_requires /^perl*/d
%filter_setup


%description
Module::Install is a standalone, extensible installer for Perl modules.  It is
designed to be a drop-in replacement for ExtUtils::MakeMaker, and is a
descendent of CPAN::MakeMaker.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}
%{__make} %{?_smp_mflags} test

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
%doc %{_mandir}/man3/Module::AutoInstall.3pm.gz
%doc %{_mandir}/man3/Module::Install.3pm.gz
%doc %{_mandir}/man3/Module::Install::*.3pm.gz
%doc %{_mandir}/man3/inc::Module::Install.3pm*
%doc %{_mandir}/man3/inc::Module::Install::DSL.3pm*
%dir %{perl_vendorlib}/Module/
%{perl_vendorlib}/Module/AutoInstall.pm
%{perl_vendorlib}/Module/Install/
%{perl_vendorlib}/Module/Install.pm
%{perl_vendorlib}/Module/Install.pod
%dir %{perl_vendorlib}/inc/
%dir %{perl_vendorlib}/inc/Module/
%{perl_vendorlib}/inc/Module/Install/DSL.pm
%{perl_vendorlib}/inc/Module/Install.pm
%exclude %{perl_vendorlib}/auto/share/

%changelog
* Sat Apr 14 2012 Denis Fateyev <denis@fateyev.com> - 1.06-1
- Updated to version 1.06, moved to RFX.

* Sat Feb 05 2011 Denis Fateyev <denis@fateyev.com> - 1.00-1
- Updated to version 1.00.

* Wed Feb  3 2010 Christoph Maser <cmr@financial.com> - 0.92-1
- Updated to version 0.92.

* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 0.91-1
- Updated to version 0.91.

* Wed Oct 08 2008 Dag Wieers <dag@wieers.com> - 0.77-1
- Updated to release 0.77.

* Mon Jun 23 2008 Dag Wieers <dag@wieers.com> - 0.75-1
- Updated to release 0.75.

* Mon May 05 2008 Dag Wieers <dag@wieers.com> - 0.72-1
- Updated to release 0.72.

* Tue Nov 06 2007 Dag Wieers <dag@wieers.com> - 0.68-1
- Updated to release 0.68.

* Mon Jun 18 2007 Dries Verachtert <dries@ulyssis.org> - 0.67-1
- Updated to release 0.67.

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
