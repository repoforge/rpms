# $Id$
# Authority: dag
# Upstream: Roy Hooper <help$thetoybox,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name HTTP-Lite
%define real_version 2.001006

Summary: Perl module that implements a lightweight HTTP implementation
Name: perl-HTTP-Lite
Version: 2.1.6
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/HTTP-Lite/

Source: http://www.cpan.org/modules/by-module/HTTP/HTTP-Lite-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-HTTP-Lite is a Perl module that implements a lightweight
HTTP implementation.

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
%doc Changes MANIFEST
%doc %{_mandir}/man3/HTTP::Lite.3pm*
%dir %{perl_vendorlib}/HTTP/
%{perl_vendorlib}/HTTP/Lite.pm

%changelog
* Sun Oct 07 2007 Dag Wieers <dag@wieers.com> - 2.1.6-1
- Initial package. (using DAR)
