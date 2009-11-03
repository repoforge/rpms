# $Id$
# Authority: dries
# Upstream: Jos Boumans <gro,miwd$enak>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name File-Fetch

Summary: Generic file fetching mechanism
Name: perl-File-Fetch
Version: 0.20
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/File-Fetch/

Source: http://www.cpan.org/modules/by-module/File/File-Fetch-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

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
