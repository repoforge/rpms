# $Id$
# Authority: dries
# Upstream: Michel Rodriguez <mirod$xmltwig,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name XML-DOM-XPath

Summary: XPath support for XML::DOM
Name: perl-XML-DOM-XPath
Version: 0.13
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-DOM-XPath/

Source: http://search.cpan.org//CPAN/authors/id/M/MI/MIROD/XML-DOM-XPath-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
XML::DOM::XPath is a helper module for XML::DOM that adds XPath support to it.
It uses XML::XPath to resolve the XPath queries.

In truth this should only be used if you have existing code using XML::DOM. 
If you start a new project and if you can install XML::LibXML (and libxml2 
on which it is based) then you will get a DOM, XPAth support and a lot more
power and speed.

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
%doc Changes README
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/XML/DOM/
%{perl_vendorlib}/XML/DOM/XPath.pm

%changelog
* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 0.13-1
- Updated to release 0.13.

* Tue Sep 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.12-1
- Initial package.
