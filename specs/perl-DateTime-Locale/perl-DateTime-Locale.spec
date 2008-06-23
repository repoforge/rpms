# $Id$
# Authority: dries
# Upstream: Dave Rolsky <autarch$urth,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name DateTime-Locale

Summary: Localization support for DateTime.pm
Name: perl-DateTime-Locale
Version: 0.4001
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DateTime-Locale/

Source: http://www.cpan.org/modules/by-module/DateTime/DateTime-Locale-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.006
Requires: perl >= 0:5.006

%description
The DateTime::Locale modules provide localization data for the
DateTime.pm class.

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
%doc Changes LICENSE LICENSE.cldr MANIFEST MANIFEST.SKIP MANIFEST.base META.yml README SIGNATURE
%doc %{_mandir}/man3/DateTime::Locale.3pm*
%doc %{_mandir}/man3/DateTime::LocaleCatalog.3pm*
%doc %{_mandir}/man3/DateTime::Locale::*.3pm*
%dir %{perl_vendorlib}/DateTime/
%{perl_vendorlib}/DateTime/Locale/
%{perl_vendorlib}/DateTime/Locale.pm
%{perl_vendorlib}/DateTime/LocaleCatalog.pm

%changelog
* Sun Jun 22 2008 Dag Wieers <dag@wieers.com> - 0.4001-1
- Updated to release 0.4001.

* Mon Nov 05 2007 Dag Wieers <dag@wieers.com> - 0.35-1
- Updated to release 0.35.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 0.22-1
- Updated to release 0.22.

* Fri Mar  4 2005 Dries Verachtert <dries@ulyssis.org> - 0.21-1
- Updated to release 0.21.

* Mon Dec 06 2004 Dries Verachtert <dries@ulyssis.org> - 0.09-1
- Initial package.
