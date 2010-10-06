# $Id$
# Authority: dag
# Upstream: Shlomi Fish <shlomif$iglu,org,il>
# RFX: el5

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name IO-Socket-INET6

Summary: Object interface for AF_INET|AF_INET6 domain sockets
Name: perl-IO-Socket-INET6
Version: 2.57
Release: 2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/IO-Socket-INET6/

Source: http://search.cpan.org/CPAN/authors/id/S/SH/SHLOMIF/IO-Socket-INET6-2.57.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(IO::Socket)
BuildRequires: perl(Socket6) >= 0.12
BuildRequires: perl(Test::More)
Requires: perl(IO::Socket)
Requires: perl(Socket6) >= 0.12

%filter_from_requires /^perl*/d
%filter_setup

%description
IO::Socket::INET6 provides an object interface to creating and using sockets
in both AF_INET|AF_INET6 domain. It is built upon the IO::Socket interface and
inherits all the methods defined by IO::Socket.

%prep
%setup -q -n %{real_name}-%{version}

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
%doc ChangeLog MANIFEST META.yml README
%doc %{_mandir}/man3/IO::Socket::INET6.3pm*
%dir %{perl_vendorlib}/IO/
%dir %{perl_vendorlib}/IO/Socket/
%{perl_vendorlib}/IO/Socket/INET6.pm

%changelog
* Wed Oct 06 2010 David Hrbáč <david@hrbac.cz> - 2.57-2
- RFXed for el5

* Wed Dec 23 2009 Christoph Maser <cmr@financial.com> - 2.57-1
- Updated to version 2.57.

* Mon Oct 13 2008 Dag Wieers <dag@wieers.com> - 2.56-1
- Updated to release 2.56.

* Wed Oct 08 2008 Dag Wieers <dag@wieers.com> - 2.55-1
- Updated to release 2.55.

* Mon Feb 25 2008 Dag Wieers <dag@wieers.com> - 2.54-1
- Updated to release 2.54.

* Wed Feb 20 2008 Dag Wieers <dag@wieers.com> - 2.52-1
- Updated to release 2.52.

* Wed Mar 30 2005 Dag Wieers <dag@wieers.com> - 2.51-1
- Initial package. (using DAR)
