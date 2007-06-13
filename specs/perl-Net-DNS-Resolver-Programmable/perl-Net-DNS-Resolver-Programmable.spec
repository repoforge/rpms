# $Id$
# Authority: dag
# Upstream: Julian Mehnle <julian$mehnle,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-DNS-Resolver-Programmable
%define real_version 0.002002

Summary: Perl module that implements a programmable DNS resolver class for offline emulation of DNS
Name: perl-Net-DNS-Resolver-Programmable
Version: 0.002.2
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-DNS-Resolver-Programmable/

Source: http://www.cpan.org/modules/by-module/Net/Net-DNS-Resolver-Programmable-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
Net-DNS-Resolver-Programmable is a Perl module that implements
a programmable DNS resolver class for offline emulation of DNS.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES INSTALL MANIFEST META.yml README SIGNATURE TODO
%doc %{_mandir}/man3/Net::DNS::Resolver::Programmable.3pm*
%dir %{perl_vendorlib}/Net/
%dir %{perl_vendorlib}/Net/DNS/
%dir %{perl_vendorlib}/Net/DNS/Resolver/
%{perl_vendorlib}/Net/DNS/Resolver/Programmable.pm

%changelog
* Wed May 02 2007 Dag Wieers <dag@wieers.com> - 0.002.2-1
- Initial package. (using DAR)
