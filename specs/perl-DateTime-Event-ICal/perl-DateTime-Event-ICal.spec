# $Id$
# Authority: dries
# Upstream: Flávio Soibelmann Glock <fglock$pucrs,br>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name DateTime-Event-ICal

Summary: Perl DateTime extension for computing rfc2445 recurrences
Name: perl-DateTime-Event-ICal
Version: 0.10
Release: 1%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DateTime-Event-ICal/

Source: http://search.cpan.org/CPAN/authors/id/F/FG/FGLOCK/DateTime-Event-ICal-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(DateTime)
BuildRequires: perl(DateTime::Event::Recurrence) >= 0.11
Requires: perl(DateTime)
Requires: perl(DateTime::Event::Recurrence) >= 0.11

%filter_from_requires /^perl*/d
%filter_setup


%description
Perl DateTime extension for computing rfc2445 recurrences like
'last friday of march'.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/DateTime/Event/ICal.pm

%changelog
* Thu Dec 31 2009 Christoph Maser <cmr@financial.com> - 0.10-1
- Updated to version 0.10.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.09-1.2
- Rebuild for Fedora Core 5.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 0.09-1
- Updated to release 0.09.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 0.08-1
- Initial package.
