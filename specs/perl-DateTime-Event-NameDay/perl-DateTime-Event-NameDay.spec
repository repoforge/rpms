# $Id$
# Authority: dries
# Upstream: Benjamin Bennett <fiji$limey,net>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name DateTime-Event-NameDay

Summary: Perl DateTime extension to work with namedays from various countries
Name: perl-DateTime-Event-NameDay
Version: 0.02
Release: 1.2
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DateTime-Event-NameDay/

Source: http://www.cpan.org/modules/by-module/DateTime/DateTime-Event-NameDay-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl-Module-Build

%description
This module handles generating name days from dates and vice versa.

%prep
%setup -n %{real_name}-%{version}

%build
# does not work with PREFIX, needs destdir
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
%dir %{perl_vendorlib}/DateTime/Event/
%{perl_vendorlib}/DateTime/Event/NameDay.pm
%{perl_vendorlib}/DateTime/Event/NameDay/*

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.02-1.2
- Rebuild for Fedora Core 5.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 0.02-1
- Initial package.
