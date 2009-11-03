# $Id$
# Authority: dag
# Upstream: Casey West <casey$geeknest,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name ACME-Error
%define real_version 0.02

Summary: Perl module to never have boring errors again!
Name: perl-ACME-Error
Version: 0.03
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/ACME-Error/

Source: http://www.cpan.org/authors/id/C/CW/CWEST/ACME-Error-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-ACME-Error is a Perl module to never have boring errors again!

This package contains the following Perl modules:

    ACME::Error
    ACME::Error::SHOUT

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
%doc Changes MANIFEST
%doc %{_mandir}/man3/ACME::Error.3pm*
%doc %{_mandir}/man3/ACME::Error::SHOUT.3pm*
%dir %{perl_vendorlib}/ACME/
%{perl_vendorlib}/ACME/Error/
%{perl_vendorlib}/ACME/Error.pm

%changelog
* Thu Oct 11 2007 Dag Wieers <dag@wieers.com> - 0.03-1
- Initial package. (using DAR)
