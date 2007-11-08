# $Id$

# Authority: dries
# Upstream: Leo Lapworth <LLAP$cuckoo,org>

%define real_name Text-vCard
%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

Summary: Edit and create a single vCard (RFC 2426)
Name: perl-Text-vCard
Version: 2.00
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Text-vCard/

Source: http://www.cpan.org/modules/by-module/Text/Text-vCard-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
With this module you can create and edit a single vCard (RFC 2426).

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX=%{buildroot}%{_prefix}
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
%doc Changes TODO
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Text/vCard.pm
%{perl_vendorlib}/Text/vCard

%changelog
* Tue Nov 14 2006 Dries Verachtert <dries@ulyssis.org> - 2.00-1
- Updated to release 2.00.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 1.99-1
- Updated to release 1.99.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.96-1.2
- Rebuild for Fedora Core 5.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 1.96-1
- Updated to release 1.96.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 1.94-1
- Updated to release 1.94.

* Wed Mar  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.93-1
- Initial package.
