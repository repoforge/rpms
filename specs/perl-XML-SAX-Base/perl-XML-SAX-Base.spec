# $Id$
# Authority: dag
# Upstream: Kip Hampton <khampton$totalcinema,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name XML-SAX-Base

Summary: XML-SAX-Base Perl module
Name: perl-XML-SAX-Base
Version: 1.04
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-SAX-Base/

Source: http://www.cpan.org/modules/by-module/XML/XML-SAX-Base-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl

%description
XML-SAX-Base Perl module.

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
%doc %{_mandir}/man3/XML::SAX::Base.3pm*
%doc %{_mandir}/man3/XML::SAX::Exception.3pm*
%dir %{perl_vendorlib}/XML/
%dir %{perl_vendorlib}/XML/SAX/
%{perl_vendorlib}/XML/SAX/Base.pm
%{perl_vendorlib}/XML/SAX/Exception.pm
%{perl_vendorlib}/XML/SAX/placeholder.pl

%changelog
* Sun Aug 05 2007 Dag Wieers <dag@wieers.com> - 1.04-1
- Cosmetic cleanup.

* Sun Aug 24 2003 Dag Wieers <dag@wieers.com> - 1.04-0
- Initial package. (using DAR)
