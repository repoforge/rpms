# $Id$
# Authority: dries
# Upstream: Chris Williams <chris@bingosnet.co.uk>

### EL6 ships with perl-Term-UI-0.20-115.el6
%{?el6:# Tag: rfx}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Term-UI

Summary: Term::ReadLine UI made easy
Name: perl-Term-UI
Version: 0.26
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Term-UI/

Source: http://search.cpan.org/CPAN/authors/id/B/BI/BINGOS/Term-UI-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Locale::Maketext::Simple)
BuildRequires: perl(Log::Message::Simple)
BuildRequires: perl(Params::Check)
BuildRequires: perl(Term::ReadLine)
BuildRequires: perl(Test::More)
Requires: perl(Locale::Maketext::Simple)
Requires: perl(Log::Message::Simple)
Requires: perl(Params::Check)
Requires: perl(Term::ReadLine)
Requires: perl(Test::More)

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
Term::UI provides methods to ask both elaborate questions as well
as simple yes/no questions via a Term::ReadLine interface using a
template. It can also parse options per unix style.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}
%{__make} test

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES MANIFEST META.yml README
%doc %{_mandir}/man3/Term::UI.3pm*
%doc %{_mandir}/man3/Term::UI::History.3pm*
%dir %{perl_vendorlib}/Term/
%{perl_vendorlib}/Term/UI/
%{perl_vendorlib}/Term/UI.pm

%changelog
* Thu Feb 10 2011 Christoph Maser <cmaser@gmx.de> - 0.26-1
- Updated to version 0.26.

* Tue Feb  8 2011 Christoph Maser <cmaser@gmx.de> - 0.24-1
- Updated to version 0.24.

* Fri Jun 12 2009 Christoph Maser <cmr@financial.com> - 0.20-1
- Updated to version 0.20.

* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 0.18-1
- Updated to release 0.18.

* Tue Nov 14 2006 Dries Verachtert <dries@ulyssis.org> - 0.14-1
- Updated to release 0.14.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 0.12-1
- Updated to release 0.12.

* Thu Mar 31 2005 Dries Verachtert <dries@ulyssis.org> - 0.05-1
- Initial package.
