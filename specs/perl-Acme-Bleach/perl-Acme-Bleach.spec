# $Id$
# Authority: dag
# Upstream: Damian Conway <damian$conway,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Acme-Bleach
%define real_version 1.05

Summary: Perl module named Acme-Bleach
Name: perl-Acme-Bleach
Version: 1.12
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Acme-Bleach/

Source: http://www.cpan.org/modules/by-module/Acme/Acme-Bleach-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Acme-Bleach is a Perl module.

This package contains the following Perl modules:

    Acme::Bleach
    Acme::DWIM

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
%doc %{_mandir}/man3/Acme::Bleach.3pm*
%doc %{_mandir}/man3/Acme::DWIM.3pm*
%doc %{_mandir}/man3/Acme::Morse.3pm*
%dir %{perl_vendorlib}/Acme/
%{perl_vendorlib}/Acme/Bleach.pm
%{perl_vendorlib}/Acme/DWIM.pm
%{perl_vendorlib}/Acme/Morse.pm

%changelog
* Thu Oct 11 2007 Dag Wieers <dag@wieers.com> - 1.12-1
- Initial package. (using DAR)
