# $Id$
# Authority: dries
# Upstream: Jochen Wiedmann <jwied$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Text-CSV_XS

Summary: Comma-separated values manipulation routines
Name: perl-Text-CSV_XS
Version: 0.23
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Text-CSV_XS/

Source: http://www.cpan.org/modules/by-module/Text/Text-CSV_XS-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Text::CSV provides facilities for the composition and decomposition of
comma-separated values.  An instance of the Text::CSV class can combine
fields into a CSV string and parse a CSV string into fields.

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

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog README
%doc %{_mandir}/man3/*
%dir %{perl_vendorarch}/Text/
%{perl_vendorarch}/Text/CSV_XS.pm
%dir %{perl_vendorarch}/auto/Text/
%{perl_vendorarch}/auto/Text/CSV_XS/

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.23-1.2
- Rebuild for Fedora Core 5.

* Tue Mar  1 2005 Dries Verachtert <dries@ulyssis.org> - 0.23-1
- Initial package.
