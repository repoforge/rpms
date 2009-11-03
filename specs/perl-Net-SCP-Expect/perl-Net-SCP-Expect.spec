# $Id$
# Authority: dag
# Upstream: Daniel Berger <djberg96$hotmail,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-SCP-Expect

Summary: Perl module to wrap scp to allow passwords via Expect
Name: perl-Net-SCP-Expect
Version: 0.16
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-SCP-Expect/

Source: http://www.cpan.org/modules/by-module/Net/Net-SCP-Expect-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Net-SCP-Expect is a Perl module to wrap scp to allow passwords via Expect.

This package contains the following Perl module:

    Net::SCP::Expect

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
%doc CHANGES MANIFEST README
%doc %{_mandir}/man3/Net::SCP::Expect.3pm*
%dir %{perl_vendorlib}/Net/
%dir %{perl_vendorlib}/Net/SCP/
%{perl_vendorlib}/Net/SCP/Expect.pm

%changelog
* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 0.16-1
- Updated to version 0.16.

* Sat Nov 03 2007 Dag Wieers <dag@wieers.com> - 0.12-1
- Initial package. (using DAR)
