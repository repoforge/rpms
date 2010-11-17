# $Id$
# Authority: dag

### EL6 ships with perl-Log-Message-Simple-0.04-115.el6
%{?el6:# Tag: rfx}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Log-Message-Simple

Summary: Standardized logging facilities using Log::Message perl module
Name: perl-Log-Message-Simple
Version: 0.06
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Log-Message-Simple/

Source: http://www.cpan.org/modules/by-module/Log/Log-Message-Simple-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
# From yaml build_requires
BuildRequires: perl(ExtUtils::MakeMaker)
# From yaml requires
BuildRequires: perl(Carp)
BuildRequires: perl(Log::Message)
BuildRequires: perl(Test::More)


%description
This module provides standardized logging facilities using the Log::Message
module.

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
%doc CHANGES MANIFEST META.yml README
%doc %{_mandir}/man3/Log::Message::Simple.3pm*
%dir %{perl_vendorlib}/Log/
%dir %{perl_vendorlib}/Log/Message/
%{perl_vendorlib}/Log/Message/Simple.pm

%changelog
* Mon Sep 14 2009 Christoph Maser <cmr@financial.com> - 0.06-1
- Updated to version 0.06.

* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 0.04-1
- Updated to release 0.04.

* Mon Jun 18 2007 Dries Verachtert <dries@ulyssis.org> - 0.02-1
- Updated to release 0.02.

* Mon May 29 2006 Dag Wieers <dag@wieers.com> - 0.01-1
- Initial package. (using DAR)
