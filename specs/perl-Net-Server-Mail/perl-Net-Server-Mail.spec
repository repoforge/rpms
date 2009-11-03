# $Id$
# Authority: cmr
# Upstream: Xavier Guimard <perl+cpan$astola,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-Server-Mail

Summary: Perl module named Net-Server-Mail
Name: perl-Net-Server-Mail
Version: 0.17
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-Server-Mail/
Obsoletes: perl-Net-Server-Mail-ESMTP-XFORWARD

Source: http://www.cpan.org/modules/by-module/Net/Net-Server-Mail-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Net-Server-Mail is a Perl module.

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
%doc Changes MANIFEST META.yml README eg/
%doc %{_mandir}/man3/Net::Server::Mail*.3pm*
%dir %{perl_vendorlib}/Net/
%dir %{perl_vendorlib}/Net/Server/
%{perl_vendorlib}/Net/Server/Mail/
%{perl_vendorlib}/Net/Server/Mail.pm

%changelog
* Sat Jul 04 2009 Unknown - 0.17-1
- Initial package. (using DAR)
