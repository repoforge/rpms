# $Id$
# Authority: dag
# Upstream: Peter Wainwright <peter$cybrid,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name SVG-Parser

Summary: Perl module that implements an XML Parser for SVG documents
Name: perl-SVG-Parser
Version: 1.01
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/SVG-Parser/

Source: http://www.cpan.org/modules/by-module/SVG/SVG-Parser-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
perl-SVG-Parser is a Perl module that implements an XML Parser
for SVG documents.

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
%doc CHANGES MANIFEST META.yml README
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/SVG/
%{perl_vendorlib}/SVG/Parser/
%{perl_vendorlib}/SVG/Parser.pm

%changelog
* Thu May 24 2007 Dag Wieers <dag@wieers.com> - 1.01-1
- Initial package. (using DAR)
