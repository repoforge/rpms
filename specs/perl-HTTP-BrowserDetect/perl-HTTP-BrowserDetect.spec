# $Id$
# Authority: dries
# Upstream: Lee Semel <lee$semel,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name HTTP-BrowserDetect

Summary: Determine the Web browser, version, and platform
Name: perl-HTTP-BrowserDetect
Version: 1.22
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/HTTP-BrowserDetect/

Source: http://search.cpan.org/CPAN/authors/id/O/OA/OALDERS/HTTP-BrowserDetect-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Data::Dump)
BuildRequires: perl(Exporter)
BuildRequires: perl(FindBin)
BuildRequires: perl(Test::More)
BuildRequires: perl(YAML::Tiny)

%filter_from_requires /^perl*/d
%filter_setup


%description
The HTTP::BrowserDetect object does a number of tests on an HTTP user
agent string. The results of these tests are available via methods of
the object.

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
%{perl_vendorlib}/HTTP/BrowserDetect.pm

%changelog
* Tue Apr 05 2011 Denis Fateyev <denis@fateyev.com> - 1.22-1
- Updated to version 1.22.

* Wed Dec 30 2009 Christoph Maser <cmr@financial.com> - 1.06-1
- Updated to version 1.06.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.99-1
- Updated to release 0.99.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.98-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.98-1
- Initial package.
