# $Id$
# Authority: dries
# Upstream: Barbie <barbie$missbarbell,co,uk>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Data-Phrasebook-Loader-XML

Summary: Absract your phrases with XML
Name: perl-Data-Phrasebook-Loader-XML
Version: 0.12
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Data-Phrasebook-Loader-XML/

Source: http://search.cpan.org//CPAN/authors/id/B/BA/BARBIE/Data-Phrasebook-Loader-XML-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Absract your phrases with XML.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/*/*/.packlist

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
