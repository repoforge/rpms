# $Id$
# Authority: dag
# Upstream: Steve Peters <steve$fisharerojo,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-Ping

Summary: Perl module to check a remote host for reachability
Name: perl-Net-Ping
Version: 2.36
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-Ping/

Source: http://www.cpan.org/modules/by-module/Net/Net-Ping-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Net-Ping is a Perl module to check a remote host for reachability.

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Net::Ping.3pm*
%dir %{perl_vendorlib}/Net/
%{perl_vendorlib}/Net/Ping.pm

%changelog
* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 2.36-1
- Updated to version 2.36.

* Thu Feb 21 2008 Dag Wieers <dag@wieers.com> - 2.35-1
- Updated to release 2.35.

* Thu Dec 27 2007 Dag Wieers <dag@wieers.com> - 2.34-1
- Updated to release 2.34.

* Sun Oct 07 2007 Dag Wieers <dag@wieers.com> - 2.33-1
- Initial package. (using DAR)
