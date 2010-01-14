# $Id$
# Authority: dries
# Upstream: Florian Ragwitz <rafl@debian.org>


%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name HTTP-Request-AsCGI

Summary: Setup a CGI enviroment from a HTTP::Request
Name: perl-HTTP-Request-AsCGI
Version: 1.2
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/HTTP-Request-AsCGI/

Source: http://search.cpan.org/CPAN/authors/id/F/FL/FLORA/HTTP-Request-AsCGI-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Carp)
BuildRequires: perl(Class::Accessor)
BuildRequires: perl(HTTP::Request)
BuildRequires: perl(HTTP::Response) >= 1.53
BuildRequires: perl(IO::File)
BuildRequires: perl(Test::More)
BuildRequires: perl(URI::Escape)
Requires: perl(Carp)
Requires: perl(Class::Accessor)
Requires: perl(HTTP::Request)
Requires: perl(HTTP::Response) >= 1.53
Requires: perl(IO::File)
Requires: perl(Test::More)
Requires: perl(URI::Escape)

%filter_from_requires /^perl*/d
%filter_setup


%description
Provides a convinient way of setting up an CGI enviroment from a HTTP::Request.

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
%{perl_vendorlib}/HTTP/Request/AsCGI.pm

%changelog
* Thu Jan 14 2010 Christoph Maser <cmr@financial.com> - 1.2-1
- Updated to version 1.2.

* Wed Dec 30 2009 Christoph Maser <cmr@financial.com> - 1.0-1
- Updated to version 1.0.

* Sun Jul  5 2009 Christoph Maser <cmr@financial.com> - 0.9-1
- Updated to version 0.9.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.5-1
- Updated to release 0.5.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.3-1.2
- Rebuild for Fedora Core 5.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 0.3-1
- Updated to release 0.3.

* Thu Dec 15 2005 Dries Verachtert <dries@ulyssis.org> - 0.2-1
- Initial package.
