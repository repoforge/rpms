# $Id$
# Authority: dag
# Upstream: Daniel Podolsky <tpaba$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-Ifconfig-Wrapper

Summary: Perl module that provides a unified way to configure network interfaces
Name: perl-Net-Ifconfig-Wrapper
Version: 0.11
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-Ifconfig-Wrapper/

Source: http://www.cpan.org/modules/by-module/Net/Net-Ifconfig-Wrapper-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Net-Ifconfig-Wrapper is a Perl module that provides a unified way
to configure network interfaces on FreeBSD, OpenBSD, Solaris, Linux,
OS X, and WinNT (from Win2K). 

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
find contrib/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST README contrib/
%doc %{_mandir}/man3/Net::Ifconfig::Wrapper.3pm*
%dir %{perl_vendorlib}/Net/
%dir %{perl_vendorlib}/Net/Ifconfig/
%{perl_vendorlib}/Net/Ifconfig/Wrapper.pm

%changelog
* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 0.11-1
- Updated to version 0.11.

* Sun Oct 07 2007 Dag Wieers <dag@wieers.com> - 0.09-1
- Initial package. (using DAR)
