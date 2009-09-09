# $Id$
# Authority: dag
# Upstream: Shawn M Moore <sartak$gmail,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Mouse

Summary: Moose minus the antlers
Name: perl-Mouse
Version: 0.28
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Mouse/

Source: http://search.cpan.org/CPAN/authors/id/S/SU/SUNNAVY/Mouse-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.6.0
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::More)
Requires: perl >= 0:5.6.0

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
%doc %{_mandir}/man3/Mouse.3pm*
%doc %{_mandir}/man3/ouse.3pm*
%doc %{_mandir}/man3/Mouse::*.3pm*
%doc %{_mandir}/man3/Squirrel.3pm*
%{perl_vendorlib}/Mouse/
%{perl_vendorlib}/Mouse.pm
%{perl_vendorlib}/ouse.pm
%{perl_vendorlib}/Squirrel/
%{perl_vendorlib}/Squirrel.pm

%changelog
* Wed Sep  9 2009 Christoph Maser <cmr@financial.com> - 0.28-1
- Updated to version 0.28.

* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 0.27-1
- Updated to version 0.27.

* Thu Oct 09 2008 Dag Wieers <dag@wieers.com> - 0.09-1
- Initial package. (using DAR)
