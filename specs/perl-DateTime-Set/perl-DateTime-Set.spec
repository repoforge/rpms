# $Id$
# Authority: dries
# Upstream:Flávio Soibelmann Glock <fglock$pucrs,br>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name DateTime-Set

Summary: Datetime sets and set math
Name: perl-DateTime-Set
Version: 0.27
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DateTime-Set/

Source: http://www.cpan.org/modules/by-module/DateTime/DateTime-Set-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Buildarch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
The DateTime::Set module provides a date/time sets implementation.

It allows, for example, the generation of groups of dates,
like "every wednesday", and then find all the dates matching that
pattern, within a time range.

%prep
%setup -n %{real_name}-%{version}

%{__perl} -pi -e 's|use Set::Infinite 0.5502;|use Set::Infinite;|g;' lib/Set/Infinite/_recurrence.pm

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
%doc %{_mandir}/man3/*
%{perl_vendorlib}/DateTime/
%dir %{perl_vendorlib}/Set/
%{perl_vendorlib}/Set/Infinite/

%changelog
* Tue Jul  7 2009 Christoph Maser <cmr@financial.com> - 0.27-1
- Updated to version 0.27.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.25-2.2
- Rebuild for Fedora Core 5.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 0.25-1
- Updated to release 0.25.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 0.22-1
- Updated to release 0.22.

* Fri Mar  4 2005 Dries Verachtert <dries@ulyssis.org> - 0.20-1
- Updated to release 0.20.

* Wed Dec 08 2004 Dries Verachtert <dries@ulyssis.org> - 0.19-2
- Requirements fixes.

* Mon Dec 06 2004 Dries Verachtert <dries@ulyssis.org> - 0.19-1
- Initial package.
