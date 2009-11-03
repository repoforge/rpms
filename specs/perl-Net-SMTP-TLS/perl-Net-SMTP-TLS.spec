# $Id$
# Authority: dag
# Upstream: Alexander Christian Westholm <awestholm$verizon,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-SMTP-TLS

Summary: SMTP client supporting TLS and AUTH
Name: perl-Net-SMTP-TLS
Version: 0.12
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-SMTP-TLS/

Source: http://www.cpan.org/modules/by-module/Net/Net-SMTP-TLS-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
SMTP client supporting TLS and AUTH.

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
%doc %{_mandir}/man3/Net::SMTP::TLS.3pm*
%dir %{perl_vendorlib}/Net/
%dir %{perl_vendorlib}/Net/SMTP/
#%{perl_vendorlib}/Net/SMTP/TLS/
%{perl_vendorlib}/Net/SMTP/TLS.pm

%changelog
* Wed Dec 17 2008 Dag Wieers <dag@wieers.com> - 0.12-1
- Initial package. (using DAR)
