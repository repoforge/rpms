# $Id$
# Authority: dag
# Upstream: Hajimu Umemoto <ume$mahoroba,org>

### EL6 ships with perl-Socket6-0.23-3.el6
%{?el6:# Tag: rfx}
### EL5 ships with perl-Socket6-0.19-3.fc6
%{?el5:# Tag: rfx}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Socket6

Summary: IPv6 related part of the C socket.h defines and structure manipulators
Name: perl-Socket6
Version: 0.23
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Socket6/

Source: http://www.cpan.org/modules/by-module/Socket6/Socket6-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl >= 0:5.00503
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl >= 0:5.00503

%description
This perl module supports getaddrinfo() and getnameinfo() to intend to
enable protocol independent programing.
If your environment supports IPv6, IPv6 related defines such as
AF_INET6 are included.


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
%doc ChangeLog MANIFEST META.yml README
#%doc %{_mandir}/man3/Socket6.3pm*
%{perl_vendorarch}/auto/Socket6/
%{perl_vendorarch}/Socket6.pm

%changelog
* Thu Jun 18 2009 Christoph Maser <cmr@financial.com> - 0.23-1
- Updated to version 0.23.

* Thu Feb 21 2008 Dag Wieers <dag@wieers.com> - 0.20-1
- Updated to release 0.20.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 0.19-1
- Updated to release 0.19.

* Wed Mar 30 2005 Dag Wieers <dag@wieers.com> - 0.18-1
- Initial package. (using DAR)
