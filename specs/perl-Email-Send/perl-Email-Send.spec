# $Id$
# Authority: dries
# Upstream: Casey West <casey$geeknest,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Email-Send

Summary: Send email
Name: perl-Email-Send
Version: 2.198
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Email-Send/

Source: http://www.cpan.org/modules/by-module/Email/Email-Send-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Email::Address) >= 1.80
BuildRequires: perl(Email::Simple) >= 1.92
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Spec) >= 0
BuildRequires: perl(Module::Pluggable) >= 2.97
BuildRequires: perl(Return::Value) >= 1.28
BuildRequires: perl(Scalar::Util) >= 1.02
BuildRequires: perl(Symbol)
BuildRequires: perl(Test::More) >= 0.47
Requires: perl
Requires: perl(Email::Address) >= 1.80
Requires: perl(Email::Simple) >= 1.92
Requires: perl(ExtUtils::MakeMaker)
Requires: perl(File::Spec) >= 0
Requires: perl(Module::Pluggable) >= 2.97
Requires: perl(Return::Value) >= 1.28
Requires: perl(Scalar::Util) >= 1.02
Requires: perl(Symbol)
Requires: perl(Test::More) >= 0.47
AutoReq: no

%description
Perl module for sending mail.

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

### Clean up docs
find eg/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes LICENSE MANIFEST META.yml README eg/
%doc %{_mandir}/man3/Email::Send.3pm*
%doc %{_mandir}/man3/Email::Send::*.3pm*
%dir %{perl_vendorlib}/Email/
%{perl_vendorlib}/Email/Send/
%{perl_vendorlib}/Email/Send.pm

%changelog
* Wed Jul 15 2009 Christoph Maser <cmr@financial.com> - 2.198-1
- Updated to version 2.198.

* Mon Jul  6 2009 Christoph Maser <cmr@financial.com> - 2.197-1
- Updated to version 2.197.

* Sat Dec 08 2007 Dag Wieers <dag@wieers.com> - 2.192-2
- Added missing dependency to perl(Module::Pluggable). (Max Kanat-Alexander)

* Tue Nov 06 2007 Dag Wieers <dag@wieers.com> - 2.192-1
- Updated to release 2.192.

* Mon Nov 05 2007 Dag Wieers <dag@wieers.com> - 2.190-1
- Updated to release 2.190.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 2.185-1
- Updated to release 2.185.

* Wed Dec 20 2006 Dries Verachtert <dries@ulyssis.org> - 2.183-1
- Initial package.
