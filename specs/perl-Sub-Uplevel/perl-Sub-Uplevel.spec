# $Id$
# Authority: dries
# Upstream: David A, Golden <dagolden$cpan,org>

### EL6 ships with perl-Sub-Uplevel-0.2002-4.el6
%{?el6:# Tag: rfx}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Sub-Uplevel

Summary: Apparently run a function in a higher stack frame
Name: perl-Sub-Uplevel
Version: 0.22
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Sub-Uplevel/

Source: http://www.cpan.org/modules/by-module/Sub/Sub-Uplevel-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Carp)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More)

%filter_from_requires /^perl*/d
%filter_setup


%description
Apparently run a function in a higher stack frame.

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
%doc Changes INSTALL LICENSE MANIFEST MANIFEST.SKIP META.yml README Todo examples/
%doc %{_mandir}/man3/Sub::Uplevel.3pm*
%dir %{perl_vendorlib}/Sub/
#%{perl_vendorlib}/Sub/Uplevel/
%{perl_vendorlib}/Sub/Uplevel.pm
%{perl_vendorlib}/Sub/Uplevel.pod

%changelog
* Thu Dec 10 2009 Christoph Maser <cmr@financial.com> - 0.22-1
- Updated to version 0.22.

* Wed Jun 17 2009 Christoph Maser <cmr@financial.com> - 0.2002-1
- Updated to version 0.2002.

* Thu Feb 21 2008 Dag Wieers <dag@wieers.com> - 0.1901-1
- Updated to release 0.1901.

* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 0.18-1
- Updated to release 0.18.

* Tue Nov 14 2006 Dries Verachtert <dries@ulyssis.org> - 0.14-1
- Updated to release 0.14.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.13-1
- Updated to release 0.13.

* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 0.12-1
- Updated to release 0.12.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.09-1
- Initial package.
