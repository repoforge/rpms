# $Id$
# Authority: dag
# Upstream: Steffen Ullrich <Steffen_Ullrich$genua,de>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name IO-Socket-SSL

Summary: Nearly transparent SSL encapsulation for IO::Socket::INET
Name: perl-IO-Socket-SSL
Version: 1.34
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/IO-Socket-SSL/

Source: http://search.cpan.org/CPAN/authors/id/S/SU/SULLR/IO-Socket-SSL-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Net::SSLeay) >= 1.21
BuildRequires: perl(Scalar::Util)
Requires: perl(Net::SSLeay) >= 1.21
Requires: perl(Scalar::Util)

Provides: perl-Net-Nessus-XMLRPC-alternative = 0.20

%filter_from_requires /^perl*/d
%filter_setup


%description
Nearly transparent SSL encapsulation for IO::Socket::INET.

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

### Clean up docs
find docs/ example/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc BUGS Changes MANIFEST META.yml README* docs/ example/
%doc %{_mandir}/man3/IO::Socket::SSL.3pm*
%dir %{perl_vendorlib}/IO/
%dir %{perl_vendorlib}/IO/Socket/
%{perl_vendorlib}/IO/Socket/SSL.pm

%changelog
* Tue Nov 02 2010 David Hrbáč <david@hrbac.cz> - 1.34-1
- new upstream release

* Thu Sep 23 2010 David Hrbáč <david@hrbac.cz> - 1.33-1
- new upstream release

* Tue May 04 2010 Steve Huff <shuff@vecna.org> - 1.31-2
- Satisfies an alternative dependency for perl-Net-Nessus-XMLRPC.

* Wed Dec 23 2009 Christoph Maser <cmr@financial.com> - 1.31-1
- Updated to version 1.31.

* Wed Sep  9 2009 Christoph Maser <cmr@financial.com> - 1.30-1
- Updated to version 1.30.

* Fri Aug  7 2009 Christoph Maser <cmr@financial.com> - 1.27-1
- Updated to version 1.27.

* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 1.26-1
- Updated to version 1.26.

* Wed Oct 15 2008 Dag Wieers <dag@wieers.com> - 1.17-1
- Updated to release 1.17.

* Wed Oct 08 2008 Dag Wieers <dag@wieers.com> - 1.16-1
- Updated to release 1.16.

* Tue Nov 13 2007 Dag Wieers <dag@wieers.com> - 1.13-1
- Updated to release 1.13.

* Tue Nov 13 2007 Dag Wieers <dag@wieers.com> - 1.12-1
- Updated to release 1.12.

* Tue Aug 07 2007 Dag Wieers <dag@wieers.com> - 1.07-2
- Disabled auto-requires for docs/ and example/.

* Mon Jun 18 2007 Dries Verachtert <dries@ulyssis.org> - 1.07-1
- Updated to release 1.07.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 1.05-1
- Updated to release 1.05.

* Mon Oct 09 2006 Dag Wieers <dag@wieers.com> - 1.01-1
- Updated to release 1.01.

* Wed Aug 16 2006 Dag Wieers <dag@wieers.com> - 0.999-1
- Updated to release 0.999.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 0.97-1
- Updated to release 0.97.

* Wed Oct 20 2004 Dries Verachtert <dries@ulyssis.org> - 0.96-0
- Update to release 0.96.

* Mon Jul 14 2003 Dag Wieers <dag@wieers.com> - 0.94-0
- Updated to release 0.94.
- Initial package. (using DAR)
