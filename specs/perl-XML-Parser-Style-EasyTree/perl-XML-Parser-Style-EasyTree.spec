# $Id:$
# Authority: cmr
# Upstream: Mons Anderson <mons@cpan.org>
# ExcludeDist: el4

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name XML-Parser-Style-EasyTree

Summary: Parse xml to simple tree
Name: perl-XML-Parser-Style-EasyTree
Version: 0.09
Release: 2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-Parser-Style-EasyTree/

Source: http://search.cpan.org/CPAN/authors/id/M/MO/MONS/XML-Parser-Style-EasyTree-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
#BuildRequires: perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Test::More)
BuildRequires: perl(XML::Parser)
BuildRequires: perl(lib::abs) >= 0.90
BuildRequires: perl >= 5.6.2
Requires: perl(Scalar::Util)
Requires: perl >= 5.6.2

%filter_from_requires /^perl*/d
%filter_setup


%description
Parse xml to simple tree.

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
%doc Changes LICENSE MANIFEST META.yml README
%doc %{_mandir}/man3/XML::Parser::Style::EasyTree.3pm*
%doc %{_mandir}/man3/XML::Parser::Style::ETree.3pm*
%dir %{perl_vendorlib}/XML/
%dir %{perl_vendorlib}/XML/Parser/
%dir %{perl_vendorlib}/XML/Parser/Style/
%{perl_vendorlib}/XML/Parser/Style/ETree.pm
%{perl_vendorlib}/XML/Parser/Style/cpants.pl
%{perl_vendorlib}/XML/Parser/Style/EasyTree.pm

%changelog
* Sat Feb 06 2010 Christoph Maser <cmr@financial.com> - 0.09-2
- Cleanup, trigger rebuild

* Tue Sep 29 2009 Christoph Maser <cmr@financial.com> - 0.09-1
- Initial package. (using DAR)
