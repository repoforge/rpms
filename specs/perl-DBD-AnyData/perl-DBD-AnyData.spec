# $Id$
# Authority: dries
# Upstream: Jeff Zucker <jeff$vpservices,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name DBD-AnyData

Summary: Interface to data in many formats and from many sources
Name: perl-DBD-AnyData
Version: 0.09
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DBD-AnyData/

Source: http://www.cpan.org/modules/by-module/DBD/DBD-AnyData-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
The DBD::AnyData module provides a DBI (Perl Database Interface)
and SQL (Structured Query Language) interface to data in many
formats and from many sources.

There are actually two modules DBD::AnyData and AnyData.  The AnyData
module provides most of the same features as DBD::AnyData
through a tied hash interface which does not require or support
DBI and SQL.

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/DBD::AnyData.3pm*
%dir %{perl_vendorlib}/DBD/
#%{perl_vendorlib}/DBD/AnyData/
%{perl_vendorlib}/DBD/AnyData.pm

%changelog
* Fri Nov 09 2007 Dag Wieers <dag@wieers.com> - 0.09-1
- Updated to release 0.09.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.08-1
- Initial package.
