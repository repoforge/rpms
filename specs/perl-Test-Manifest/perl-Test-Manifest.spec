# $Id$
# Authority: dries
# Upstream: brian d foy <bdfoy$cpan,org>

### EL6 ships with perl-Test-Manifest-1.22-5.el6
%{?el6:# Tag: rfx}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Test-Manifest

Summary: Interact with a t/test_manifest file
Name: perl-Test-Manifest
Version: 1.23
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Test-Manifest/

Source: http://www.cpan.org/modules/by-module/Test/Test-Manifest-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This module allows you to interact with a t/test_manifest file.

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

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes LICENSE MANIFEST META.yml README examples/
#%doc %{_mandir}/man3/Test::Manifest*
%dir %{perl_vendorlib}/Test/
#%{perl_vendorlib}/Test/Manifest/
%{perl_vendorlib}/Test/Manifest.pm

%changelog
* Mon Jul 20 2009 Christoph Maser <cmr@financial.com> - 1.23-1
- Updated to version 1.23.

* Tue Nov 06 2007 Dag Wieers <dag@wieers.com> - 1.22-1
- Updated to release 1.22

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 1.17-1
- Updated to release 1.17.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 1.14-1
- Updated to release 1.14.

* Wed Oct 20 2004 Dries Verachtert <dries@ulyssis.org> - 1.11-1
- Update to release 1.11.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 0.93-1
- Initial package.
