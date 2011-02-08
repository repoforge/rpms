# $Id$
# Authority: dries
# Upstream: Elizabeth Mattijsen <liz@dijkmat.nl>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Text-vFile-asData

Summary: Parse vFile formatted files into data structures
Name: perl-Text-vFile-asData
Version: 0.07
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Text-vFile-asData/

Source: http://search.cpan.org/CPAN/authors/id/R/RC/RCLAMP/Text-vFile-asData-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl(Class::Accessor::Chained)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More) 
Requires: perl(Class::Accessor::Chained)
Requires: perl(Test::More)

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
With this package you can parse vFile formatted files into data structures.

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
%doc Changes
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Text/vFile/asData.pm

%changelog
* Tue Feb  8 2011 Christoph Maser <cmaser@gmx.de> - 0.07-1
- Updated to version 0.07.

* Tue Feb  8 2011 Christoph Maser <cmaser@gmx.de> - 0.19-1
- Updated to version 0.19.

* Wed Jun 11 2008 Dries Verachtert <dries@ulyssis.org> - 0.05-2
- Added Class::Accessor::Chained requirement, thanks to Sven Sternberger.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.05-1.2
- Rebuild for Fedora Core 5.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 0.05-1
- Updated to release 0.05.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 0.04-1
- Updated to release 0.04.

* Wed Mar  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.02-1
- Initial package.
