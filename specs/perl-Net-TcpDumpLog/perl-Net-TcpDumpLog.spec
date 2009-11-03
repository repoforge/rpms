# $Id$
# Authority: dag
# Upstream: Brendan Gregg <brendan,gregg$tpg,com,au>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-TcpDumpLog

Summary: Perl module to read tcpdump/libpcap network packet logs
Name: perl-Net-TcpDumpLog
Version: 0.11
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-TcpDumpLog/

Source: http://www.cpan.org/modules/by-module/Net/Net-TcpDumpLog-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Net-TcpDumpLog is a Perl module to read tcpdump/libpcap network
packet logs.

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
%doc Changes MANIFEST README
%doc %{_mandir}/man3/Net::TcpDumpLog.3pm*
%dir %{perl_vendorlib}/Net/
%{perl_vendorlib}/Net/TcpDumpLog.pm

%changelog
* Sun Oct 07 2007 Dag Wieers <dag@wieers.com> - 0.11-1
- Initial package. (using DAR)
