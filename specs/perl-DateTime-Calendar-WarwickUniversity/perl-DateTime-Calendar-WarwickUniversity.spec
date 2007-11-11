# $Id$
# Authority: dries
# Upstream: Tim Retout <tim$retout,co,uk>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name DateTime-Calendar-WarwickUniversity

Summary: Warwick University academic calendar
Name: perl-DateTime-Calendar-WarwickUniversity
Version: 0.01
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DateTime-Calendar-WarwickUniversity/

Source: http://www.cpan.org/modules/by-module/DateTime/DateTime-Calendar-WarwickUniversity-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 2:5.8.4
BuildRequires: perl(ExtUtils::MakeMaker)

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
%doc Changes README
%doc %{_mandir}/man3/DateTime::Calendar::WarwickUniversity*
%{perl_vendorlib}/DateTime/Calendar/WarwickUniversity.pm

%changelog
* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.01-1
- Initial package.
