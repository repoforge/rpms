# $Id$
# Authority: dries
# Upstream: Jim Turner <turnerjw$wwol,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name DBD-LDAP

Summary: SQL/Perl DBI interface to Ldap databases
Name: perl-DBD-LDAP
Version: 0.20
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DBD-LDAP/

Source: http://search.cpan.org/CPAN/authors/id/T/TU/TURNERJW/DBD-LDAP-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(DBI)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Net::LDAP) >= 0.01
Requires: perl(DBI)
Requires: perl(Net::LDAP) >= 0.01

%filter_from_requires /^perl*/d
%filter_setup


%description
DBD::LDAP - A DBI driver for LDAP databases.  LDAP stands for the
"Lightweight Directory Access Protocol".  For more information,
see:  http://www.ogre.com/ldap/docs.html

%prep
%setup -n %{real_name}-%{version}
%{__perl} -pi -e 's|/usr/local/bin/perl5|/usr/bin/perl|g;' */*.pm

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
%doc %{_mandir}/man3/*
%{perl_vendorlib}/DBD/LDAP.pm
%{perl_vendorlib}/JLdap.pm

%changelog
* Wed Dec 30 2009 Christoph Maser <cmr@financial.com> - 0.20-1
- Updated to version 0.20.

* Tue Nov 14 2006 Dries Verachtert <dries@ulyssis.org> - 0.09-1
- Updated to release 0.09.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.08-1
- Updated to release 0.08.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.06-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.06-1
- Initial package.
