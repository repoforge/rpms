# $Id$
# Authority: dag
# Upstream: Graham Barr <gbarr$pobox,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-PH

Summary: Perl module that implements a CCSO Nameserver Client class
Name: perl-Net-PH
Version: 2.21
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-PH/

Source: http://www.cpan.org/modules/by-module/Net/Net-PH-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Net-PH is a Perl module that implements a CCSO Nameserver Client class.

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
%doc MANIFEST README
%doc %{_mandir}/man3/Net::PH.3pm*
%dir %{perl_vendorlib}/Net/
%{perl_vendorlib}/Net/PH.pm

%changelog
* Sun Oct 07 2007 Dag Wieers <dag@wieers.com> - 2.21-1
- Initial package. (using DAR)
