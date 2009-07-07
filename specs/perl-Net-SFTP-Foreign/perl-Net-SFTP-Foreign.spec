# $Id$
# Authority: dag
# Upstream: Salvador Fandiño García <salva$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-SFTP-Foreign

Summary: SSH File Transfer Protocol client
Name: perl-Net-SFTP-Foreign
Version: 1.53
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-SFTP-Foreign/

Source: http://www.cpan.org/modules/by-module/Net/Net-SFTP-Foreign-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
SSH File Transfer Protocol client.

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
find samples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes LICENSE MANIFEST META.yml README samples/
%doc %{_mandir}/man3/Net::SFTP::Foreign.3pm*
%doc %{_mandir}/man3/Net::SFTP::Foreign::*.3pm*
%dir %{perl_vendorlib}/Net/
%dir %{perl_vendorlib}/Net/SFTP/
%{perl_vendorlib}/Net/SFTP/Foreign/
%{perl_vendorlib}/Net/SFTP/Foreign.pm

%changelog
* Tue Jul  7 2009 Christoph Maser <cmr@financial.com> - 1.53-1
- Updated to version 1.53.

* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 1.51-1
- Updated to version 1.51.

* Sun Jun 22 2008 Dag Wieers <dag@wieers.com> - 1.38-1
- Initial package. (using DAR)
