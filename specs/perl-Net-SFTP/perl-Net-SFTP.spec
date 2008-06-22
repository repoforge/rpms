# $Id$
# Authority: dag
# Upstream: David Robins <dbrobins$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-SFTP

Summary: Secure File Transfer Protocol client
Name: perl-Net-SFTP
Version: 0.10
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-SFTP/

Source: http://www.cpan.org/modules/by-module/Net/Net-SFTP-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Secure File Transfer Protocol client.

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
find eg/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes LICENSE MANIFEST MANIFEST.SKIP META.yml README ToDo eg/
%doc %{_mandir}/man3/Net::SFTP.3pm*
%doc %{_mandir}/man3/Net::SFTP::*.3pm*
%dir %{perl_vendorlib}/Net/
%{perl_vendorlib}/Net/SFTP/
%{perl_vendorlib}/Net/SFTP.pm

%changelog
* Sun Jun 22 2008 Dag Wieers <dag@wieers.com> - 0.10-1
- Initial package. (using DAR)
