# $Id$
# Authority: dries
# Upstream: Pete Krawczyk <petek$bsod,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name HTML-Tree

Summary: HTML-Tree module for perl
Name: perl-HTML-Tree
Version: 3.23
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/HTML-Tree/

Source: http://www.cpan.org/modules/by-module/HTML/HTML-Tree-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 2:5.8.0
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl >= 2:5.8.0

%description
HTML-Tree module for perl.

This package contains the following Perl module:

    HTML::AsSubs

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
%doc Changes MANIFEST META.yml README TODO
%doc %{_mandir}/man3/*.3pm*
%{perl_vendorlib}/HTML/

%changelog
* Tue Nov 14 2006 Dries Verachtert <dries@ulyssis.org> - 3.23-1
- Updated to release 3.23.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 3.21-1
- Updated to release 3.21.

* Thu Mar 18 2004 Dag Wieers <dag@wieers.com> - 3.18-0
- Updated to release 3.18.

* Sun Aug 03 2003 Dag Wieers <dag@wieers.com> - 3.17-0
- Initial package. (using DAR)
