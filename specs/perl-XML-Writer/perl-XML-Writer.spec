# $Id$
# Authority: dries
# Upstream: David Megginson <david$megginson,com>
# Upstream: Ed Avis <ed$membled,com>
# Upstream: Joseph Walton <joe$kafsemo,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name XML-Writer

Summary: Extension for writing XML documents
Name: perl-XML-Writer
Version: 0.603
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-Writer/

Source: http://www.cpan.org/modules/by-module/XML/XML-Writer-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.006
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This module contains a perl extension for writing XML documents.

This package contains the following Perl module:

    XML::Writer

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
%doc Changes MANIFEST META.yml README TODO
%doc %{_mandir}/man3/XML::Writer.3pm*
%dir %{perl_vendorlib}/XML/
#%{perl_vendorlib}/XML/Writer/
%{perl_vendorlib}/XML/Writer.pm

%changelog
* Mon Nov 05 2007 Dag Wieers <dag@wieers.com> - 0.603-1
- Updated to release 0.603.

* Tue Nov 14 2006 Dries Verachtert <dries@ulyssis.org> - 0.602-1
- Updated to release 0.602.

* Tue Sep 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.601-1
- Updated to release 0.601.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 0.600-1
- Updated to release 0.600.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 0.545-1
- Updated to release 0.545.

* Fri Mar  4 2005 Dries Verachtert <dries@ulyssis.org> - 0.530-1
- Updated to release 0.530.

* Mon Dec 20 2004 Dag Wieers <dag@wieers.com> - 0.520-1
- Updated to release 0.520.

* Wed Jun 16 2004 Dries Verachtert <dries@ulyssis.org> - 0.510-1
- Initial package.
