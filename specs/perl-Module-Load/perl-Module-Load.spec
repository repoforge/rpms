# $Id$
# Authority: dries
# Upstream: Jos Boumans <kane$cpan,org>

### EL6 ships with perl-Module-Load-0.16-115.el6
%{?el6:# Tag: rfx}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Module-Load

Summary: Runtime require of both modules and files
Name: perl-Module-Load
Version: 0.16
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Module-Load/

Source: http://www.cpan.org/modules/by-module/Module/Module-Load-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Runtime require of both modules and files.

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
%doc CHANGES MANIFEST META.yml README
%doc %{_mandir}/man3/Module::Load.3pm*
%dir %{perl_vendorlib}/Module/
#%{perl_vendorlib}/Module/Load/
%{perl_vendorlib}/Module/Load.pm

%changelog
* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 0.16-1
- Updated to version 0.16.

* Wed Nov 14 2007 Dag Wieers <dag@wieers.com> - 0.12-1
- Updated to release 0.12.

* Fri Dec 10 2004 Dries Verachtert <dries@ulyssis.org> - 0.10-1
- Initial package.
