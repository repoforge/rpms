# $Id$
# Authority: dries
# Upstream: Ricardo SIGNES <rjbs$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Acme-ProgressBar

Summary: Simple progress bar for the patient
Name: perl-Acme-ProgressBar
Version: 1.125
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Acme-ProgressBar/

Source: http://www.cpan.org/modules/by-module/Acme/Acme-ProgressBar-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Exporter)
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Simple progress bar for the patient.

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
%doc Changes LICENSE MANIFEST META.yml README
%doc %{_mandir}/man3/Acme::ProgressBar.3pm*
%dir %{perl_vendorlib}/Acme/
#%{perl_vendorlib}/Acme/ProgressBar/
%{perl_vendorlib}/Acme/ProgressBar.pm

%changelog
* Mon Sep 28 2009 Christoph Maser <cmr@financial.com> - 1.125-1
- Updated to version 1.125.

* Tue Nov 13 2007 Dag Wieers <dag@wieers.com> - 1.124-1
- Updated to release 1.124.

* Tue Nov 06 2007 Dag Wieers <dag@wieers.com> - 1.123-1
- Updated to release 1.123.

* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 1.121-1
- Initial package.
