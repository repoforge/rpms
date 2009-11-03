# $Id$
# Authority: dries
# Upstream: Tim Retout <tim$retout,co,uk>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name DateTime-Calendar-WarwickUniversity

Summary: Warwick University academic calendar
Name: perl-DateTime-Calendar-WarwickUniversity
Version: 0.02
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DateTime-Calendar-WarwickUniversity/

Source: http://www.cpan.org/modules/by-module/DateTime/DateTime-Calendar-WarwickUniversity-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 2:5.8.4
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Module::Build)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::Pod)
BuildRequires: perl(Test::Pod::Coverage)
Requires: perl >= 2:5.8.4

%description
Warwick University academic calendar.

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
%doc %{_mandir}/man3/DateTime::Calendar::WarwickUniversity.3pm*
%dir %{perl_vendorlib}/DateTime/
%dir %{perl_vendorlib}/DateTime/Calendar/
#%{perl_vendorlib}/DateTime/Calendar/WarwickUniversity/
%{perl_vendorlib}/DateTime/Calendar/WarwickUniversity.pm

%changelog
* Sat Nov 24 2007 Dag Wieers <dag@wieers.com> - 0.02-1
- Updated to release 0.02.

* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.01-1
- Initial package.
