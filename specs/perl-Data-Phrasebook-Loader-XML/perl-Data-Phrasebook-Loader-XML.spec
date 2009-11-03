# $Id$
# Authority: dries
# Upstream: Barbie <barbie$missbarbell,co,uk>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Data-Phrasebook-Loader-XML

Summary: Absract your phrases with XML
Name: perl-Data-Phrasebook-Loader-XML
Version: 0.12
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Data-Phrasebook-Loader-XML/

Source: http://www.cpan.org/modules/by-module/Data/Data-Phrasebook-Loader-XML-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Absract your phrases with XML.

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
%doc Changes README
%doc %{_mandir}/man3/Data::Phrasebook::Loader::XML*
%{perl_vendorlib}/Data/Phrasebook/Loader/XML.pm
%dir %{perl_vendorlib}/Data/Phrasebook/Loader/
%dir %{perl_vendorlib}/Data/Phrasebook/

%changelog
* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.12-1
- Initial package.
