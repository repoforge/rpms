# $Id$
# Authority: dag
# Upstream: Vlad Manilici <vman$tmok,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-Libdnet

Summary: Perl module that implements an interface to libdnet
Name: perl-Net-Libdnet
Version: 0.01
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-Libdnet/

Source: http://www.cpan.org/modules/by-module/Net/Net-Libdnet-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

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
%doc %{_mandir}/man3/Net::Libdnet.3pm*
%dir %{perl_vendorarch}/Net/
%{perl_vendorarch}/Net/Libdnet.pm
%dir %{perl_vendorarch}/auto/Net/
%{perl_vendorarch}/auto/Net/Libdnet/

%changelog
* Sat Aug 04 2007 Dag Wieers <dag@wieers.com> - 0.01-1
- Initial package. (using DAR)
