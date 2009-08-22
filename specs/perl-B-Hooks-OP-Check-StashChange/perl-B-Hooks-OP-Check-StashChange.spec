# $Id$
# Authority: cmr
# Upstream: Florian Ragwitz <rafl$debian,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name B-Hooks-OP-Check-StashChange

Summary: Invoke callbacks when the stash code is being compiled in changes
Name: perl-B-Hooks-OP-Check-StashChange
Version: 0.06
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/B-Hooks-OP-Check-StashChange/

Source: http://www.cpan.org/modules/by-module/B/B-Hooks-OP-Check-StashChange-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::Depends)
# From yaml build_requires
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More)
# From yaml requires
BuildRequires: perl(B::Hooks::OP::Check) >= 0.14
BuildRequires: perl(parent)


%description
Invoke callbacks when the stash code is being compiled in changes.

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
%doc %{_mandir}/man3/B::Hooks::OP::Check::StashChange.3pm*
%dir %{perl_vendorarch}/auto/B/
%dir %{perl_vendorarch}/auto/B/Hooks/
%dir %{perl_vendorarch}/auto/B/Hooks/OP/
%dir %{perl_vendorarch}/auto/B/Hooks/OP/Check/
%{perl_vendorarch}/auto/B/Hooks/OP/Check/StashChange/
%dir %{perl_vendorarch}/B/
%dir %{perl_vendorarch}/B/Hooks/
%dir %{perl_vendorarch}/B/Hooks/OP/
%dir %{perl_vendorarch}/B/Hooks/OP/Check/
%{perl_vendorarch}/B/Hooks/OP/Check/StashChange.pm
%{perl_vendorarch}/B/Hooks/OP/Check/StashChange/Install/Files.pm
%{perl_vendorarch}/B/Hooks/OP/Check/StashChange/Install/hook_op_check_stashchange.h


%changelog
* Sat Aug 22 2009 Christoph Maser <cmr@financial.com> - 0.06-1
- Initial package. (using DAR)
