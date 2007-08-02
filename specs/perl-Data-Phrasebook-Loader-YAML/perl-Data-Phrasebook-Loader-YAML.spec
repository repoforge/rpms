# $Id$
# Authority: dries
# Upstream: Barbie <barbie$missbarbell,co,uk>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Data-Phrasebook-Loader-YAML

Summary: Absract your phrases with YAML
Name: perl-Data-Phrasebook-Loader-YAML
Version: 0.06
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Data-Phrasebook-Loader-YAML/

Source: http://search.cpan.org//CPAN/authors/id/B/BA/BARBIE/Data-Phrasebook-Loader-YAML-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Absract your phrases with YAML.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/Data::Phrasebook::Loader::YAML*
%{perl_vendorlib}/Data/Phrasebook/Loader/YAML.pm

%changelog
* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.06-1
- Initial package.
