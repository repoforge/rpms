# $Id$
# Authority: dag
# Upstream: Greg Sabino Mullane <greg@turnstep.com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name DBD-Pg

Summary: DBI PostgreSQL interface
Name: perl-DBD-Pg
Version: 1.32
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DBD-Pg/

Source: http://www.cpan.org/modules/by-module/DBD/DBD-Pg-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(DBI) >= 1.45
BuildRequires: perl(Test::Harness) >= 2.03
BuildRequires: perl(Test::Simple) >= 0.3

%description
DBI PostgreSQL interface.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST README README.win32 TODO
%doc %{_mandir}/man3/DBD::Pg.3pm*
%dir %{perl_vendorarch}/DBD/
%{perl_vendorarch}/DBD/Pg.pm
%dir %{perl_vendorarch}/auto/DBD/
%{perl_vendorarch}/auto/DBD/Pg/

%changelog
* Sat Aug 04 2007 Dag Wieers <dag@wieers.com> - 1.32-1
- Initial package. (using DAR)
