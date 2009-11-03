# $Id$
# Authority: dries
# Upstream: Rolf Harold Nelson <rolf$usa,healthnet,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name SyslogScan

Summary: Parse system logs
Name: perl-SyslogScan
Version: 0.32
Release: 1.2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/SyslogScan/

Source: http://www.cpan.org/modules/by-module/SyslogScan/SyslogScan-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
SyslogScan contains routines to parse system logs.  The package
includes a sample application, read_mail_log.pl, which can print out
various statistics about mail sent and received.

%prep
%setup -n %{real_name}-%{version}
%{__perl} -pi -e 's|/usr/bin/perl5|/usr/bin/perl|g;' *.pl t/*.t

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
%doc README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/SyslogScan
%{perl_vendorlib}/read_mail_log.pl

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.32-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.32-1
- Initial package.
