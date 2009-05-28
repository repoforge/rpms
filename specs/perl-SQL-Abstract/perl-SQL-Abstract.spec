# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name SQL-Abstract

Name: perl-SQL-Abstract
Summary: Generate SQL from Perl data structures
Version: 1.55
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/SQL-Abstract/

Source: http://www.cpan.org/modules/by-module/SQL/SQL-Abstract-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl(ExtUtils::MakeMaker)
BuildArch: noarch

%description
This module was inspired by the excellent L<DBIx::Abstract>.
However, in using that module I found that what I really wanted
to do was generate SQL, but still retain complete control over my
statement handles and use the DBI interface. So, I set out to
create an abstract SQL generation module.

While based on the concepts used by L<DBIx::Abstract>, there are
several important differences, especially when it comes to WHERE
clauses. I have modified the concepts used to make the SQL easier
to generate from Perl data structures and, IMO, more intuitive.
The underlying idea is for this module to do what you mean, based
on the data structures you provide it. The big advantage is that
you don't have to modify your code every time your data changes,
as this module figures it out.

%prep
%setup -n %{real_name}-%{version}
#chmod -R u+w %{_builddir}/%{pkgname}-%{version}

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
%{_mandir}/man3/*
%dir %{perl_vendorlib}/SQL/
%{perl_vendorlib}/SQL/Abstract.pm
%{perl_vendorlib}/SQL/Abstract/Test.pm

%changelog
* Thu May 28 2009 Christoph Maser <cmr@financial.com> - 1.55-1
- Updated to release 1.55.

* Fri Apr 24 2009 Christoph Maser <cmr@financial.com> - 1.51-1
- Updated to release 1.51.

* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 1.22-1
- Updated to release 1.22.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 1.21-1
- Updated to release 1.21.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 1.20-1
- Updated to release 1.20.

* Thu Mar 31 2005 Dag Wieers <dag@wieers.com> - 1.18-1
- Initial package. (using DAR)
