# $Id$
# Authority: dag
# Upstream: Patrick Collins <pcollins$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name HTTP-DAV

Summary: WebDAV client library for Perl
Name: perl-HTTP-DAV
Version: 0.42
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/HTTP-DAV/

Source: http://search.cpan.org/CPAN/authors/id/O/OP/OPERA/HTTP-DAV-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(LWP) >= 5.48
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(XML::DOM)
BuildRequires: perl(XML::Parser)
Requires: perl(LWP) >= 5.48
Requires: perl(Scalar::Util)
Requires: perl(XML::DOM)

%filter_from_requires /^perl*/d
%filter_setup

%description
HTTP::DAV is a Perl API for interacting with and modifying content
on webservers using the WebDAV protocol. Now you can LOCK, DELETE
and PUT files and much more on a DAV-enabled webserver.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}
%{__make} %{?_smp_mflags} test

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

### Clean up docs
find doc/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README TODO doc/
%doc %{_mandir}/man1/dave.1*
%doc %{_mandir}/man3/HTTP::DAV.3pm*
%doc %{_mandir}/man3/HTTP::DAV::*.3pm*
%dir %{perl_vendorlib}/HTTP/
%{_bindir}/dave
%{perl_vendorlib}/HTTP/DAV/
%{perl_vendorlib}/HTTP/DAV.pm

%changelog
* Tue Apr 05 2011 Denis Fateyev <denis@fateyev.com> - 0.42-1
- Updated to version 0.42.

* Wed Feb  3 2010 Christoph Maser <cmr@financial.com> - 0.40-1
- Updated to version 0.40.

* Wed Dec 30 2009 Christoph Maser <cmr@financial.com> - 0.39-1
- Updated to version 0.39.

* Sun Jul  5 2009 Christoph Maser <cmr@financial.com> - 0.38-1
- Updated to version 0.38.

* Sun Nov 09 2008 Dag Wieers <dag@wieers.com> - 0.35-1
- Updated to release 0.35.

* Wed Oct 08 2008 Dag Wieers <dag@wieers.com> - 0.34-1
- Updated to release 0.34.

* Sat Feb 12 2005 Dag Wieers <dag@wieers.com> - 0.31-1
- Initial package. (using DAR)
