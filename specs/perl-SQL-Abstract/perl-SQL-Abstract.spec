# $Id$
# Authority: dag
# Upstream: Nate Wiger <nate$wiger,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name SQL-Abstract

Name: perl-SQL-Abstract
Summary: Generate SQL from Perl data structures
Version: 1.69
Release: 2%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/SQL-Abstract/

Source: http://search.cpan.org/CPAN/authors/id/F/FR/FREW/SQL-Abstract-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Class::Accessor::Grouped) >= 0.09005
#BuildRequires: perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Getopt::Long::Descriptive) >= 0.086
BuildRequires: perl(Hash::Merge) >= 0.12
BuildRequires: perl(List::Util)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Storable)
BuildRequires: perl(Test::Deep) >= 0.106
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::More)
#BuildRequires: perl(Test::Warn)
BuildRequires: perl >= v5.6.2
Requires: perl(Class::Accessor::Grouped) >= 0.09005
Requires: perl(Getopt::Long::Descriptive) >= 0.086
Requires: perl(Hash::Merge) >= 0.12
Requires: perl(List::Util)
Requires: perl(Scalar::Util)
Requires: perl >= v5.6.2

%filter_from_requires /^perl*/d
%filter_setup


%description
This module was inspired by the excellent DBIx::Abstract.  However, in using
that module I found that what I really wanted to do was generate SQL, but still
retain complete control over my statement handles and use the DBI interface.
So, I set out to create an abstract SQL generation module.

While based on the concepts used by DBIx::Abstract, there are several important
differences, especially when it comes to WHERE clauses. I have modified the
concepts used to make the SQL easier to generate from Perl data structures and,
IMO, more intuitive.  The underlying idea is for this module to do what you
mean, based on the data structures you provide it. The big advantage is that
you don't have to modify your code every time your data changes, as this module
figures it out.

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
%{_bindir}/format-sql
%{perl_vendorlib}/DBIx/Class/Storage/Debug/PrettyPrint.pm
%{perl_vendorlib}/SQL/Abstract.pm
%{perl_vendorlib}/SQL/Abstract/Test.pm
%{perl_vendorlib}/SQL/Abstract/Tree.pm


%changelog
* Wed Nov 03 2010 Steve Huff <shuff@vecna.org> - 1.69-2
- Removed POD from %description.

* Fri Oct 29 2010 Christoph Maser <cmaser@gmx.de> - 1.69-1
- Updated to version 1.69.

* Mon Jun  7 2010 Christoph Maser <cmaser@gmx.de> - 1.67-1
- Updated to version 1.67.

* Fri Apr 16 2010 Christoph Maser <cmr@financial.com> - 1.65-1
- Updated to version 1.65.

* Fri Feb 05 2010 Steve Huff <shuff@vecna.org> - 1.61-1
- Updated to version 1.61.

* Thu Oct 22 2009 Christoph Maser <cmr@financial.com> - 1.60-1
- Updated to version 1.60.

* Mon Sep  7 2009 Christoph Maser <cmr@financial.com> - 1.58-1
- Updated to version 1.58.

* Fri Sep  4 2009 Christoph Maser <cmr@financial.com> - 1.57-1
- Updated to version 1.57.

* Thu Jun 11 2009 Christoph Maser <cmr@financial.com> - 1.56-1
- Updated to version 1.56.

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
