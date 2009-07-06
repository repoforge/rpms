# $Id$
# Authority: dries
# Upstream: Hakan Ardo <hakan$debian,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name DBIx-HTMLView

Summary: Create web userinterfaces to DBI databases
Name: perl-DBIx-HTMLView
Version: 0.9
Release: 1
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DBIx-HTMLView/

Source: http://www.cpan.org/modules/by-module/DBIx/DBIx-HTMLView-LATEST.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This is a general propose module to simplify the creation of web
userinterfaces to a DBI database, currently it can list, view, add,
edit and delete entries in the databse using either input ... or
textarea to gather the info.

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
%{perl_vendorlib}/DBIx/HTMLView.pm
%{perl_vendorlib}/DBIx/comp2.pl
%{perl_vendorlib}/DBIx/config.pm
%{perl_vendorlib}/DBIx/fmt_srv.pl
%{perl_vendorlib}/DBIx/gen_act.pl
%{perl_vendorlib}/DBIx/HTMLView

%changelog
* Mon Jul  6 2009 Christoph Maser <cmr@financial.com> - 0.9-1
- Updated to version 0.9.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.1-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.1-1
- Initial package.
