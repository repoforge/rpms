# $Id$
# Authority: dag
# Upstream: Brad Fitzpatrick <brad$danga,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Sys-Syscall

Summary: Perl module to access system calls that Perl doesn't normally provide access to
Name: perl-Sys-Syscall
Version: 0.22
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Sys-Syscall/

Source: http://www.cpan.org/modules/by-module/Sys/Sys-Syscall-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Sys-Syscall is a Perl module to access system calls that Perl
doesn't normally provide access to.

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
%doc CHANGES MANIFEST META.yml
%doc %{_mandir}/man3/Sys::Syscall.3pm*
%dir %{perl_vendorlib}/Sys/
%{perl_vendorlib}/Sys/Syscall.pm

%changelog
* Sun Aug 05 2007 Dag Wieers <dag@wieers.com> - 0.22-1
- Initial package. (using DAR)
