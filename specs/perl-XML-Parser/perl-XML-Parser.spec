# $Id$
# Authority: dag
# Upstream: Matt Sergeant <msergeant$cpan,org>

### EL6 ships with perl-XML-Parser-2.36-7.el6
%{?el6:# Tag: rfx}
### EL5 ships with perl-XML-Parser-2.34-6.1.2.2.1
%{?el5:# Tag: rfx}
### EL4 ships with perl-XML-Parser-2.34-5
%{?el4:# Tag: rfx}
### EL3 ships with perl-XML-Parser-2.31-16.EL3
%{?el3:# Tag: rfx}
### EL2 ships with perl-XML-Parser-2.30-7
%{?el2:# Tag: rfx}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name XML-Parser

Summary: XML-Parser Perl module
Name: perl-XML-Parser
Version: 2.40
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-Parser/

Source: http://search.cpan.org/CPAN/authors/id/C/CH/CHORNY/XML-Parser-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: expat-devel
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(LWP)
BuildRequires: perl >= 5.00405
Requires: expat
Requires: perl(LWP)
Requires: perl >= 5.00405

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
XML-Parser Perl module.

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
find samples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README samples/
%doc %{_mandir}/man3/XML::Parser.3pm*
%doc %{_mandir}/man3/XML::Parser::*.3pm*
%dir %{perl_vendorarch}/auto/XML/
%dir %{perl_vendorarch}/auto/XML/Parser/
%{perl_vendorarch}/auto/XML/Parser/Expat/
%dir %{perl_vendorarch}/XML/
%{perl_vendorarch}/XML/Parser/
%{perl_vendorarch}/XML/Parser.pm

%changelog
* Mon Feb  7 2011 Christoph Maser <cmaser@gmx.de> - 2.40-1
- Updated to version 2.40.

* Sat Nov 24 2007 Dag Wieers <dag@wieers.com> - 2.36-1
- Updated to release 2.36.

* Mon Nov 19 2007 Dag Wieers <dag@wieers.com> - 2.35-1
- Updated to release 2.35.

* Tue Aug 07 2007 Dag Wieers <dag@wieers.com> - 2.34-2
- Disabled auto-requires for samples/.

* Fri Nov 12 2004 Dag Wieers <dag@wieers.com> - 2.34-1
- Workaround directory-conflicts bug in up2date. (RHbz #106123)

* Sat Dec 20 2003 Dag Wieers <dag@wieers.com> - 2.34-0
- Initial package. (using DAR)
