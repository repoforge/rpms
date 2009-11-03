# $Id$
# Authority: dag
# Upstream: Benjamin Sugars <bsugars$canoe,ca>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name IPC-Shareable
%define real_version 0.6

Summary: Share Perl variables between processes
Name: perl-IPC-Shareable
Version: 0.60
Release: 2%{?dist}
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/IPC-Shareable/

Source: http://www.cpan.org/modules/by-module/IPC/IPC-Shareable-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.00503
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl >= 0:5.00503

%description
Share Perl variables between processes.

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

### Clean up docs
find eg/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES COPYING CREDITS MANIFEST README eg/
%doc %{_mandir}/man3/IPC::Shareable.3pm*
%doc %{_mandir}/man3/IPC::Shareable::SharedMem.3pm*
%dir %{perl_vendorlib}/IPC/
%{perl_vendorlib}/IPC/Shareable/
%{perl_vendorlib}/IPC/Shareable.pm

%changelog
* Tue Aug 07 2007 Dag Wieers <dag@wieers.com> - 0.60-2
- Disabled auto-requires for eg/.

* Sun Mar 07 2004 Dag Wieers <dag@wieers.com> - 0.60-1
- Initial package. (using DAR)
