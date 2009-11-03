# $Id$
# Authority: dries
# Upstream: Alexander Karelas <karjala$karjala,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name XML-MyXML

Summary: Simple-to-use XML module, for parsing and creating XML documents
Name: perl-XML-MyXML
Version: 0.0986
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-MyXML/

Source: http://www.cpan.org/modules/by-module/XML/XML-MyXML-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Simple-to-use XML module, for parsing and creating XML documents.

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
%doc %{_mandir}/man3/XML::MyXML.3pm*
%dir %{perl_vendorlib}/XML/
#%{perl_vendorlib}/XML/MyXML/
%{perl_vendorlib}/XML/MyXML.pm

%changelog
* Mon Nov 19 2007 Dag Wieers <dag@wieers.com> - 0.0986-1
- Updated to release 0.0986.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.08-1
- Initial package.
