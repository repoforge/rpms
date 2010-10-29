# $Id$
# Authority: cmr
# Upstream: Vincent Pit <perl$profvince,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Variable-Magic

Summary: Associate user-defined magic to variables from Perl
Name: perl-Variable-Magic
Version: 0.44
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Variable-Magic/

Source: http://search.cpan.org/CPAN/authors/id/V/VP/VPIT/Variable-Magic-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl(Carp)
BuildRequires: perl(Config)
BuildRequires: perl(Exporter)
BuildRequires: perl(ExtUtils::MakeMaker)
#BuildRequires: perl(Test::More)   conflicts with perl package
BuildRequires: perl(XSLoader)
#BuildRequires: perl(base)  conflicts with perl package
BuildRequires: perl >= 5.008
Requires: perl(Carp)
Requires: perl(Exporter)
Requires: perl(XSLoader)
#Requires: perl(base)  conflicts with perl package
Requires: perl >= 5.008

%filter_from_requires /^perl*/d
%filter_setup

%description
Associate user-defined magic to variables from Perl.

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

### Clean up docs
find samples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README samples/
%doc %{_mandir}/man3/Variable::Magic.3pm*
%dir %{perl_vendorarch}/auto/Variable/
%{perl_vendorarch}/auto/Variable/Magic/
%dir %{perl_vendorarch}/Variable/
%{perl_vendorarch}/Variable/Magic.pm

%changelog
* Fri Oct 29 2010 Christoph Maser <cmaser@gmx.de> - 0.44-1
- Updated to version 0.44.

* Fri Mar 26 2010 Christoph Maser <cmr@financial.com> - 0.41-1
- Updated to version 0.41.

* Thu Jan  7 2010 Christoph Maser <cmr@financial.com> - 0.40-1
- Updated to version 0.40.

* Wed Dec  9 2009 Christoph Maser <cmr@financial.com> - 0.39-1
- Updated to version 0.39.

* Fri Oct 16 2009 Christoph Maser <cmr@financial.com> - 0.38-1
- Updated to version 0.38.

* Sat Aug 29 2009 Christoph Maser <cmr@financial.com> - 0.37-1
- Updated to version 0.37.

* Mon Jul  6 2009 Christoph Maser <cmr@financial.com> - 0.36-1
- Updated to version 0.36.

* Fri May 29 2009 Christoph Maser <cmr@financial.com> - 0.35-1
- Initial package. (using DAR)
