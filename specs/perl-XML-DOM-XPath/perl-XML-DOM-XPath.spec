# $Id$
# Authority: dries
# Upstream: Michel Rodriguez <mirod$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name XML-DOM-XPath

Summary: Perl extension to add XPath support to XML::DOM, using XML::XPath engine
Name: perl-XML-DOM-XPath
Version: 0.14
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-DOM-XPath/

Source: http://www.cpan.org/modules/by-module/XML/XML-DOM-XPath-%{version}.tar.gz
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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/XML::DOM::XPath.3pm*
%dir %{perl_vendorlib}/XML/
%dir %{perl_vendorlib}/XML/DOM/
#%{perl_vendorlib}/XML/DOM/XPath/
%{perl_vendorlib}/XML/DOM/XPath.pm


%changelog
* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 0.14-1
- Updated to release 0.14.

* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 0.13-1
- Updated to release 0.13.

* Tue Sep 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.12-1
- Initial package.
