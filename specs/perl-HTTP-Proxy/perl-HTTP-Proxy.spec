# $Id$
# Authority: dag
# Upstream: Philippe "BooK" Bruhat <book$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name HTTP-Proxy

Summary: Pure Perl HTTP proxy
Name: perl-HTTP-Proxy
Version: 0.22
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/HTTP-Proxy/

Source: http://www.cpan.org/modules/by-module/HTTP/HTTP-Proxy-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
HTTP-Proxy is a Perl module that implements a HTTP proxy.

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

### Clean up docs
find eg/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README eg/
%doc %{_mandir}/man3/HTTP::Proxy.3pm*
%doc %{_mandir}/man3/HTTP::Proxy::*.3pm*
%dir %{perl_vendorlib}/HTTP/
%{perl_vendorlib}/HTTP/Proxy/
%{perl_vendorlib}/HTTP/Proxy.pm

%changelog
* Mon May 05 2008 Dag Wieers <dag@wieers.com> - 0.22-1
- Updated to release 0.22.

* Wed May 02 2007 Dag Wieers <dag@wieers.com> - 0.20-1
- Initial package. (using DAR)
