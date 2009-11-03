# $Id$
# Authority: dries
# Upstream: Gábor Szabó <gabor$pti,co,il>

%{?dtag: %{expand: %%define %dtag 1}}

%{!?dtag:%define _with_libpcapdevel 1}
%{?el5:%define _with_libpcapdevel 1}
%{?fc6:%define _with_libpcapdevel 1}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-RawIP

Summary: Manipulate raw ip packets with interface to libpcap
Name: perl-Net-RawIP
Version: 0.25
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-RawIP/

Source: http://www.cpan.org/modules/by-module/Net/Net-RawIP-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: libpcap
BuildRequires: perl(ExtUtils::MakeMaker)
%{?_with_libpcapdevel:BuildRequires:libpcap-devel}

%description
This is Net::RawIP, a perl module can to manipulate raw IP packets,
with an optional feature for manipulating Ethernet headers.

%prep
%setup -n %{real_name}-%{version}
%{__perl} -pi.orig -e 's|/lib\b|/%{_lib}|g' Makefile.PL

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} OPTIMIZE="%{optflags}"
#%{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST MANIFEST.SKIP META.yml README README.Devel TODO examples/
%doc %{_mandir}/man3/Net::RawIP.3pm*
%doc %{_mandir}/man3/Net::RawIP::libpcap.3pm*
%dir %{perl_vendorarch}/auto/Net/
%{perl_vendorarch}/auto/Net/RawIP/
%dir %{perl_vendorarch}/Net/
%{perl_vendorarch}/Net/RawIP/
%{perl_vendorarch}/Net/RawIP.pm

%changelog
* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 0.25-1
- Updated to version 0.25.

* Wed Jan 23 2008 Dag Wieers <dag@wieers.com> - 0.23-1
- Updated to release 0.23.

* Thu Nov 15 2007 Dag Wieers <dag@wieers.com> - 0.21-1
- Updated to release 0.21.

* Thu Aug 24 2006 Dries Verachtert <dries@ulyssis.org> - 0.2-2
- Gcc fixes: patch added.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.2-1
- Initial package.
