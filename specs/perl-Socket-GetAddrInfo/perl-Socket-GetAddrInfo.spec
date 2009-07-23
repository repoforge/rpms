# $Id$
# Authority: cmr
# Upstream: Paul Evans E<lt>leonerd$leonerd,org,ukE<gt>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Socket-GetAddrInfo

Summary: RFC 2553's C<getaddrinfo> and C<getnameinfo> functions
Name: perl-Socket-GetAddrInfo
Version: 0.11
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Socket-GetAddrInfo/

Source: http://www.cpan.org/modules/by-module/Socket/Socket-GetAddrInfo-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::CBuilder)
BuildRequires: perl(Module::Build)
BuildRequires: perl(Module::Build::Compat)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::More)

%description
RFC 2553's C<getaddrinfo> and C<getnameinfo> functions.

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
%doc Changes MANIFEST META.yml
%doc %{_mandir}/man3/Socket::GetAddrInfo.3pm*
%dir %{perl_vendorarch}/auto/Socket/
%{perl_vendorarch}/auto/Socket/GetAddrInfo/
%dir %{perl_vendorarch}/Socket/
%{perl_vendorarch}/Socket/GetAddrInfo.pm

%changelog
* Thu Jul 23 2009 Christoph Maser <cmr@financial.com> - 0.11-1
- Initial package. (using DAR)
