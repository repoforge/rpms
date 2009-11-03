# $Id$
# Authority: dag
# Upstream: Matt Sergeant <msergeant$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name HTTP-GHTTP

Summary: Perl interface to the gnome ghttp library
Name: perl-HTTP-GHTTP
Version: 1.07
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/HTTP-GHTTP/

Source: http://www.cpan.org/modules/by-module/HTTP/HTTP-GHTTP-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libghttp-devel
BuildRequires: perl

%description
Perl interface to the gnome ghttp library.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST README
%doc %{_mandir}/man3/HTTP::GHTTP.3pm*
%{_bindir}/g-request
%dir %{perl_vendorarch}/auto/HTTP/
%{perl_vendorarch}/auto/HTTP/GHTTP/
%dir %{perl_vendorarch}/HTTP/
%{perl_vendorarch}/HTTP/GHTTP.pm

%changelog
* Mon Jun 23 2008 Dag Wieers <dag@wieers.com> - 1.07-1
- Initial package. (using DAR)
