# $Id$
# Authority: dries
# Upstream: Dave Rolsky <autarch$urth,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name DateTime-Locale

Summary: Localization support for DateTime
Name: perl-DateTime-Locale
Version: 0.22
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DateTime-Locale/

Source: http://www.cpan.org/modules/by-module/DateTime/DateTime-Locale-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl-Module-Build, perl

%description
The DateTime::Locale modules provide localization data for the
DateTime.pm class.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" destdir="%{buildroot}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} \
		%{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/DateTime/
%{perl_vendorlib}/DateTime/Locale.pm
%{perl_vendorlib}/DateTime/Locale/
%{perl_vendorlib}/DateTime/LocaleCatalog.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.22-1.2
- Rebuild for Fedora Core 5.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 0.22-1
- Updated to release 0.22.

* Fri Mar  4 2005 Dries Verachtert <dries@ulyssis.org> - 0.21-1
- Updated to release 0.21.

* Mon Dec 06 2004 Dries Verachtert <dries@ulyssis.org> - 0.09-1
- Initial package.
