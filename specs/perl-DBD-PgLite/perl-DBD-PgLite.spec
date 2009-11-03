# $Id$
# Authority: dag
# Upstream: Baldur Kristinsson <bk$mbl,is>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name DBD-PgLite

Summary: PostgreSQL emulation mode for SQLite
Name: perl-DBD-PgLite
Version: 0.11
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DBD-PgLite/

Source: http://www.cpan.org/modules/by-module/DBD/DBD-PgLite-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
PostgreSQL emulation mode for SQLite.

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
%doc Changes LICENSE MANIFEST META.yml README Todo
%doc %{_mandir}/man3/DBD::PgLite.3pm*
%doc %{_mandir}/man3/DBD::PgLite::*.3pm*
%dir %{perl_vendorlib}/DBD/
%{perl_vendorlib}/DBD/PgLite/
%{perl_vendorlib}/DBD/PgLite.pm

%changelog
* Tue Jul  7 2009 Christoph Maser <cmr@financial.com> - 0.11-1
- Updated to version 0.11.

* Thu Feb 28 2008 Dag Wieers <dag@wieers.com> - 0.09-1
- Initial package. (using DAR)
