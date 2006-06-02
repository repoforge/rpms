# $Id$
# Authority: dries
# Upstream: Jason Kohles <cpan$jasonkohles,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name WWW-Google-SiteMap

Summary: Create sitemaps
Name: perl-WWW-Google-SiteMap
Version: 1.08
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/WWW-Google-SiteMap/

Source: http://search.cpan.org/CPAN/authors/id/J/JA/JASONK/WWW-Google-SiteMap-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
The Sitemap Protocol allows you to inform search engine crawlers about
URLs on your Web sites that are available for crawling. A Sitemap con-
sists of a list of URLs and may also contain additional information
about those URLs, such as when they were last modified, how frequently
they change, etc.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/WWW/Google/SiteMap.pm
%{perl_vendorlib}/WWW/Google/SiteMap/

%changelog
* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 1.08-1
- Updated to release 1.08.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 1.07-1
- Updated to release 1.07.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.04-1.2
- Rebuild for Fedora Core 5.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 1.04-1
- Updated to release 1.04.

* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.03-1
- Initial package.
