# $Id$
# Authority: dries
# Upstream: Alexander Karelas <karjala$karjala,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name XML-MyXML

Summary: Simple-to-use XML module, for parsing and creating XML documents
Name: perl-XML-MyXML
Version: 0.08
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-MyXML/

Source: http://search.cpan.org//CPAN/authors/id/K/KA/KARJALA/MyXML/XML-MyXML-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
Simple-to-use XML module, for parsing and creating XML documents.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/XML::MyXML*
%{perl_vendorlib}/XML/MyXML.pm

%changelog
* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.08-1
- Initial package.
