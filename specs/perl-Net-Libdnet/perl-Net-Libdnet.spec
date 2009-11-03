# $Id$
# Authority: dag
# Upstream: Vlad Manilici <vman$tmok,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-Libdnet

Summary: Perl module that implements an interface to libdnet
Name: perl-Net-Libdnet
Version: 0.92
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-Libdnet/

Source: http://www.cpan.org/modules/by-module/Net/Net-Libdnet-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: libdnet-devel
Requires: libdnet

%description
perl-Net-Libdnet is a Perl module that implements an interface to libdnet.

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

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes LICENSE MANIFEST README
%doc %{_mandir}/man3/Net::Libdnet*.3pm*
%dir %{perl_vendorarch}/Net/
%{perl_vendorarch}/Net/Libdnet.pm
%dir %{perl_vendorarch}/Net/
%{perl_vendorarch}/Net/Libdnet/
%{perl_vendorarch}/auto/Net/Libdnet/Libdnet.bs
%{perl_vendorarch}/auto/Net/Libdnet/Libdnet.so
%{_bindir}/dnet.pl

%changelog
* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 0.92-1
- Updated to version 0.92.

* Sat Aug 04 2007 Dag Wieers <dag@wieers.com> - 0.01-1
- Initial package. (using DAR)
