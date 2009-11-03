# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name XML-SAX-PurePerl

Summary: XML-SAX-PurePerl Perl module
Name: perl-XML-SAX-PurePerl
Version: 0.80
Release: 0.2%{?dist}
License: GPL or Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-SAX-PurePerl/

Source: http://www.cpan.org/modules/by-module/XML/XML-SAX-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl

%description
XML-SAX-PurePerl Perl module.

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
%doc Changes MANIFEST README
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/XML/
%dir %{perl_vendorlib}/XML/SAX/
%{perl_vendorlib}/XML/SAX/PurePerl.pm
%{perl_vendorlib}/XML/SAX/PurePerl/

%changelog
* Sun Aug 24 2003 Dag Wieers <dag@wieers.com> - 0.80-0
- Initial package. (using DAR)
