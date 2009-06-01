# $Id$
# Authority: dag
# Upstream: Oliver Gorwits <oliver,gorwits$oucs,ox,ac,uk>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-MAC

Summary: Perl extension for representing and manipulating MAC addresses
Name: perl-Net-MAC
Version: 1.5
Release: 1
License: GPL/LGPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-MAC/

Source: http://www.cpan.org/modules/by-module/Net/Net-MAC-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 2:5.8.0
Requires: perl >= 2:5.8.0

%description
Perl extension for representing and manipulating MAC addresses.

%prep
%setup -n %{real_name}-%{version}

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
%doc Changes INSTALL MANIFEST META.yml README
%doc %{_mandir}/man3/Net::MAC.3pm*
%dir %{perl_vendorlib}/Net/
#%{perl_vendorlib}/Net/MAC/
%{perl_vendorlib}/Net/MAC.pm

%changelog
* Mon Jun  1 2009 Dries Verachtert <dries@ulyssis.org> - 1.5-1
- Updated to release 1.5.

* Tue Sep 16 2008 Dag Wieers <dag@wieers.com> - 1.4-1
- Initial package. (using DAR)
