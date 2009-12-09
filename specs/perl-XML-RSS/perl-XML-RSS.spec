# $Id$
# Authority: dries
# Upstream: Shlomi Fish <shlomif$iglu,org,il>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name XML-RSS

Summary: Creates and updates RSS files
Name: perl-XML-RSS
Version: 1.47
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-RSS/

Source: http://search.cpan.org/CPAN/authors/id/S/SH/SHLOMIF/XML-RSS-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(DateTime)
BuildRequires: perl(DateTime::Format::Mail)
BuildRequires: perl(DateTime::Format::W3CDTF)
BuildRequires: perl(HTML::Entities)
BuildRequires: perl(Test::Manifest) >= 0.9
#BuildRequires: perl(Test::More) conflicts with perl package
BuildRequires: perl(XML::Parser) >= 2.23
BuildRequires: perl >= 5.008
Requires: perl(DateTime)
Requires: perl(DateTime::Format::Mail)
Requires: perl(DateTime::Format::W3CDTF)
Requires: perl(HTML::Entities)
Requires: perl(XML::Parser) >= 2.23
Requires: perl >= 5.008

%filter_from_requires /^perl*/d
%filter_setup


%description
This module was created to help those who need to manage
RDF Site Summary (RSS) files. It makes quick work of
creating, updating, and saving RSS files.

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
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README TODO examples/
%doc %{_mandir}/man3/XML::RSS.3pm*
%dir %{perl_vendorlib}/XML/
%{perl_vendorlib}/XML/RSS/
%{perl_vendorlib}/XML/RSS.pm

%changelog
* Wed Dec  9 2009 Christoph Maser <cmr@financial.com> - 1.47-1
- Updated to version 1.47.

* Fri Oct 16 2009 Christoph Maser <cmr@financial.com> - 1.46-1
- Updated to version 1.46.

* Sat Aug 29 2009 Christoph Maser <cmr@financial.com> - 1.45-1
- Updated to version 1.45.

* Fri May 29 2009 Christoph Maser <cmr@financial.com> - 1.44-1
- Updated to version 1.44.

* Thu Feb 21 2008 Dag Wieers <dag@wieers.com> - 1.32-1
- Updated to release 1.32.

* Tue Nov 06 2007 Dag Wieers <dag@wieers.com> - 1.31-1
- Updated to release 1.31.

* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 1.22-1
- Updated to release 1.22.

* Tue Nov 14 2006 Dries Verachtert <dries@ulyssis.org> - 1.20-1
- Updated to release 1.20.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 1.10-1
- Updated to release 1.10.

* Sun Dec 19 2004 Dries Verachtert <dries@ulyssis.org> - 1.05
- Initial package.
