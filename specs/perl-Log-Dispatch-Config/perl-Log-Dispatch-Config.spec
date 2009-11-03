# $Id$
# Authority: dag
# Upstream: Tatsuhiko Miyagawa <miyagawa$bulknews,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Log-Dispatch-Config

Summary: Perl module that implements Log4j
Name: perl-Log-Dispatch-Config
Version: 1.02
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Log-Dispatch-Config/

Source: http://www.cpan.org/modules/by-module/Log/Log-Dispatch-Config-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Log-Dispatch-Config is a Perl module that implements Log4j.

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
%doc %{_mandir}/man3/Log::Dispatch::Config.3pm*
%doc %{_mandir}/man3/Log::Dispatch::Configurator.3pm*
%doc %{_mandir}/man3/Log::Dispatch::Configurator::AppConfig.3pm*
%dir %{perl_vendorlib}/Log/
%dir %{perl_vendorlib}/Log/Dispatch/
%{perl_vendorlib}/Log/Dispatch/Config.pm
%{perl_vendorlib}/Log/Dispatch/Configurator.pm
%dir %{perl_vendorlib}/Log/Dispatch/Configurator/
%{perl_vendorlib}/Log/Dispatch/Configurator/AppConfig.pm

%changelog
* Tue Nov 13 2007 Dag Wieers <dag@wieers.com> - 1.02-1
- Updated to release 1.02.

* Thu May 03 2007 Dag Wieers <dag@wieers.com> - 1.01-1
- Initial package. (using DAR)
