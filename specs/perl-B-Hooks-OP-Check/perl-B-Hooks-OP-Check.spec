# $Id$
# Authority: cmr
# Upstream: Florian Ragwitz <rafl$debian,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name B-Hooks-OP-Check

Summary: Wrap OP check callbacks
Name: perl-B-Hooks-OP-Check
Version: 0.18
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/B-Hooks-OP-Check/

Source: http://www.cpan.org/modules/by-module/B/B-Hooks-OP-Check-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
# From yaml build_requires
BuildRequires: perl(ExtUtils::Depends)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More)
# From yaml requires
BuildRequires: perl(parent)
BuildRequires: perl >= 5.8.1


%description
Wrap OP check callbacks.

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

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST MANIFEST.SKIP META.yml README
%doc %{_mandir}/man3/B::Hooks::OP::Check.3pm*
%dir %{perl_vendorarch}/auto/B/
%dir %{perl_vendorarch}/auto/B/Hooks/
%dir %{perl_vendorarch}/auto/B/Hooks/OP/
%{perl_vendorarch}/auto/B/Hooks/OP/Check/
%{perl_vendorarch}/B/Hooks/OP/Check/Install/Files.pm
%{perl_vendorarch}/B/Hooks/OP/Check/Install/hook_op_check.h
%dir %{perl_vendorarch}/B/
%dir %{perl_vendorarch}/B/Hooks/
%dir %{perl_vendorarch}/B/Hooks/OP/
%{perl_vendorarch}/B/Hooks/OP/Check.pm

%changelog
* Sat Aug 22 2009 Christoph Maser <cmr@financial.com> - 0.18-1
- Initial package. (using DAR)
