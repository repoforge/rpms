# $Id$
# Authority: dag
# Upstream: Giovanni S Marzot <marz$users,sourceforge,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name TFTP
%define real_version 1.0b3

Summary: Perl module that implements a TFTP Client class
Name: perl-TFTP
Version: 1.0
Release: 0.b3%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/TFTP/

Source: http://www.cpan.org/modules/by-module/TFTP/TFTP-%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-TFTP is a Perl module that implements a TFTP Client class.

%prep
%setup -n %{real_name}-%{real_version}

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
%doc %{_mandir}/man3/TFTP.3pm*
%{perl_vendorlib}/TFTP.pm

%changelog
* Sun Oct 07 2007 Dag Wieers <dag@wieers.com> - 1.0-0.b3
- Initial package. (using DAR)
