# $Id$
# Authority: cmr
# Upstream: Michael Koehne <kraehe$copyleft,de>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name XML-Edifact

Summary: Perl module named XML-Edifact
Name: perl-XML-Edifact
Version: 0.47
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-Edifact/

Source: http://www.cpan.org/modules/by-module/XML/XML-Edifact-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(XML::Parser)

%description
perl-XML-Edifact is a Perl module.

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

### Clean up docs
find doc/ examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc MANIFEST README doc/ examples/
%doc %{_mandir}/man1/edi2xml.1.gz
%doc %{_mandir}/man1/xml2edi.1.gz
%doc %{_mandir}/man3/XML::Edifact.3.gz*
%{_bindir}/edi2xml
%{_bindir}/xml2edi
%dir %{perl_vendorlib}/XML/
%{perl_vendorlib}/XML/Edifact.pm
%{perl_vendorlib}/XML/Edifact/Config.pm
%{perl_vendorlib}/XML/Edifact/d96b/codes.dat.dir
%{perl_vendorlib}/XML/Edifact/d96b/codes.dat.pag
%{perl_vendorlib}/XML/Edifact/d96b/composite.dat.dir
%{perl_vendorlib}/XML/Edifact/d96b/composite.dat.pag
%{perl_vendorlib}/XML/Edifact/d96b/element.dat.dir
%{perl_vendorlib}/XML/Edifact/d96b/element.dat.pag
%{perl_vendorlib}/XML/Edifact/d96b/segment.dat.dir
%{perl_vendorlib}/XML/Edifact/d96b/segment.dat.pag
%{perl_vendorlib}/XML/Edifact/d96b/segment.rev.dir
%{perl_vendorlib}/XML/Edifact/d96b/segment.rev.pag


%changelog
* Thu Aug 20 2009 Unknown - 0.47-1
- Initial package. (using DAR)
