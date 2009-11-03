# $Id$
# Authority: dag
# Upstream: Matt Sergeant <msergeant$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name DBD-SQLite2

Summary: Perl module that implements a self contained RDBMS in a DBI Driver (sqlite 2.x)
Name: perl-DBD-SQLite2
Version: 0.33
Release: 1%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DBD-SQLite2/

Source: http://www.cpan.org/modules/by-module/DBD/DBD-SQLite2-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(DBI)
BuildRequires: perl(ExtUtils::MakeMaker)

%description
DBD-SQLite2 is a Perl module that implements a self contained
RDBMS in a DBI Driver. (sqlite 2.x)

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/DBD::SQLite2.3pm*
%dir %{perl_vendorarch}/DBD/
%{perl_vendorarch}/DBD/SQLite2.pm
%{perl_vendorarch}/DBD/getsqlite.pl
%dir %{perl_vendorarch}/auto/DBD/
%{perl_vendorarch}/auto/DBD/SQLite2/

%changelog
* Tue May 01 2007 Dag Wieers <dag@wieers.com> - 0.33-1
- Initial package. (using DAR)
