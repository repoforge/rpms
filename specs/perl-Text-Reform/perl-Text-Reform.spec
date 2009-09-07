# $Id$
# Authority: dries
# Upstream: Damian Conway <damian$conway,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Text-Reform

Summary: Manual text wrapping and reformatting
Name: perl-Text-Reform
Version: 1.20
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Text-Reform/

Source: http://www.cpan.org/modules/by-module/Text/Text-Reform-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Exporter)
BuildRequires: perl(ExtUtils::MakeMaker)

%description
The module supplies a re-entrant, highly configurable replacement
for the built-in Perl format() mechanism.

This package contains the following Perl module:

    Text::Reform

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
%doc Changes MANIFEST README
%doc %{_mandir}/man3/Text::Reform.3pm*
%dir %{perl_vendorlib}/Text/
#%{perl_vendorlib}/Text/Reform/
%{perl_vendorlib}/Text/Reform.pm

%changelog
* Mon Sep  7 2009 Christoph Maser <cmr@financial.com> - 1.20-1
- Updated to version 1.20.

* Sun Dec 19 2004 Dries Verachtert <dries@ulyssis.org> - 1.11
- Initial package.
