# $Id$
# Authority: dries
# Upstream: Jochen Wiedmann <jwied$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name PlRPC

Summary: Perl extension for writing PlRPC servers and clients
Name: perl-PlRPC
Version: 0.2020
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/PlRPC/

Source: http://www.cpan.org/modules/by-module/RPC/PlRPC-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
PlRPC (Perl RPC) is a package for implementing servers and clients that
are written in Perl entirely. The name is borrowed from Sun's RPC
(Remote Procedure Call), but it could as well be RMI like Java's "Remote
Method Interface), because PlRPC gives you the complete power of Perl's
OO framework in a very simple manner.

%prep
%setup -n %{real_name}

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
%doc %{_mandir}/man3/Bundle::PlRPC.3pm*
%doc %{_mandir}/man3/RPC::PlClient.3pm*
%doc %{_mandir}/man3/RPC::PlServer.3pm*
%dir %{perl_vendorlib}/Bundle/
%{perl_vendorlib}/Bundle/PlRPC.pm
%dir %{perl_vendorlib}/RPC/
%{perl_vendorlib}/RPC/PlClient/
%{perl_vendorlib}/RPC/PlClient.pm
%{perl_vendorlib}/RPC/PlServer/
%{perl_vendorlib}/RPC/PlServer.pm

%changelog
* Mon Jun 18 2007 Dries Verachtert <dries@ulyssis.org> - 0.2020-1
- Updated to release 0.2020.

* Wed Dec 29 2004 Dries Verachtert <dries@ulyssis.org> - 0.2018-1
- Updated to release 0.2018.

* Wed Jun 16 2004 Dries Verachtert <dries@ulyssis.org> - 0.2017-1
- Initial package.
