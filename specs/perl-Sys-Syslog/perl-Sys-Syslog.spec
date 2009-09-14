# $Id$
# Authority: cmr
# Upstream: Sebastien Aperghis-Tramoni <sebastien$aperghis,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Sys-Syslog

Summary: Perl interface to the UNIX syslog(3) calls
Name: perl-Sys-Syslog
Version: 0.27
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Sys-Syslog/

Source: http://www.cpan.org/modules/by-module/Sys/Sys-Syslog-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
# From yaml requires
BuildRequires: perl(Carp)
BuildRequires: perl(Fcntl)
BuildRequires: perl(File::Basename)
BuildRequires: perl(File::Spec)
BuildRequires: perl(POSIX)
BuildRequires: perl(Socket)
BuildRequires: perl(Test::More)
BuildRequires: perl(XSLoader)


%description
Perl interface to the UNIX syslog(3) calls.

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
find eg/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README README.win32 eg/
%doc %{_mandir}/man3/Sys::Syslog.3pm*
%dir %{perl_vendorarch}/auto/Sys/
%{perl_vendorarch}/auto/Sys/Syslog/
%dir %{perl_vendorarch}/Sys/
%{perl_vendorarch}/Sys/Syslog.pm

%changelog
* Mon Sep 14 2009 Christoph Maser <cmr@financial.com> - 0.27-1
- Initial package. (using DAR)
