# $Id$
# Authority: dries
# Upstream: H. Merijn Brand <h,merijn$xs4all,nl>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Text-CSV_XS

Summary: Comma-separated values manipulation routines
Name: perl-Text-CSV_XS
Version: 0.33
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Text-CSV_XS/

Source: http://www.cpan.org/modules/by-module/Text/Text-CSV_XS-%{version}.tgz
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

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog MANIFEST META.yml README examples/
%doc %{_mandir}/man3/Text::CSV_XS.3pm*
%dir %{perl_vendorarch}/auto/Text/
%{perl_vendorarch}/auto/Text/CSV_XS/
%dir %{perl_vendorarch}/Text/
%{perl_vendorarch}/Text/CSV_XS.pm

%changelog
* Fri Jan 04 2008 Dag Wieers <dag@wieers.com> - 0.33-1
- Updated to release 0.33.

* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 0.32-1
- Updated to release 0.32.

* Tue Mar  1 2005 Dries Verachtert <dries@ulyssis.org> - 0.23-1
- Initial package.
