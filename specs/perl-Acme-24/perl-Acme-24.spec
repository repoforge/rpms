# $Id$
# Authority: dag
# Upstream: Cosimo Streppone <cosimo$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Acme-24

Summary: Your favourite TV-show Acme module
Name: perl-Acme-24
Version: 0.03
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Acme-24/

Source: http://www.cpan.org/modules/by-module/Acme/Acme-24-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Your favourite TV-show Acme module.

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
%doc %{_mandir}/man3/Acme::24.3pm*
%dir %{perl_vendorlib}/Acme/
%{perl_vendorlib}/Acme/24.pm

%changelog
* Mon Sep 28 2009 Christoph Maser <cmr@financial.com> - 0.03-1
- Updated to version 0.03.

* Thu Oct 11 2007 Dag Wieers <dag@wieers.com> - 0.01-1
- Initial package. (using DAR)
