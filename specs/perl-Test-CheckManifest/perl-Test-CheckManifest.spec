# $Id$
# Authority: dries
# Upstream: Renee Baecker <module$renee-baecker,de>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Test-CheckManifest

Summary: Checks manifest files
Name: perl-Test-CheckManifest
Version: 1.22
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Test-CheckManifest/

Source: http://search.cpan.org/CPAN/authors/id/R/RE/RENEEB/Test-CheckManifest-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Carp)
BuildRequires: perl(Cwd)
BuildRequires: perl(File::Basename)
BuildRequires: perl(File::Find)
BuildRequires: perl(File::Spec)
BuildRequires: perl(Test::Builder)
Requires: perl(Carp)
Requires: perl(Cwd)
Requires: perl(File::Basename)
Requires: perl(File::Find)
Requires: perl(File::Spec)
Requires: perl(Test::Builder)

%filter_from_requires /^perl*/d
%filter_setup

%description
Checks manifest files.

%prep
%setup -n %{real_name}-%{version}

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Test::CheckManifest.3pm*
%dir %{perl_vendorlib}/Test/
#%{perl_vendorlib}/Test/CheckManifest/
%{perl_vendorlib}/Test/CheckManifest.pm

%changelog
* Tue Feb  8 2011 Christoph Maser <cmaser@gmx.de> - 1.22-1
- Updated to version 1.22.

* Sat Feb  6 2010 Christoph Maser <cmr@financial.com> - 1.2-1
- Updated to version 1.2.

* Wed Dec  9 2009 Christoph Maser <cmr@financial.com> - 1.1-1
- Updated to version 1.1.

* Fri Jan 04 2008 Dag Wieers <dag@wieers.com> - 1.01-1
- Updated to release 1.01.

* Thu Jan 04 2007 Dries Verachtert <dries@ulyssis.org> - 1.0-1
- Updated to release 1.0.

* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.5-1
- Initial package.
