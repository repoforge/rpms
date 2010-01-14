# $Id$
# Authority: dries
# Upstream: Brian Cassidy <bricas@cpan.org>
# ExcludeDist: el4

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Catalyst-Plugin-I18N-Request

Summary: Plugin for localizing/delocalizing paths and parameters
Name: perl-Catalyst-Plugin-I18N-Request
Version: 0.05
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Catalyst-Plugin-I18N-Request/

Source: http://search.cpan.org/CPAN/authors/id/B/BR/BRICAS/Catalyst-Plugin-I18N-Request-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Catalyst::Plugin::I18N)
BuildRequires: perl(Catalyst::Runtime) >= 5.7000
BuildRequires: perl(MRO::Compat)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Test::More)
BuildRequires: perl(URI)
BuildRequires: perl >= 5.8.0
Requires: perl(Catalyst::Plugin::I18N)
Requires: perl(Catalyst::Runtime) >= 5.7000
Requires: perl(MRO::Compat)
Requires: perl(Scalar::Util)
Requires: perl(URI)
Requires: perl >= 5.8.0

%filter_from_requires /^perl*/d
%filter_setup


%description
Plugin for localizing/delocalizing paths and parameters.

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
%doc %{_mandir}/man3/Catalyst::Plugin::I18N::Request.3pm*
%dir %{perl_vendorlib}/Catalyst/
%dir %{perl_vendorlib}/Catalyst/Plugin/
%dir %{perl_vendorlib}/Catalyst/Plugin/I18N/
#%{perl_vendorlib}/Catalyst/Plugin/I18N/Request/
%{perl_vendorlib}/Catalyst/Plugin/I18N/Request.pm

%changelog
* Thu Jan 14 2010 Christoph Maser <cmr@financial.com> - 0.05-1
- Updated to version 0.05.

* Tue Nov 06 2007 Dag Wieers <dag@wieers.com> - 0.03-1
- Updated to release 0.03.

* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.02-1
- Initial package.
