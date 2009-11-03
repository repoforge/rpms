# $Id$
# Authority: dries
# Upstream: Damian Conway <damian$conway,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Perl6-Export

Summary: Implements the Perl 6 is export trait
Name: perl-Perl6-Export
Version: 0.07
Release: 2%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Perl6-Export/

Source: http://www.cpan.org/modules/by-module/Perl6/Perl6-Export-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This module prototypes the Perl 6 'exported' and 'exportable' traits
in Perl 5.

Instead of messing around with @EXPORT arrays, you just declare which subs
are to be exported (or are exportable on request) as part of those subs.

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
%doc Changes README
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/Perl6/
%{perl_vendorlib}/Perl6/Export.pm

%changelog
* Thu Feb 21 2008 Dries Verachtert <dries@ulyssis.org> - 0.07-2
- Fixed the description, thanks to Bill McGonigle.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.07-1.2
- Rebuild for Fedora Core 5.

* Tue Dec 07 2004 Dries Verachtert <dries@ulyssis.org> - 0.07-1
- Initial package.
