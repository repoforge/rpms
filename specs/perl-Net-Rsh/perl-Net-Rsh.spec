# $Id$
# Authority: dag
# Upstream: Oleg Prokopyev <riiki$gu,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-Rsh

Summary: Perl module that implements a client for Rsh protocol
Name: perl-Net-Rsh
Version: 0.05
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-Rsh/

Source: http://www.cpan.org/modules/by-module/Net/Net-Rsh-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Net-Rsh is a Perl module that implements a client for Rsh protocol.

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
%doc Changes MANIFEST README
%doc %{_mandir}/man3/Net::Rsh.3pm*
%dir %{perl_vendorlib}/Net/
%{perl_vendorlib}/Net/Rsh.pm

%changelog
* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 0.05-1
- Updated to version 0.05.

* Sun Oct 07 2007 Dag Wieers <dag@wieers.com> - 0.02-1
- Initial package. (using DAR)
