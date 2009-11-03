# $Id$
# Authority: dries
# Upstream: David Boyce <dsb$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name ClearCase-CRDB

Summary: Impact analysis in a clearmake build environment
Name: perl-ClearCase-CRDB
Version: 0.15
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/ClearCase-CRDB/

Source: http://www.cpan.org/modules/by-module/ClearCase/ClearCase-CRDB-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Whouses provides a limited form of "impact analysis" in a clearmake
build environment. This is different from traditional impact analysis
In particular, it operates at the granularity of files rather than language
elements.

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
%doc Changes MANIFEST README
%doc %{_mandir}/man1/whouses.1*
%doc %{_mandir}/man3/ClearCase::CRDB.3pm*
%{_bindir}/whouses
%dir %{perl_vendorlib}/ClearCase/
#%{perl_vendorlib}/ClearCase/CRDB/
%{perl_vendorlib}/ClearCase/CRDB.pm

%changelog
* Wed Nov 07 2007 Dag Wieers <dag@wieers.com> - 0.15-1
- Updated to release 0.15.

* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.12-1
- Initial package.
