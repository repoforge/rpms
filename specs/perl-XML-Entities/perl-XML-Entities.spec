# $Id$
# Authority: cmr
# Upstream: Jan Oldrich Kruza <Sixtease+cpan@gmail.com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name XML-Entities

Summary: Mapping of XML entities to Unicode
Name: perl-XML-Entities
Version: 1.0000
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-Entities/

Source: http://search.cpan.org/CPAN/authors/id/S/SI/SIXTEASE/XML-Entities-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl(Carp)
BuildRequires: perl(Test::More)
BuildRequires: perl >= 5.008
Requires: perl(Carp)
Requires: perl >= 5.008

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup


%description
Mapping of XML entities to Unicode.

%prep
%setup -n %{real_name}

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
%doc %{_mandir}/man3/XML::Entities.3pm*
%doc %{_mandir}/man3/XML::Entities::Data.3pm*
%doc %{_mandir}/man1/download-entities.pl.1*
%doc %{_mandir}/man3/download-entities.pl.3pm*
%dir %{perl_vendorlib}/XML/
%{perl_vendorlib}/XML/Entities/
%{perl_vendorlib}/XML/Entities.pm
%{_bindir}/download-entities.pl


%changelog
* Mon Feb  7 2011 Christoph Maser <cmaser@gmx.de> - 1.0000-1
- Updated to version 1.0000.

* Mon Mar 16 2009 Unknown - 0.0307-1
- Initial package. (using DAR)
