# $Id$
# Authority: dries
# Upstream: Chris Williams <chris@bingosnet.co.uk>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name File-Fetch

Summary: Generic file fetching mechanism
Name: perl-File-Fetch
Version: 0.24
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/File-Fetch/

Source: http://search.cpan.org/CPAN/authors/id/B/BI/BINGOS/File-Fetch-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Basename)
BuildRequires: perl(File::Copy)
BuildRequires: perl(File::Path)
BuildRequires: perl(File::Spec) >= 0.82
BuildRequires: perl(IPC::Cmd) >= 0.42
BuildRequires: perl(Locale::Maketext::Simple)
BuildRequires: perl(Module::Load::Conditional) >= 0.04
BuildRequires: perl(Params::Check) >= 0.07
BuildRequires: perl(Test::More)
Requires: perl(File::Basename)
Requires: perl(File::Copy)
Requires: perl(File::Path)
Requires: perl(File::Spec) >= 0.82
Requires: perl(IPC::Cmd) >= 0.42
Requires: perl(Locale::Maketext::Simple)
Requires: perl(Module::Load::Conditional) >= 0.04
Requires: perl(Params::Check) >= 0.07
Requires: perl(Test::More)

%filter_from_requires /^perl*/d
%filter_setup

%description
A generic file fetching mechanism.

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
%doc CHANGES MANIFEST META.yml README
%doc %{_mandir}/man3/File::Fetch*
%dir %{perl_vendorlib}/File/
%{perl_vendorlib}/File/Fetch.pm

%changelog
* Thu Jan  7 2010 Christoph Maser <cmr@financial.com> - 0.24-1
- Updated to version 0.24.

* Wed Dec 30 2009 Christoph Maser <cmr@financial.com> - 0.22-1
- Updated to version 0.22.

* Sun Jul  5 2009 Christoph Maser <cmr@financial.com> - 0.20-1
- Updated to version 0.20.

* Mon Oct 13 2008 Dag Wieers <dag@wieers.com> - 0.16-1
- Updated to release 0.16.

* Wed Jan 23 2008 Dag Wieers <dag@wieers.com> - 0.14-1
- Updated to release 0.14.

* Mon Nov 19 2007 Dag Wieers <dag@wieers.com> - 0.12-1
- Updated to release 0.12.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.10-1
- Updated to release 0.10.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.08-1
- Updated to release 0.08.

* Thu Mar 31 2005 Dries Verachtert <dries@ulyssis.org> - 0.07-1
- Initial package.
