# $Id$
# Authority: dries
# Upstream: Makamaka Hannyaharamitu <makamaka$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Text-CSV

Summary: comma-separated values manipulator (using XS or PurePerl)
Name: perl-Text-CSV
Version: 1.05
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Text-CSV/

Source: http://www.cpan.org/modules/by-module/Text/Text-CSV-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Text::CSV provides facilities for the composition and decomposition of
comma-separated values.  An instance of the Text::CSV class can combine
fields into a CSV string and parse a CSV string into fields.

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Text::CSV.3pm*
%doc %{_mandir}/man3/Text::CSV_PP.3pm*
%dir %{perl_vendorlib}/Text/
#%{perl_vendorlib}/Text/CSV/
%{perl_vendorlib}/Text/CSV.pm
%{perl_vendorlib}/Text/CSV_PP.pm

%changelog
* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 1.05-1
- Updated to release 1.05.

* Fri Mar 14 2008 Dag Wieers <dag@wieers.com> - 1.02-1
- Updated to release 1.02.

* Fri Mar 07 2008 Dag Wieers <dag@wieers.com> - 1.01-1
- Updated to release 1.01.

* Tue Dec 04 2007 Dag Wieers <dag@wieers.com> - 1.00-1
- Updated to release 1.00.

* Mon Feb 28 2005 Dries Verachtert <dries@ulyssis.org> - 0.01-1
- Initial package.
