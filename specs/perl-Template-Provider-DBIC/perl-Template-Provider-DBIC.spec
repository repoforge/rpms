# $Id$
# Authority: dries
# Upstream: Dave Cardwell <dcardwell$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Template-Provider-DBIC

Summary: Load templates using DBIx::Class
Name: perl-Template-Provider-DBIC
Version: 0.02
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Template-Provider-DBIC/

Source: http://www.cpan.org/modules/by-module/Template/Template-Provider-DBIC-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(DBD::SQLite) >= 1.11
BuildRequires: perl(DBIx::Class)
BuildRequires: perl(Test::More)

%description
Load templates using DBIx::Class.

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

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes INSTALL MANIFEST META.yml README examples/
%doc %{_mandir}/man3/Template::Provider::DBIC.3pm*
%dir %{perl_vendorlib}/Template/
%dir %{perl_vendorlib}/Template/Provider/
#%{perl_vendorlib}/Template/Provider/DBIC/
%{perl_vendorlib}/Template/Provider/DBIC.pm

%changelog
* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 0.02-1
- Updated to release 0.02.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.01-1
- Initial package.
