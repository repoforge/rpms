# $Id$
# Authority: dries
# Upstream: Stefan Hornburg <racke$linuxia,de>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name DBIx-Easy

Summary: Easy to Use DBI interface
Name: perl-DBIx-Easy
Version: 0.18
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DBIx-Easy/

Source: http://www.cpan.org/modules/by-module/DBIx/DBIx-Easy-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Easy to Use DBI interface.

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
%{_bindir}/dbs_*
%{perl_vendorlib}/DBIx/Easy.pm
%dir %{perl_vendorlib}/DBIx/Easy/
%{perl_vendorlib}/DBIx/Easy/Import.pm

%changelog
* Mon Jul  6 2009 Christoph Maser <cmr@financial.com> - 0.18-1
- Updated to version 0.18.

* Mon Jun 18 2007 Dries Verachtert <dries@ulyssis.org> - 0.17-1
- Updated to release 0.17.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.16-1.2
- Rebuild for Fedora Core 5.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 0.16-1
- Updated to release 0.16.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.15-1
- Initial package.
