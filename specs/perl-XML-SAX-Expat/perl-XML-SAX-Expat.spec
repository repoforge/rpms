# $Id$
# Authority: dag
# Upstream: Björn Höhrmann <bjoern$hoehrmann,de>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name XML-SAX-Expat

Summary: Perl module is a SAX2 Driver for Expat (XML::Parser)
Name: perl-XML-SAX-Expat
Version: 0.40
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-SAX-Expat/

Source: http://www.cpan.org/modules/by-module/XML/XML-SAX-Expat-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-XML-SAX-Expat is a Perl module is a SAX2 Driver for Expat (XML::Parser).

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
%doc Changes MANIFEST META.yml
%doc %{_mandir}/man3/XML::SAX::Expat.3pm*
%dir %{perl_vendorlib}/XML/
%dir %{perl_vendorlib}/XML/SAX/
%{perl_vendorlib}/XML/SAX/Expat.pm

%changelog
* Fri May 29 2009 Christoph Maser <cmr@financial.com> - 0.40-1
- Updated to version 0.40.

* Sun Aug 05 2007 Dag Wieers <dag@wieers.com> - 0.39-1
- Initial package. (using DAR)
