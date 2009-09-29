# $Id$
# Authority: dag
# Upstream: Adam Kennedy <adamk$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Algorithm-Dependency

Summary: Base class for implementing various dependency trees
Name: perl-Algorithm-Dependency
Version: 1.110
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Algorithm-Dependency/

Source: http://www.cpan.org/modules/by-module/Algorithm/Algorithm-Dependency-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.005
# From yaml build_requires
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Spec) >= 0.80
BuildRequires: perl(Test::ClassAPI) >= 0.6
BuildRequires: perl(Test::More) >= 0.47
# From yaml requires
BuildRequires: perl(List::Util) >= 1.11
BuildRequires: perl(Params::Util) >= 0.31
BuildRequires: perl >= 5.005

Requires: perl >= 0:5.005

%description
Algorithm-Dependency is a perl module for implementing various
dependency trees.

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
%doc Changes LICENSE MANIFEST META.yml README
%doc %{_mandir}/man3/Algorithm::Dependency.3pm*
%doc %{_mandir}/man3/Algorithm::Dependency::*.3pm*
%dir %{perl_vendorlib}/Algorithm/
%{perl_vendorlib}/Algorithm/Dependency/
%{perl_vendorlib}/Algorithm/Dependency.pm

%changelog
* Tue Sep 29 2009 Christoph Maser <cmr@financial.com> - 1.110-1
- Updated to version 1.110.

* Wed Jan 23 2008 Dag Wieers <dag@wieers.com> - 1.106-1
- Updated to release 1.106.

* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 1.104-1
- Updated to release 1.104.

* Tue Nov 06 2007 Dag Wieers <dag@wieers.com> - 1.103-1
- Updated to release 1.103.

* Sun Apr 29 2007 Dag Wieers <dag@wieers.com> - 1.102-1
- Initial package. (using DAR)
