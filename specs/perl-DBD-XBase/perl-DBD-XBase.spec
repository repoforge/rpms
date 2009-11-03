# $Id$
# Authority: dries
# Upstream: Jan Pazdziora <adelton$fi,muni,cz>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name DBD-XBase

Summary: DBI driver for XBase compatible database files
Name: perl-DBD-XBase
Version: 0.241
Release: 1.2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DBD-XBase/

Source: http://www.cpan.org/modules/by-module/DBD/DBD-XBase-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Module XBase provides access to XBase (dBase, Fox*) dbf files.
It also handles memo files (dbt, fpt) and to certain extend
index files (ndx, ntx, mdx, idx and cdx). The DBD::XBase is
a database driver for DBI and provides simple SQL interface for
reading and writing the database files. So this package offers
two ways of accessing your beloved data in dbf files: XBase.pm
and DBD::XBase. I recommend using DBD::XBase and only resort
to XBase.pm if you need something special which is not
supported by the DBI interface.

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
%doc %{_mandir}/man?/*
%{_bindir}/dbfdump
%{_bindir}/indexdump
%{perl_vendorlib}/DBD/XBase.pm
%{perl_vendorlib}/XBase
%{perl_vendorlib}/XBase.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.241-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.241-1
- Initial package.
