# $Id$
# Authority: dag
# Upstream: Michel Rodriguez <xmltwig$gmail,com>

### EL6 ships with perl-XML-Twig-3.34-1.el6
%{?el6:# Tag: rfx}
### EL5 ships with perl-XML-Twig-3.26-1.fc6
%{?el5:# Tag: rfx}
### EL4 ships with perl-XML-Twig-3.13-6
%{?el4:# Tag: rfx}
### EL3 ships with perl-XML-Twig-3.09-3
%{?el3:# Tag: rfx}
### EL2 ships with perl-XML-Twig-2.02-2
%{?el2:# Tag: rfx}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name XML-Twig

Summary: Perl module for processing huge XML documents in tree mode
Name: perl-XML-Twig
Version: 3.34
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-Twig/

Source: http://search.cpan.org/CPAN/authors/id/M/MI/MIROD/XML-Twig-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(XML::Parser) >= 2.23
Requires: perl(XML::Parser) >= 2.23

%filter_from_requires /^perl*/d
%filter_setup


%description
perl-XML-Twig is a Perl module for processing huge XML documents in tree mode.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL -y INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
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
%doc %{_mandir}/man1/xml_grep.1*
%doc %{_mandir}/man1/xml_merge.1*
%doc %{_mandir}/man1/xml_pp.1*
%doc %{_mandir}/man1/xml_spellcheck.1*
%doc %{_mandir}/man1/xml_split.1*
%doc %{_mandir}/man3/XML::Twig.3pm*
%{_bindir}/xml_grep
%{_bindir}/xml_merge
%{_bindir}/xml_pp
%{_bindir}/xml_spellcheck
%{_bindir}/xml_split
%dir %{perl_vendorlib}/XML/
%{perl_vendorlib}/XML/Twig/
%{perl_vendorlib}/XML/Twig.pm

%changelog
* Wed Feb  3 2010 Christoph Maser <cmr@financial.com> - 3.34-1
- Updated to version 3.34.

* Mon Nov 19 2007 Dag Wieers <dag@wieers.com> - 3.32-1
- Updated to release 3.32.

* Sun Aug 05 2007 Dag Wieers <dag@wieers.com> - 3.29-1
- Initial package. (using DAR)
