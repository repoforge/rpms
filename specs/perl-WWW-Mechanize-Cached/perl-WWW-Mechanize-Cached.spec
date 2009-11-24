# $Id$
# Authority: dag
# Upstream: Andy Lester <andy$petdance,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name WWW-Mechanize-Cached

Summary: Cache response to be polite
Name: perl-WWW-Mechanize-Cached
Version: 1.35
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/WWW-Mechanize-Cached/

Source: http://www.cpan.org/modules/by-module/WWW/WWW-Mechanize-Cached-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Cache::Cache) >= 1.02
BuildRequires: perl(Carp)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(HTTP::Headers) >= 5.827
BuildRequires: perl(Storable) >= 2.08
BuildRequires: perl(Test::More) >= 0.47
#BuildRequires: perl(Test::Warn) >= 0.11  
BuildRequires: perl(WWW::Mechanize) >= 1.00
Requires: perl(Cache::Cache) >= 1.02
Requires: perl(Carp)
Requires: perl(HTTP::Headers) >= 5.827
Requires: perl(Storable) >= 2.08
Requires: perl(Test::More) >= 0.47
Requires: perl(Test::Warn) >= 0.11
Requires: perl(WWW::Mechanize) >= 1.00

%filter_from_requires /^perl*/d
%filter_setup



%description
Cache response to be polite.

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
%doc AUTHORS Changes INSTALL MANIFEST MANIFEST.SKIP META.yml README
%doc %{_mandir}/man3/WWW::Mechanize::Cached.3pm*
%dir %{perl_vendorlib}/WWW/
%dir %{perl_vendorlib}/WWW/Mechanize/
#%{perl_vendorlib}/WWW/Mechanize/Cached/
%{perl_vendorlib}/WWW/Mechanize/Cached.pm

%changelog
* Tue Nov 24 2009 Christoph Maser <cmr@financial.com> - 1.35-1
- Updated to version 1.35.

* Wed Jul 15 2009 Christoph Maser <cmr@financial.com> - 1.33-1
- Updated to version 1.33.

* Fri Nov 23 2007 Dag Wieers <dag@wieers.com> - 1.32-1
- Initial package. (using DAR)
