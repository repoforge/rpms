# $Id$
# Authority: dries
# Upstream: Michael Schilli <m$perlmeister,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Proc-Simple

Summary: Launch and control background processes
Name: perl-Proc-Simple
Version: 1.26
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Proc-Simple/

Source: http://www.cpan.org/modules/by-module/Proc/Proc-Simple-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
The Proc::Simple package provides objects mimicing real-life processes
from a user's point of view.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

### Clean up docs
find eg/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST MANIFEST.SKIP META.yml README eg/
%doc %{_mandir}/man3/Proc::Simple.3pm*
%dir %{perl_vendorlib}/auto/Proc/
%{perl_vendorlib}/auto/Proc/Simple/
%dir %{perl_vendorlib}/Proc/
#%{perl_vendorlib}/Proc/Simple/
%{perl_vendorlib}/Proc/Simple.pm

%changelog
* Wed Jul 22 2009 Christoph Maser <cmr@financial.com> - 1.26-1
- Updated to version 1.26.

* Mon Jun 22 2009 Christoph Maser <cmr@financial.com> - 1.24-1
- Updated to version 1.24.

* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 1.22-1
- Updated to release 1.22.

* Wed Dec 08 2004 Dries Verachtert <dries@ulyssis.org> - 1.21-1
- Initial package.
