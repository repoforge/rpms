# $Id$
# Authority: dag
# Upstream: D. Hageman <dhageman$dracken,com>
# Needs cups >= 1.2.2
# ExcludeDist: el4

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-CUPS

Summary: Perl module that implements a Common Unix Printing System Interface
Name: perl-Net-CUPS
Version: 0.60
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-CUPS/

Source: http://www.cpan.org/modules/by-module/Net/Net-CUPS-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: cups-devel >= 1:1.2.2
BuildRequires: perl

%description
perl-Net-CUPS is a Perl module that implements a Perl module implements
a Common Unix Printing System Interface.

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

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST README TODO examples/
%doc %{_mandir}/man3/Net::CUPS.3pm*
%doc %{_mandir}/man3/Net::CUPS::*.3pm*
%dir %{perl_vendorarch}/auto/Net/
%{perl_vendorarch}/auto/Net/CUPS/
%dir %{perl_vendorarch}/Net/
%{perl_vendorarch}/Net/CUPS/
%{perl_vendorarch}/Net/CUPS.pm

%changelog
* Wed Aug  5 2009 Christoph Maser <cmr@financial.com> - 0.60-1
- Updated to version 0.60.

* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 0.59-1
- Updated to version 0.59.

* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 0.56-1
- Updated to release 0.56.

* Thu Nov 15 2007 Dag Wieers <dag@wieers.com> - 0.55-1
- Updated to release 0.55.

* Sat Aug 04 2007 Dag Wieers <dag@wieers.com> - 0.51-1
- Initial package. (using DAR)
