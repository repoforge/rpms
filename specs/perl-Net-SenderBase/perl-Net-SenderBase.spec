# $Id: $
# Authority: dries
# Upstream: Matt Sergeant <msergeant$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-SenderBase

Summary: Query the senderbase service
Name: perl-Net-SenderBase
Version: 1.01
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-SenderBase/

Source: http://www.cpan.org/modules/by-module/Net/Net-SenderBase-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
Requires: perl

%description
This module allows you to query the SenderBase service via
either DNS or HTTP and get the results in a perl object.

%prep
%setup -n %{real_name}-%{version}

%build
echo | %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
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
%doc Changes MANIFEST MANIFEST.SKIP README
%doc %{_mandir}/man3/Net::SenderBase.3pm*
%doc %{_mandir}/man3/Net::SenderBase::*.3pm*
%dir %{perl_vendorlib}/Net/
%{perl_vendorlib}/Net/SenderBase/
%{perl_vendorlib}/Net/SenderBase.pm

%changelog
* Thu Jul 24 2008 Dries Verachtert <dries@ulyssis.org> - 1.01-1
- Initial package.
