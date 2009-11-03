# $Id$
# Authority: dag
# Upstream: José Alves de Castro <cog$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Acme-BooK-Is-My-Bitch

Summary: Perl module bout BooK is my Bitch
Name: perl-Acme-BooK-Is-My-Bitch
Version: 0.02
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Acme-BooK-Is-My-Bitch/

Source: http://www.cpan.org/modules/by-module/Acme/Acme-BooK-Is-My-Bitch-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Acme-BooK-Is-My-Bitch is a Perl module bout BooK is my Bitch.

This package contains the following Perl module:

    Acme::BooK::Is::My::Bitch

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
%doc %{_mandir}/man3/Acme::BooK::Is::My::Bitch.3pm*
%dir %{perl_vendorlib}/Acme/
%dir %{perl_vendorlib}/Acme/BooK/
%dir %{perl_vendorlib}/Acme/BooK/Is/
%dir %{perl_vendorlib}/Acme/BooK/Is/My/
%{perl_vendorlib}/Acme/BooK/Is/My/Bitch.pm

%changelog
* Thu Oct 11 2007 Dag Wieers <dag@wieers.com> - 0.02-1
- Initial package. (using DAR)
