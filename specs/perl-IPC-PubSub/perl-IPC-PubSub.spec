# $Id$
# Authority: dag
# Upstream: Audrey Tang <cpan$audreyt,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name IPC-PubSub

Summary: Interprocess Publish/Subscribe channels
Name: perl-IPC-PubSub
Version: 0.29
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/IPC-PubSub/

Source: http://www.cpan.org/modules/by-module/IPC/IPC-PubSub-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.6.0
Requires: perl >= 0:5.6.0

%description
Interprocess Publish/Subscribe channels.

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
%doc Changes MANIFEST META.yml README SIGNATURE
%doc %{_mandir}/man3/IPC::PubSub.3pm*
%dir %{perl_vendorlib}/IPC/
%{perl_vendorlib}/IPC/PubSub/
%{perl_vendorlib}/IPC/PubSub.pm

%changelog
* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 0.29-1
- Updated to version 0.29.

* Mon Oct 13 2008 Dag Wieers <dag@wieers.com> - 0.28-1
- Updated to release 0.28.

* Mon Nov 05 2007 Dag Wieers <dag@wieers.com> - 0.27-1
- Initial package. (using DAR)
