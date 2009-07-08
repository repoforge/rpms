# $Id$
# Authority: cmr
# Upstream: Michael Stillwell <mjs$beebo,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name XML-LibXML-Enhanced

Summary: Perl module named XML-LibXML-Enhanced
Name: perl-XML-LibXML-Enhanced
Version: 0.01
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-LibXML-Enhanced/

Source: http://www.cpan.org/modules/by-module/XML/XML-LibXML-Enhanced-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-XML-LibXML-Enhanced is a Perl module.

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
%doc MANIFEST META.yml
%doc %{_mandir}/man3/XML::LibXML::*.3pm*
%dir %{perl_vendorlib}/XML/
%dir %{perl_vendorlib}/XML/LibXML/
%{perl_vendorlib}/XML/LibXML

%changelog
* Wed Jul 08 2009 Christoph Maser <cmr@financial.com> - 0.01-1
- Initial package. (using DAR)
