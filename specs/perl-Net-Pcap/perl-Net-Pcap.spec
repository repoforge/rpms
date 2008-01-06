# $Id$
# Authority: dries
# Upstream: Sébastien Aperghis-Tramoni <sebastien$aperghis,net>

%{?dtag: %{expand: %%define %dtag 1}}

%{!?dtag:%define _with_libpcapdevel 1}
%{?el5:%define _with_libpcapdevel 1}
%{?fc6:%define _with_libpcapdevel 1}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-Pcap

Summary: Interface to pcap(3) LBL packet capture library
Name: perl-Net-Pcap
Version: 0.16
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-Pcap/

Source: http://www.cpan.org/modules/by-module/Net/Net-Pcap-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: libpcap
BuildRequires: perl(ExtUtils::MakeMaker)
%{?_with_libpcapdevel:BuildRequires:libpcap-devel}

%description
Interface to pcap(3) LBL packet capture library.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

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
%doc %{_mandir}/man1/pcapinfo.1*
%doc %{_mandir}/man3/Net::Pcap.3pm*
%{_bindir}/pcapinfo
%dir %{perl_vendorarch}/auto/Net/
%{perl_vendorarch}/auto/Net/Pcap/
%dir %{perl_vendorarch}/Net/
%{perl_vendorarch}/Net/Pcap.pm

%changelog
* Fri Jan 04 2008 Dag Wieers <dag@wieers.com> - 0.16-1
- Updated to release 0.16.

* Tue Dec 04 2007 Dag Wieers <dag@wieers.com> - 0.15-1
- Updated to release 0.15.

* Thu Nov 15 2007 Dag Wieers <dag@wieers.com> - 0.14-1
- Updated to release 0.14.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.12-1
- Updated to release 0.12.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 0.11-1
- Updated to release 0.11.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 0.10-1
- Updated to release 0.10.

* Fri Dec 10 2004 Dries Verachtert <dries@ulyssis.org> - 0.05-1
- Initial package.
