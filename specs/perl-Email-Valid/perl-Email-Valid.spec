# $Id$
# Authority: dag
# Upstream: Ricardo SIGNES <rjbs$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Email-Valid

Summary: Check validity of Internet email addresses
Name: perl-Email-Valid
Version: 0.182
Release: 1%{?dist}
License: distributable
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Email-Valid/

Source: http://www.cpan.org/modules/by-module/Email/Email-Valid-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
# From yaml requires
BuildRequires: perl(Mail::Address)
BuildRequires: perl(Net::DNS)
BuildRequires: perl(Test::More)

Requires: perl

%description
Check validity of Internet email addresses

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
%doc Changes LICENSE MANIFEST META.yml README
%doc %{_mandir}/man3/Email::Valid.3pm*
%dir %{perl_vendorlib}/Email/
#%{perl_vendorlib}/Email/Valid/
%{perl_vendorlib}/Email/Valid.pm

%changelog
* Mon Sep 14 2009 Christoph Maser <cmr@financial.com> - 0.182-1
- Updated to version 0.182.

* Mon Jul  6 2009 Christoph Maser <cmr@financial.com> - 0.181-1
- Updated to version 0.181.

* Fri Nov 09 2007 Dag Wieers <dag@wieers.com> - 0.179-1
- Updated to release 0.179.

* Sat Aug 07 2004 Dag Wieers <dag@wieers.com> - 0.15-1
- Initial package. (using DAR)
