# $Id$
# Authority: dag
# Upstream: Brian Cassidy <bricas$cpan,org>
# ExcludeDist: el4

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Catalyst-Plugin-ConfigLoader

Summary: Load config files of various types
Name: perl-Catalyst-Plugin-ConfigLoader
Version: 0.27
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Catalyst-Plugin-ConfigLoader/

Source: http://search.cpan.org/CPAN/authors/id/B/BR/BRICAS/Catalyst-Plugin-ConfigLoader-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Catalyst::Runtime) >= 5.7008
BuildRequires: perl(Config::Any) >= 0.08
BuildRequires: perl(Data::Visitor) >= 0.24
#BuildRequires: perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(MRO::Compat) >= 0.09
BuildRequires: perl(Test::More)
BuildRequires: perl >= 5.8.0
Requires: perl(Catalyst::Runtime) >= 5.7008
Requires: perl(Config::Any) >= 0.08
Requires: perl(Data::Visitor) >= 0.24
Requires: perl(MRO::Compat) >= 0.09
Requires: perl >= 5.8.0

%filter_from_requires /^perl*/d
%filter_setup


%description
perl-Catalyst-Plugin-ConfigLoader is a Perl module to load config files
of various types.

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
%doc %{_mandir}/man3/Catalyst::Plugin::ConfigLoader.3pm*
%doc %{_mandir}/man3/Catalyst::Plugin::ConfigLoader::*.3pm*
#%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/Catalyst/
%dir %{perl_vendorlib}/Catalyst/Plugin/
%{perl_vendorlib}/Catalyst/Plugin/ConfigLoader/
%{perl_vendorlib}/Catalyst/Plugin/ConfigLoader.pm

%changelog
* Tue Jan 12 2010 Christoph Maser <cmr@financial.com> - 0.27-1
- Updated to version 0.27.

* Tue Oct 07 2008 Dag Wieers <dag@wieers.com> - 0.21-1
- Updated to release 0.21.

* Mon May 05 2008 Dag Wieers <dag@wieers.com> - 0.20-1
- Updated to release 0.20.

* Sat Nov 24 2007 Dag Wieers <dag@wieers.com> - 0.19-1
- Updated to release 0.19.

* Tue Nov 06 2007 Dag Wieers <dag@wieers.com> - 0.18-1
- Updated to release 0.18.

* Fri Aug 03 2007 Dag Wieers <dag@wieers.com> - 0.14-1
- Initial package. (using DAR)
