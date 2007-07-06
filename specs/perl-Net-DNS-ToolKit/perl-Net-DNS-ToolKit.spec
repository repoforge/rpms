# $Id$

# Authority: dries
# Upstream: Michael Robinton <michael$bizsystems,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-DNS-ToolKit

Summary: Routines to pick apart, examine and put together DNS packets
Name: perl-Net-DNS-ToolKit
Version: 0.31
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-DNS-ToolKit/

Source: http://www.cpan.org/modules/by-module/Net/Net-DNS-ToolKit-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
Routines to pick apart, examine and put together DNS packets. They can
be used for diagnostic purposes or as building blocks for DNS
applications such as DNS servers and clients or to allow user
applications to interact directly with remote DNS servers.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}/auto/*{,/*{,/*}}/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Artistic Changes INSTALL MANIFEST META.yml README
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorarch}/Net/
%dir %{perl_vendorarch}/Net/DNS/
%{perl_vendorarch}/Net/DNS/ToolKit.pm
%{perl_vendorarch}/Net/DNS/ToolKit/
%dir %{perl_vendorarch}/auto/Net/
%dir %{perl_vendorarch}/auto/Net/DNS/
%{perl_vendorarch}/auto/Net/DNS/ToolKit/

%changelog
* Thu Jul  5 2007 Quien Sabe (aka Jim) <quien-sabe@metaorg.com> - 0.31-1
- Updated to latest upstream version { old source not available }

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.26-1
- Updated to release 0.26.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 0.25-1
- Updated to release 0.25.

* Fri Mar  4 2005 Dries Verachtert <dries@ulyssis.org> - 0.24-1
- Updated to release 0.24.

* Wed Dec 29 2004 Dries Verachtert <dries@ulyssis.org> - 0.23-1
- Updated to release 0.23.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 0.17-1
- Initial package.
