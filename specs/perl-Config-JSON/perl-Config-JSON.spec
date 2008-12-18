# $Id$
# Authority: dries
# Upstream: JT Smith <jt$plainblack,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Config-JSON
%define real_version 1.003000

Summary: JSON based config file system
Name: perl-Config-JSON
Version: 1.3.0
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Config-JSON/

Source: http://www.cpan.org/modules/by-module/Config/Config-JSON-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

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
