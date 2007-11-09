# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name HTTP-DAV

Summary: WebDAV client library for Perl
Name: perl-HTTP-DAV
Version: 0.31
Release: 1.2
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/HTTP-DAV/

Source: http://www.cpan.org/modules/by-module/HTTP/HTTP-DAV-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl-libwww-perl
BuildRequires: perl-libxml-enno
Requires: perl, perl-libwww-perl

%description
HTTP::DAV is a Perl API for interacting with and modifying content
on webservers using the WebDAV protocol. Now you can LOCK, DELETE
and PUT files and much more on a DAV-enabled webserver.

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
%doc Changes MANIFEST README TODO
%doc %{_mandir}/man?/*
%{_bindir}/dave
%{perl_vendorlib}/HTTP/DAV/
%{perl_vendorlib}/HTTP/DAV.pm

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.31-1.2
- Rebuild for Fedora Core 5.

* Sat Feb 12 2005 Dag Wieers <dag@wieers.com> -
- Initial package. (using DAR)
