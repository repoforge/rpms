# $Id$
# Authority: dag
# Upstream: Jesse Vincent <jesse$bestpractical,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name DBIx-SearchBuilder

Summary: Encapsulate SQL queries and rows in simple perl objects
Name: perl-DBIx-SearchBuilder
Version: 1.56
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DBIx-SearchBuilder/

Source: http://www.cpan.org/modules/by-module/DBIx/DBIx-SearchBuilder-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
# From yaml build_requires
BuildRequires: perl(DBD::SQLite)
#BuildRequires: perl(ExtUtils::MakeMaker) >= 6.42    <- kills el4 build
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Temp)
#BuildRequires: perl(Test::More) >= 0.52 <- kills el4 build
BuildRequires: perl(Test::More)
# From yaml requires
BuildRequires: perl(Cache::Simple::TimedExpiry) >= 0.21
BuildRequires: perl(Class::ReturnValue) >= 0.4
BuildRequires: perl(Clone)
BuildRequires: perl(DBI)
BuildRequires: perl(Encode) >= 1.99
BuildRequires: perl(Want)
# From build
BuildRequires: perl(capitalization) >= 0.03
BuildRequires: perl(DBIx::DBSchema)
BuildRequires: perl(Class::Accessor)


%description
Encapsulate SQL queries and rows in simple perl objects.

%prep
%setup -n %{real_name}-%{version}

### Disable perl-Test-More (part of perl package)
%{__perl} -pi.orig -e "s|^(build_requires\('Test::More'.+$)|#$1|" Makefile.PL

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}" --skipdeps
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
%doc Changes MANIFEST META.yml README ROADMAP SIGNATURE
%doc %{_mandir}/man3/DBIx::SearchBuilder.3pm*
%doc %{_mandir}/man3/DBIx::SearchBuilder::*.3pm*
%dir %{perl_vendorlib}/DBIx/
%{perl_vendorlib}/DBIx/SearchBuilder/
%{perl_vendorlib}/DBIx/SearchBuilder.pm
%exclude %{perl_vendorlib}/DBIx/SearchBuilder/Handle/Oracle.pm

%changelog
* Sat Aug 22 2009 Christoph Maser <cmr@financial.com> - 1.56-1
- Updated to version 1.56.

* Tue Oct 07 2008 Dag Wieers <dag@wieers.com> - 1.54-1
- Updated to release 1.54.

* Mon May 05 2008 Dag Wieers <dag@wieers.com> - 1.53-1
- Updated to release 1.53.

* Wed Jan 23 2008 Dag Wieers <dag@wieers.com> - 1.51-1
- Updated to release 1.51.

* Sat Nov 24 2007 Dag Wieers <dag@wieers.com> - 1.50-1
- Updated to release 1.50.

* Sun Aug 05 2007 Dag Wieers <dag@wieers.com> - 1.49-1
- Updated to release 1.49.
- Removed perl(DBD:Oracle) dependency. (Kanwar Ranbir Sandhu)

* Mon Jun 05 2006 Dag Wieers <dag@wieers.com> - 1.43-1
- Initial package. (using DAR)
