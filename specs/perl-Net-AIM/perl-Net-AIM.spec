# $Id$
# Authority: dag
# Upstream: Aryeh Goldsmith <perlaim$aryeh,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-AIM

Summary: Perl module for AOL Instant Messenger TOC protocol
Name: perl-Net-AIM
Version: 1.22
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-AIM/

Source: http://www.cpan.org/modules/by-module/Net/Net-AIM-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Net-AIM is a Perl module for AOL Instant Messenger TOC protocol.

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
%doc MANIFEST README TODO
%doc %{_mandir}/man3/Net::AIM.3pm*
%doc %{_mandir}/man3/Net::AIM::Connection.3pm*
%doc %{_mandir}/man3/Net::AIM::Event.3pm*
%dir %{perl_vendorlib}/Net/
%{perl_vendorlib}/Net/AIM/
%{perl_vendorlib}/Net/AIM.pm

%changelog
* Sun Oct 07 2007 Dag Wieers <dag@wieers.com> - 1.22-1
- Initial package. (using DAR)
