# $Id$
# Authority: dries
# Upstream: Chris Dawson <cdawson$webiphany,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Podcast-Publisher

Summary: Manages RSS files and podcasts
Name: perl-Podcast-Publisher
Version: 0.51
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Podcast-Publisher/

Source: http://www.cpan.org/authors/id/C/CD/CDAWSON/Podcast-Publisher-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
With this module, you can manage rss feeds and podcasts.

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
%doc README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Podcast/

%changelog
* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 0.51-1
- Updated to release 0.51.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.50-1
- Updated to release 0.50.

* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 0.45-1
- Updated to release 0.45.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.44-1.2
- Rebuild for Fedora Core 5.

* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.44-1
- Initial package.
