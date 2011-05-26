# $Id$
# Authority: cmr
# Upstream: Ricardo Signes <rjbs$cpan,org>
# needs new ExtutilsMakeMaker
# ExcludeDist: el4

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Software-License
%define real_version 0.103001

Summary: packages that provide templated software licenses
Name: perl-Software-License
Version: 0.013.1
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Software-License/

Source: http://www.cpan.org/authors/id/R/RJ/RJBS/Software-License-%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.6.0
BuildRequires: perl(ExtUtils::MakeMaker) >= 6.31
BuildRequires: perl(Data::Section)
BuildRequires: perl(Sub::Install)
BuildRequires: perl(Test::More)
BuildRequires: perl(Text::Template)
Requires: perl >= 0:5.6.0
%{?real_version:Provides: perl(Software::License) = %{real_version}}

%description
packages that provide templated software licenses.

%prep
%setup -n %{real_name}-%{real_version}

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
%doc Changes LICENSE MANIFEST META.json README
%doc %{_mandir}/man?/*
%dir %{perl_vendorlib}/Software/
%{perl_vendorlib}/Software/License/
%{perl_vendorlib}/Software/License.pm
%{perl_vendorlib}/Software/LicenseUtils.pm

%changelog
* Thu May 26 2011 Steve Huff <shuff@vecna.org> - 0.013.1-1
- Updated to release 0.013001.

* Sun Aug 02 2009 Christoph Maser <cmr@financial.com> - 0.012-1
- Initial package. (using DAR)
