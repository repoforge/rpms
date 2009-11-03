# $Id$
# Authority: dag
# Upstream: Peter Wainwright <peter,wainwright$cybrid,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name SVG-Parser

Summary: Perl module that implements an XML Parser for SVG documents
Name: perl-SVG-Parser
Version: 1.03
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/SVG-Parser/

Source: http://www.cpan.org/modules/by-module/SVG/SVG-Parser-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Module::Build)

%description
perl-SVG-Parser is a Perl module that implements an XML Parser
for SVG documents.

%prep
%setup -n %{real_name}-%{version}

%build
#%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
#%{__make} %{?_smp_mflags}
%{__perl} Build.PL
./Build

%install
%{__rm} -rf %{buildroot}
#%{__make} pure_install
PERL_INSTALL_ROOT="%{buildroot}" ./Build install installdirs="vendor"

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES MANIFEST META.yml README examples/
%doc %{_mandir}/man3/SVG::Parser.3pm*
%doc %{_mandir}/man3/SVG::Parser::*.3pm*
%dir %{perl_vendorlib}/SVG/
%{perl_vendorlib}/SVG/Parser/
%{perl_vendorlib}/SVG/Parser.pm

%changelog
* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 1.03-1
- Updated to release 1.03.

* Thu May 24 2007 Dag Wieers <dag@wieers.com> - 1.01-1
- Initial package. (using DAR)
