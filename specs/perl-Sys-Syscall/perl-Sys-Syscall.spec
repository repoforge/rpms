# $Id$
# Authority: dag
# Upstream: Brad Fitzpatrick <brad$danga,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Sys-Syscall

Summary: Perl module to access system calls that Perl doesn't normally provide access to
Name: perl-Sys-Syscall
Version: 0.23
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Sys-Syscall/

Source: http://search.cpan.org/CPAN/authors/id/B/BR/BRADFITZ/Sys-Syscall-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl(POSIX)
BuildRequires: perl(Test::More)
Requires: perl(POSIX)
Requires: perl(Test::More)

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
perl-Sys-Syscall is a Perl module to access system calls that Perl
doesn't normally provide access to.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}
%{__make} test

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
%doc %{_mandir}/man3/Sys::README.3pm*
%dir %{perl_vendorlib}/Sys/
%{perl_vendorlib}/Sys/Syscall.pm
%{perl_vendorlib}/Sys/README.pod

%changelog
* Thu Feb 10 2011 Christoph Maser <cmaser@gmx.de> - 0.23-1
- Updated to version 0.23.

* Sun Aug 05 2007 Dag Wieers <dag@wieers.com> - 0.22-1
- Initial package. (using DAR)
