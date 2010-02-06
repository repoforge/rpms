# $Id$
# Authority: dag
# Upstream: Florian Ragwitz <rafl@debian.org>
# ExcludeDist: el4

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Catalyst-Plugin-Authentication

Summary: Infrastructure plugin for the Catalyst
Name: perl-Catalyst-Plugin-Authentication
Version: 0.10016
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Catalyst-Plugin-Authentication/

Source: http://search.cpan.org/CPAN/authors/id/F/FL/FLORA/Catalyst-Plugin-Authentication-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Catalyst::Plugin::Session) >= 0.10
BuildRequires: perl(Catalyst::Runtime)
BuildRequires: perl(Class::Inspector)
BuildRequires: perl(Class::MOP)
#BuildRequires: perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(MRO::Compat)
BuildRequires: perl(Moose)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::More)
BuildRequires: perl >= 5.8.1
Requires: perl(Catalyst::Plugin::Session) >= 0.10
Requires: perl(Catalyst::Runtime)
Requires: perl(Class::Inspector)
Requires: perl(MRO::Compat)
Requires: perl >= 5.8.1

%filter_from_requires /^perl*/d
%filter_setup


%description
Infrastructure plugin for the Catalyst.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}" --skipdeps
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
%doc %{_mandir}/man3/Catalyst::Authentication::*.3pm*
%doc %{_mandir}/man3/Catalyst::Plugin::Authentication.3pm*
%doc %{_mandir}/man3/Catalyst::Plugin::Authentication::*.3pm*
%dir %{perl_vendorlib}/Catalyst/
%{perl_vendorlib}/Catalyst/Authentication/
%dir %{perl_vendorlib}/Catalyst/Plugin/
%{perl_vendorlib}/Catalyst/Plugin/Authentication/
%{perl_vendorlib}/Catalyst/Plugin/Authentication.pm

%changelog
* Sat Feb  6 2010 Christoph Maser <cmr@financial.com> - 0.10016-1
- Updated to version 0.10016.

* Thu Jan 14 2010 Christoph Maser <cmr@financial.com> - 0.10015-1
- Updated to version 0.10015.

* Thu Dec 18 2008 Dag Wieers <dag@wieers.com> - 0.10008-1
- Updated to release 0.10008.

* Tue Oct 07 2008 Dag Wieers <dag@wieers.com> - 0.10007-1
- Updated to release 0.10007.

* Tue Feb 19 2008 Dag Wieers <dag@wieers.com> - 0.10006-1
- Updated to release 0.10006.

* Sat Jan 26 2008 Dag Wieers <dag@wieers.com> - 0.10005-1
- Updated to release 0.10005.

* Sun Dec 30 2007 Dag Wieers <dag@wieers.com> - 0.10004-1
- Initial package. (using DAR)
