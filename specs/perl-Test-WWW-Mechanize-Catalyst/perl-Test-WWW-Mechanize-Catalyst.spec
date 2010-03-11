# $Id$
# Authority: dag
# Upstream: Tomas Doran <bobtfish@bobtfish.net>
# ExcludeDist: el4

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Test-WWW-Mechanize-Catalyst

Summary: Test::WWW::Mechanize for Catalyst
Name: perl-Test-WWW-Mechanize-Catalyst
Version: 0.52
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Test-WWW-Mechanize-Catalyst/

Source: http://search.cpan.org/CPAN/authors/id/B/BO/BOBTFISH/Test-WWW-Mechanize-Catalyst-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Catalyst) >= 5.00
BuildRequires: perl(Catalyst::Plugin::Session::State::Cookie)
BuildRequires: perl(Catalyst::Plugin::Session::Store::Dummy)
#BuildRequires: perl(ExtUtils::MakeMaker) >= 6.42
#BuildRequires: perl(LWP) >= 5.816
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(LWP)
BuildRequires: perl(Moose) >= 0.67
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::WWW::Mechanize) >= 1.14
BuildRequires: perl(WWW::Mechanize) >= 1.54
BuildRequires: perl(namespace::clean) >= 0.09
Requires: perl(Catalyst) >= 5.00
#Requires: perl(LWP) >= 5.816
Requires: perl(LWP)
Requires: perl(Moose) >= 0.67
Requires: perl(Test::WWW::Mechanize) >= 1.14
Requires: perl(WWW::Mechanize) >= 1.54
Requires: perl(namespace::clean) >= 0.09

%filter_from_requires /^perl*/d
%filter_setup


%description
Test::WWW::Mechanize for Catalyst.

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
%doc %{_mandir}/man3/Test::WWW::Mechanize::Catalyst.3pm*
%dir %{perl_vendorlib}/Test/
%dir %{perl_vendorlib}/Test/WWW/
%dir %{perl_vendorlib}/Test/WWW/Mechanize/
#%{perl_vendorlib}/Test/WWW/Mechanize/Catalyst/
%{perl_vendorlib}/Test/WWW/Mechanize/Catalyst.pm

%changelog
* Thu Mar 11 2010 Christoph Maser <cmr@financial.com> - 0.52-1
- Updated to version 0.52.

* Thu Jun 11 2009 Christoph Maser <cmr@financial.com> - 0.51-1
- Updated to version 0.51.

* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 0.42-1
- Updated to release 0.42.

* Sun Dec 30 2007 Dag Wieers <dag@wieers.com> - 0.41-1
- Initial package. (using DAR)
