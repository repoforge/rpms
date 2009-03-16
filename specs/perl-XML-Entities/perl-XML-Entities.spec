# $Id$
# Authority: cmr
# Upstream: Oldrich Kruza <sixtease$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name XML-Entities

Summary: Mapping of XML entities to Unicode
Name: perl-XML-Entities
Version: 0.0307
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-Entities/

Source: http://www.cpan.org/modules/by-module/XML/XML-Entities-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 1:5.008
BuildRequires: perl(Test::More)
BuildRequires: perl-libwww-perl
Requires: perl >= 1:5.008
Requires: perl-libwww-perl

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
%doc %{_mandir}/man1/download-entities.pl.1.gz
%dir %{perl_vendorlib}/XML/
%{perl_vendorlib}/XML/Entities/
%{perl_vendorlib}/XML/Entities.pm
%{_bindir}/download-entities.pl


%changelog
* Mon Mar 16 2009 Unknown - 0.0307-1
- Initial package. (using DAR)
