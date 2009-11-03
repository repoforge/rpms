# $Id$
# Authority: dag
# Upstream: Dan Kogai <dankogai$dan,co,jp>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Acme-Bleach-Numerically

Summary: Perl module to fit the whole world between 0 and 1
Name: perl-Acme-Bleach-Numerically
Version: 0.04
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Acme-Bleach-Numerically/

Source: http://www.cpan.org/modules/by-module/Acme/Acme-Bleach-Numerically-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 2:5.8.1
Requires: perl >= 2:5.8.1

%description
perl-Acme-Bleach-Numerically is a Perl module to fit the whole world
between 0 and 1.

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
%doc %{_mandir}/man3/Acme::Bleach::Numerically.3pm*
%dir %{perl_vendorlib}/Acme/
%dir %{perl_vendorlib}/Acme/Bleach/
%{perl_vendorlib}/Acme/Bleach/Numerically.pm

%changelog
* Thu Oct 11 2007 Dag Wieers <dag@wieers.com> - 0.04-1
- Initial package. (using DAR)
