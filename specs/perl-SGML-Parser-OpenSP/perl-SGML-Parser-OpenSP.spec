# $Id$
# Authority: dag
# Upstream: Björn Höhrmann <bjoern$hoehrmann,de>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name SGML-Parser-OpenSP

Summary: Perl module to parse SGML documents using OpenSP
Name: perl-SGML-Parser-OpenSP
Version: 0.994
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/SGML-Parser-OpenSP/

Source: http://www.cpan.org/modules/by-module/SGML/SGML-Parser-OpenSP-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: opensp-devel
BuildRequires: perl(ExtUtils::MakeMaker)

%description
perl-SGML-Parser-OpenSP is a Perl module to parse SGML documents using OpenSP.

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
%doc %{_mandir}/man3/SGML::Parser::OpenSP.3pm*
%doc %{_mandir}/man3/SGML::Parser::OpenSP::Tools.3pm*
%dir %{perl_vendorarch}/auto/SGML/
%dir %{perl_vendorarch}/auto/SGML/Parser/
%{perl_vendorarch}/auto/SGML/Parser/OpenSP/
%dir %{perl_vendorarch}/SGML/
%dir %{perl_vendorarch}/SGML/Parser/
%{perl_vendorarch}/SGML/Parser/OpenSP/
%{perl_vendorarch}/SGML/Parser/OpenSP.pm

%changelog
* Thu Jun 18 2009 Christoph Maser <cmr@financial.com> - 0.994-1
- Updated to version 0.994.

* Sat Dec 08 2007 Dag Wieers <dag@wieers.com> - 0.991-1
- Updated to release 0.991.

* Sun Aug 05 2007 Dag Wieers <dag@wieers.com> - 0.99-1
- Initial package. (using DAR)
