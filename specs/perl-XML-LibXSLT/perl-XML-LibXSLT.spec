# $Id$
# Authority: shuff
# Upstream: Petr Pajas <pajas$matfyz,cz>
# ExcludeDist: el4 el3

# Newer versions require a later libxslt than available in el5

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name XML-LibXSLT

Summary: Interface to Gnome libxslt library
Name: perl-XML-LibXSLT
Version: 1.63
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-LibXSLT/

Source: http://search.cpan.org/CPAN/authors/id/P/PA/PAJAS/XML-LibXSLT-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libxslt-devel >= 1.0.6
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
# XML::LibXML 1.70 introduces a non-backwards-compatible ABI
BuildRequires: perl(XML::LibXML) >= 1.60, perl(XML::LibXML) <= 1.69
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

### Clean up docs
find example/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README example/
%doc %{_mandir}/man3/XML::LibXSLT.3pm*
%dir %{perl_vendorarch}/auto/XML/
%{perl_vendorarch}/auto/XML/LibXSLT/
%dir %{perl_vendorarch}/XML/
%{perl_vendorarch}/XML/LibXSLT.pm
%{perl_vendorarch}/XML/benchmark.pl

%changelog
* Tue May 18 2010 Steve Huff <shuff@vecna.org> - 1.63-2
- Reverted to 1.63 (later versions can't build on el5).
- Captured dependencies more precisely.

* Tue May 18 2010 Steve Huff <shuff@vecna.org> - 1.70-1
- Updated to release 1.70.

* Wed Feb 20 2008 Dag Wieers <dag@wieers.com> - 1.66-1
- Updated to release 1.66.

* Fri Nov 09 2007 Dag Wieers <dag@wieers.com> - 1.63-1
- Updated to release 1.63.

* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 1.62-1
- Updated to release 1.62.

* Tue Sep 26 2006 Dries Verachtert <dries@ulyssis.org> - 1.61-1
- Updated to release 1.61.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 1.60-1
- Updated to release 1.60.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 1.58-1
- Updated to release 1.58.

* Sun Mar  6 2005 Dries Verachtert <dries@ulyssis.org> - 1.57-1
- Initial package.
