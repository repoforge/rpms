# $Id$
# Authority: dag
# Upstream: Jason Kohles <cpan$jasonkohles,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name WWW-Google-SiteMap

Summary: Perl module to create sitemaps
Name: perl-WWW-Google-SiteMap
Version: 1.09
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/WWW-Google-SiteMap/

Source: http://www.cpan.org/modules/by-module/WWW/WWW-Google-SiteMap-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)
BuildRequires: perl(XML::Twig), perl(URI::Escape)

%description
perl-WWW-Google-SiteMap is a Perl module to create sitemaps.

This package contains the following Perl modules:

    WWW::Google::SiteMap
    WWW::Google::SiteMap::Index
    WWW::Google::SiteMap::Ping
    WWW::Google::SiteMap::Robot
    WWW::Google::SiteMap::URL

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
%doc Changes MANIFEST MANIFEST.SKIP META.yml README
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/WWW/
%dir %{perl_vendorlib}/WWW/Google/
%{perl_vendorlib}/WWW/Google/SiteMap/
%{perl_vendorlib}/WWW/Google/SiteMap.pm

%changelog
* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 1.09-1
- Updated to release 1.09.

* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 1.08-1
- Updated to release 1.08.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 1.07-1
- Updated to release 1.07.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 1.04-1
- Updated to release 1.04.

* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.03-1
- Initial package.
