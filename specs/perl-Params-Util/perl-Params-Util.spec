# $Id$
# Authority: dries
# Upstream: Adam Kennedy <adamk$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Params-Util

Summary: Param checking functions
Name: perl-Params-Util
Version: 1.00
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Params-Util/

Source: http://www.cpan.org/modules/by-module/Params/Params-Util-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl >= 0:5.005
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Spec) >= 0.8
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Test::More) >= 0.42
Requires: perl >= 0:5.005

%description
Simple standalone param-checking functions.

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
%doc %{_mandir}/man3/Params::Util.3pm*
%{perl_vendorarch}/Params/Util.pm
%{perl_vendorarch}/auto/Params/Util/Util.bs
%{perl_vendorarch}/auto/Params/Util/Util.so


%changelog
* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 1.00-1
- Updated to version 1.00.

* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 0.31-1
- Updated to release 0.31.

* Tue Nov 06 2007 Dag Wieers <dag@wieers.com> - 0.30-1
- Updated to release 0.30.

* Mon Jun 18 2007 Dries Verachtert <dries@ulyssis.org> - 0.25-1
- Updated to release 0.25.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.23-1
- Updated to release 0.23.

* Tue Nov 14 2006 Dries Verachtert <dries@ulyssis.org> - 0.22-1
- Updated to release 0.22.

* Tue Sep 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.20-1
- Updated to release 0.20.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.19-1
- Updated to release 0.19.

* Thu Jun 01 2006 Dag Wieers <dag@wieers.com> - 0.14-1
- Updated to release 0.14.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.10-1
- Updated to release 0.10.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 0.09-1
- Updated to release 0.09.

* Sun Dec 04 2005 Dries Verachtert <dries@ulyssis.org> - 0.07-1
- Initial package.
