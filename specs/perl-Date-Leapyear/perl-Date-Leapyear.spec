# $Id$
# Authority: dries
# Upstream: Rich Bowen <rbowen$rcbowen,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Date-Leapyear

Summary: Is a particular year a leap year
Name: perl-Date-Leapyear
Version: 1.72
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Date-Leapyear/

Source: http://www.cpan.org/modules/by-module/Date/Date-Leapyear-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Date::Leapyear exports one function - isleap - which returns 1 or 0 if a
year is leap, or not, respectively.

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
%doc README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Date/Leapyear.pm

%changelog
* Thu Jul  9 2009 Christoph Maser <cmr@financial.com> - 1.72-1
- Updated to version 1.72.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.71-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.71-1
- Initial package.
