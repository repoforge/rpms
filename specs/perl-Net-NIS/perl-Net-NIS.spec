# $Id$
# Authority: dag
# Upstream: Eduardo Santiago Muñoz <pause$edsantiago,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-NIS

Summary: Interface to Sun's Network Information Service
Name: perl-Net-NIS
Version: 0.34
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-NIS/

Source: http://www.cpan.org/modules/by-module/Net/Net-NIS-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
Interface to Sun's Network Information Service.

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
%doc MANIFEST README
%doc %{_mandir}/man3/Net::NIS.3pm*
%doc %{_mandir}/man3/Net::NISTable.3pm*
%dir %{perl_vendorarch}/auto/Net/
%{perl_vendorarch}/auto/Net/NIS/
%dir %{perl_vendorarch}/Net/
%{perl_vendorarch}/Net/NIS/
%{perl_vendorarch}/Net/NIS.pm
%{perl_vendorarch}/Net/NIS.pod
%{perl_vendorarch}/Net/NISTable.pod

%changelog
* Sun Jun 22 2008 Dag Wieers <dag@wieers.com> - 0.34-1
- Initial package. (using DAR)
