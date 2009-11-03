# $Id$
# Authority: dries
# Upstream: JT Smith <jt$plainblack,com>
# Needs new List::Util
# ExcludeDist: el4
%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Config-JSON

Summary: JSON based config file system
Name: perl-Config-JSON
Version: 1.3.1
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Config-JSON/

Source: http://www.cpan.org/modules/by-module/Config/Config-JSON-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
# From yaml requires
BuildRequires: perl(Class::InsideOut) >= 1.06
#BuildRequires: perl(File::Temp) >= 0.18      <- conflicts with perl from base
BuildRequires: perl(File::Temp)
BuildRequires: perl(JSON) >= 2.12
BuildRequires: perl(List::Util) >= 1.19
BuildRequires: perl(Test::Deep) >= 0.095
BuildRequires: perl(Test::More) >= 0.7
BuildRequires: perl(version) >= 0.7203


%description
A JSON based config file system.

%prep
%setup -n %{real_name}

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
%doc %{_mandir}/man3/Config::JSON.3pm*
%dir %{perl_vendorlib}/Config/
#%{perl_vendorlib}/Config/JSON/
%{perl_vendorlib}/Config/JSON.pm

%changelog
* Sat Aug 22 2009 Chsrioph Maser <cmr@financial.com> - 1.3.1-1
- Updated to release 1.3.1.

* Thu Dec 18 2008 Dag Wieers <dag@wieers.com> - 1.3.0-1
- Updated to release 1.3.0.

* Sat Jan 26 2008 Dag Wieers <dag@wieers.com> - 1.1.4-1
- Updated to release 1.1.4.

* Wed Nov 07 2007 Dag Wieers <dag@wieers.com> - 1.1.1-1
- Updated to release 1.1.1.

* Wed May 02 2007 Dries Verachtert <dries@ulyssis.org> - 1.0.3-1
- Updated to release 1.0.3.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 1.0.2-1
- Initial package.
