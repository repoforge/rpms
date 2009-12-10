# $Id$
# Authority: dag
# Upstream: Shawn M Moore <sartak$gmail,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Mouse

Summary: Moose minus the antlers
Name: perl-Mouse
Version: 0.44
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Mouse/

Source: http://search.cpan.org/CPAN/authors/id/G/GF/GFUJI/Mouse-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
#BuildRequires: perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(ExtUtils::ParseXS) >= 2.21
BuildRequires: perl(Scalar::Util) >= 1.14
BuildRequires: perl(Test::Exception) >= 0.27
#BuildRequires: perl(Test::More) >= 0.88
BuildRequires: perl(Test::More)
BuildRequires: perl(XSLoader) >= 0.1
BuildRequires: perl >= 5.6.2
Requires: perl(Scalar::Util) >= 1.14
Requires: perl(XSLoader) >= 0.1
Requires: perl >= 5.6.2

%filter_from_requires /^perl*/d
%filter_setup

%description
Moose minus the antlers.

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
%doc Changes MANIFEST META.yml
%doc %{_mandir}/man3/ouse.3pm*
%doc %{_mandir}/man3/Mouse.3pm*
%doc %{_mandir}/man3/Mouse::*.3pm*
%doc %{_mandir}/man3/Squirrel.3pm*
%doc %{_mandir}/man3/Squirrel::Role.3pm*
%doc %{_mandir}/man3/Test::Mouse.3pm.gz
%{perl_vendorlib}/Mouse/
%{perl_vendorlib}/Mouse.pm
%{perl_vendorlib}/ouse.pm
%{perl_vendorlib}/Squirrel/
%{perl_vendorlib}/Squirrel.pm
%{perl_vendorlib}/Test/Mouse.pm


%changelog
* Wed Sep  9 2009 Christoph Maser <cmr@financial.com> - 0.28-1
- Updated to version 0.28.

* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 0.27-1
- Updated to version 0.27.

* Thu Oct 09 2008 Dag Wieers <dag@wieers.com> - 0.09-1
- Initial package. (using DAR)
