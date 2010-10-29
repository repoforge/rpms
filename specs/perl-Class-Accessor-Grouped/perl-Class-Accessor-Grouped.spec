# $Id$
# Authority: dag
# Upstream: Rafael Kitover <rkitover@io.com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Class-Accessor-Grouped

Summary: Lets you build groups of accessors
Name: perl-Class-Accessor-Grouped
Version: 0.09008
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Class-Accessor-Grouped/

Source: http://search.cpan.org/CPAN/authors/id/R/RI/RIBASUSHI/Class-Accessor-Grouped-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Carp)
BuildRequires: perl(Class::Inspector)
#BuildRequires: perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(MRO::Compat)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Sub::Identify)
BuildRequires: perl(Sub::Name) >= 0.04
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::More)
BuildRequires: perl >= 5.6.1
Requires: perl(Carp)
Requires: perl(Class::Inspector)
Requires: perl(MRO::Compat)
Requires: perl(Scalar::Util)
Requires: perl(Sub::Name) >= 0.04
Requires: perl >= 5.6.1

%filter_from_requires /^perl*/d
%filter_setup

%description
Lets you build groups of accessors.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}" --skipdeps
%{__make} %{?_smp_mflags}
%{__make} test

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST MANIFEST.SKIP META.yml README
%doc %{_mandir}/man3/Class::Accessor::Grouped.3pm*
%dir %{perl_vendorlib}/Class/
%dir %{perl_vendorlib}/Class/Accessor/
#%{perl_vendorlib}/Class/Accessor/Grouped/
%{perl_vendorlib}/Class/Accessor/Grouped.pm

%changelog
* Fri Oct 29 2010 Christoph Maser <cmaser@gmx.de> - 0.09008-1
- Updated to version 0.09008.

* Mon Jun  7 2010 Christoph Maser <cmaser@gmx.de> - 0.09003-1
- Updated to version 0.09003.

* Thu Dec 31 2009 Christoph Maser <cmr@financial.com> - 0.09002-1
- Updated to version 0.09002.

* Wed Sep  9 2009 Christoph Maser <cmr@financial.com> - 0.09000-1
- Updated to version 0.09000.

* Wed May 13 2009 Dag Wieers <dag@wieers.com> - 0.08003-1
- Updated to release 0.08003.

* Thu Dec 18 2008 Dag Wieers <dag@wieers.com> - 0.08002-1
- Updated to release 0.08002.

* Wed Jan 23 2008 Dag Wieers <dag@wieers.com> - 0.08001-1
- Updated to release 0.08001.

* Sun Dec 30 2007 Dag Wieers <dag@wieers.com> - 0.07000-1
- Initial package. (using DAR)
