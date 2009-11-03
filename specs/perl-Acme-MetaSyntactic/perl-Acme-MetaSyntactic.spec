# $Id$
# Authority: dag
# Upstream: Philippe "BooK" Bruhat <book$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Acme-MetaSyntactic

Summary: Themed metasyntactic variables names
Name: perl-Acme-MetaSyntactic
Version: 0.99
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Acme-MetaSyntactic/

Source: http://www.cpan.org/modules/by-module/Acme/Acme-MetaSyntactic-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Themed metasyntactic variables names.

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man1/meta.1*
%doc %{_mandir}/man3/Acme::MetaSyntactic.3pm*
%doc %{_mandir}/man3/Acme::MetaSyntactic::*.3pm*
%{_bindir}/meta
%dir %{perl_vendorlib}/Acme/
%{perl_vendorlib}/Acme/MetaSyntactic/
%{perl_vendorlib}/Acme/MetaSyntactic.pm

%changelog
* Fri Nov 23 2007 Dag Wieers <dag@wieers.com> - 0.99-1
- Initial package. (using DAR)
