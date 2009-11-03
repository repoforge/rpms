# $Id$
# Authority: dries
# Upstream: Graham Barr <gbarr$pobox,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-TFTP

Summary: TFTP Client class
Name: perl-Net-TFTP
Version: 0.17
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-TFTP/

Source: http://www.cpan.org/modules/by-module/Net/Net-TFTP-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Net::TFTP was previously part of the libnet distribution. But has now
been separated out to a distribution of its own.

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
%doc ChangeLog MANIFEST META.yml README
%doc %{_mandir}/man3/Net::TFTP.3pm*
%dir %{perl_vendorlib}/Net/
#%{perl_vendorlib}/Net/TFTP/
%{perl_vendorlib}/Net/TFTP.pm

%changelog
* Thu Nov 15 2007 Dag Wieers <dag@wieers.com> - 0.17-1
- Updated to release 0.17.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.16-1
- Initial package.
