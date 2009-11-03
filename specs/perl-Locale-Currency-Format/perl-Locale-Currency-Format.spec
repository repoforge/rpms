# $Id$
# Authority: dries
# Upstream: Tan D Nguyen <tdn$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Locale-Currency-Format

Summary: Functions for formatting monetary values
Name: perl-Locale-Currency-Format
Version: 1.28
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Locale-Currency-Format/

Source: http://search.cpan.org/CPAN/authors/id/T/TN/TNGUYEN/Locale-Currency-Format-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Perl functions for formatting monetary values.

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
%doc MANIFEST README
%doc %{_mandir}/man3/Locale::Currency::Format.3pm*
%dir %{perl_vendorlib}/Locale/
%dir %{perl_vendorlib}/Locale/Currency/
#%{perl_vendorlib}/Locale/Currency/Format/
%{perl_vendorlib}/Locale/Currency/Format.pm

%changelog
* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 1.28-1
- Updated to version 1.28.

* Mon Oct 13 2008 Dag Wieers <dag@wieers.com> - 1.26-1
- Updated to release 1.26.

* Sat May 10 2008 Dag Wieers <dag@wieers.com> - 1.25-1
- Updated to release 1.25.

* Mon Feb 25 2008 Dag Wieers <dag@wieers.com> - 1.24-1
- Updated to release 1.24.

* Sun Dec 11 2005 Dries Verachtert <dries@ulyssis.org> - 1.22-1
- Initial package.
