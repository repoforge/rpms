# $Id$
# Authority: dag
# Upstream: Audrey Tang <cpan$audreyt,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Scalar-Defer

Summary: Lazy evaluation in Perl
Name: perl-Scalar-Defer
Version: 0.22
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Scalar-Defer/

Source: http://search.cpan.org/CPAN/authors/id/J/JE/JESSE/Scalar-Defer-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Class::InsideOut)
BuildRequires: perl(Exporter::Lite)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl >= 5.6.0
Requires: perl(Class::InsideOut)
Requires: perl(Exporter::Lite)
Requires: perl >= 5.6.0

%filter_from_requires /^perl*/d
%filter_setup

%description
Lazy evaluation in Perl.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}" --skipdeps
%{__make} %{?_smp_mflags}
%{__make} %{?_smp_mflags} test

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README SIGNATURE
%doc %{_mandir}/man3/Scalar::Defer.3pm*
%dir %{perl_vendorlib}/Scalar/
#%{perl_vendorlib}/Scalar/Defer/
%{perl_vendorlib}/Scalar/Defer.pm

%changelog
* Wed Feb  3 2010 Christoph Maser <cmr@financial.com> - 0.22-1
- Updated to version 0.22.

* Tue Jul 21 2009 Christoph Maser <cmr@financial.com> - 0.20-1
- Updated to version 0.20.

* Fri Jun 19 2009 Christoph Maser <cmr@financial.com> - 0.18-1
- Updated to version 0.18.

* Wed Jan 23 2008 Dag Wieers <dag@wieers.com> - 0.14-1
- Updated to release 0.14.

* Fri Jan 04 2008 Dag Wieers <dag@wieers.com> - 0.13-1
- Updated to release 0.13.

* Thu Dec 27 2007 Dag Wieers <dag@wieers.com> - 0.12-1
- Updated to release 0.12.

* Tue Dec 04 2007 Dag Wieers <dag@wieers.com> - 0.11-1
- Updated to release 0.11.

* Mon Nov 05 2007 Dag Wieers <dag@wieers.com> - 0.10-1
- Initial package. (using DAR)
