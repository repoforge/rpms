# $Id$
# Authority: dries
# Upstream: Marco Carnut <kiko$tempest,com,br>

%{?dist: %{expand: %%define %dist 1}}

%{!?dist:%define _with_libpcapdevel 1}
%{?el5:%define _with_libpcapdevel 1}
%{?fc6:%define _with_libpcapdevel 1}

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-Pcap

Summary: Interface to pcap(3) LBL packet capture library
Name: perl-Net-Pcap
Version: 0.12
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-Pcap/

Source: http://search.cpan.org/CPAN/authors/id/S/SA/SAPER/Net-Pcap-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, libpcap, perl(ExtUtils::MakeMaker)
%{?_with_libpcapdevel:BuildRequires:libpcap-devel}

%description
This module is an interface to pcap(3) LBL packet capture library.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} \
		%{buildroot}%{perl_vendorarch}/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%doc %{_mandir}/man1/pcapinfo*.1*
%doc %{_mandir}/man3/*.3pm*
%{_bindir}/pcapinfo
%dir %{perl_vendorarch}/Net/
%{perl_vendorarch}/Net/Pcap.pm
%dir %{perl_vendorarch}/auto/Net/
%{perl_vendorarch}/auto/Net/Pcap/

%changelog
* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.12-1
- Updated to release 0.12.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 0.11-1
- Updated to release 0.11.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 0.10-1
- Updated to release 0.10.

* Fri Dec 10 2004 Dries Verachtert <dries@ulyssis.org> - 0.05-1
- Initial package.
