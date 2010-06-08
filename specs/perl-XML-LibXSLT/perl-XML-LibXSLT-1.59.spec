# $Id$
# Authority: dries
# Upstream: Petr Pajas <pajas$matfyz,cz>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name XML-LibXSLT

Summary: Interface to the gnome libxslt library
Name: perl-XML-LibXSLT
Version: 1.59
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-LibXSLT/

Source: http://www.cpan.org/modules/by-module/XML/XML-LibXSLT-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: libxslt-devel
### XML::LibXML 1.70 introduces a non-backwards-compatible ABI
BuildRequires: perl(XML::LibXML) >= 1.58, perl(XML::LibXML) < 1.70
Conflicts: perl-XML-LibXML >= 1.70

%description
perl-XML-LibXSLT is a fast XSLT library, based on the Gnome libxslt engine
that you can find at http://www.xmlsoft.org/XSLT/

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

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
%doc %{_mandir}/man3/XML::LibXSLT.3pm*
%dir %{perl_vendorarch}/XML/
%{perl_vendorarch}/XML/benchmark.pl
%{perl_vendorarch}/XML/LibXSLT.pm
%dir %{perl_vendorarch}/auto/XML/
%{perl_vendorarch}/auto/XML/LibXSLT/

%changelog
* Wed Jun 20 2007 Dag Wieers <dag@wieers.com> - 1.59-1
- Updated to release 1.59.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 1.58-1
- Updated to release 1.58.

* Sun Mar  6 2005 Dries Verachtert <dries@ulyssis.org> - 1.57-1
- Initial package.
