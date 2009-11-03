# $Id$
# Authority: dag
# Upstream: Edmund Mergl <E,Mergl$bawue,de>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name pgsql_perl5

Summary: Perl module named pgsql_perl5
Name: perl-pgsql_perl5
Version: 1.9.0
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/pgsql_perl5/

Source: http://www.cpan.org/modules/by-module/Pg/pgsql_perl5-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
perl-pgsql_perl5 is a Perl module.

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

### Clean up docs
find eg/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST README eg/
%doc %{_mandir}/man3/Pg.3pm*
%{perl_vendorarch}/auto/Pg/
%{perl_vendorarch}/Pg.pm

%changelog
* Sat Nov 24 2007 Dag Wieers <dag@wieers.com> - 1.9.0-1
- Initial package. (using DAR)
