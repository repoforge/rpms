# $Id$
# Authority: dag
# Upstream: Casey West <casey$geeknest,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name HTTP-Request-Params

Summary: HTTP-Request-Params module for perl
Name: perl-HTTP-Request-Params
Version: 1.01
Release: 1%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/HTTP-Request-Params/

Source: http://www.cpan.org/modules/by-module/HTTP/HTTP-Request-Params-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
HTTP-Request-Params module for perl.

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/HTTP::Request::Params.3pm*
#%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/HTTP/
%dir %{perl_vendorlib}/HTTP/Request/
#%{perl_vendorlib}/HTTP/Request/Params/
%{perl_vendorlib}/HTTP/Request/Params.pm

%changelog
* Wed May 02 2007 Dag Wieers <dag@wieers.com> - 1.01-1
- Initial package. (using DAR)
