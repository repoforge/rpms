# $Id$

# Authority: dries
# Upstream: Michael Robinton <michael$bizsystems,com>

%define real_name Net-DNS-ToolKit
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Routines to pick apart, examine and put together DNS packets
Name: perl-Net-DNS-ToolKit
Version: 0.23
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-DNS-ToolKit/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://search.cpan.org/CPAN/authors/id/M/MI/MIKER/Net-DNS-ToolKit-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
Routines to pick apart, examine and put together DNS packets. They can
be used for diagnostic purposes or as building blocks for DNS
applications such as DNS servers and clients or to allow user
applications to interact directly with remote DNS servers.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README Changes
%doc %{_mandir}/man3/*
%{perl_vendorarch}/Net/DNS/ToolKit.pm
%{perl_vendorarch}/Net/DNS/ToolKit
%{perl_vendorarch}/auto/Net/DNS/ToolKit

%changelog
* Wed Dec 29 2004 Dries Verachtert <dries@ulyssis.org> - 0.23-1
- Updated to release 0.23.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 0.17-1
- Initial package.
