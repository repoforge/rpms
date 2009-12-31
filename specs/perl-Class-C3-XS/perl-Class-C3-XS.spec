# $Id$
# Authority: dag
# Upstream: Florian Ragwitz <rafl@debian.org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Class-C3-XS

Summary: XS speedups for Class::C3
Name: perl-Class-C3-XS
Version: 0.13
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Class-C3-XS/

Source: http://search.cpan.org/CPAN/authors/id/F/FL/FLORA/Class-C3-XS-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

#BuildRequires: perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More) >= 0.47
BuildRequires: perl >= 5.6.0
Requires: perl >= 5.6.0

%filter_from_requires /^perl*/d
%filter_setup

%description
XS speedups for Class::C3.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog MANIFEST META.yml README
%doc %{_mandir}/man3/Class::C3::XS.3pm*
%dir %{perl_vendorarch}/Class/
%dir %{perl_vendorarch}/Class/C3/
%{perl_vendorarch}/Class/C3/XS.pm
%dir %{perl_vendorarch}/auto/Class/
%dir %{perl_vendorarch}/auto/Class/C3/
%{perl_vendorarch}/auto/Class/C3/XS/

%changelog
* Thu Dec 31 2009 Christoph Maser <cmr@financial.com> - 0.13-1
- Updated to version 0.13.

* Thu Jul 16 2009 Christoph Maser <cmr@financial.com> - 0.11-1
- Updated to version 0.11.

* Fri Aug 03 2007 Dag Wieers <dag@wieers.com> - 0.08-1
- Initial package. (using DAR)
