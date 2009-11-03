# $Id$
# Authority: dag
# Upstream: Darren Chamberlain <darren$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name MySQL-Config

Summary: Perl module to parse and utilize MySQL's /etc/my.cnf and ~/.my.cnf files
Name: perl-MySQL-Config
Version: 1.04
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/MySQL-Config/

Source: http://www.cpan.org/modules/by-module/MySQL/MySQL-Config-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-MySQL-Config is a Perl module to parse and utilize
MySQL's /etc/my.cnf and ~/.my.cnf files.

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
%doc %{_mandir}/man3/MySQL::Config.3pm*
%dir %{perl_vendorlib}/MySQL/
%{perl_vendorlib}/MySQL/Config.pm

%changelog
* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 1.04-1
- Updated to version 1.04.

* Sun Oct 07 2007 Dag Wieers <dag@wieers.com> - 1.03-1
- Initial package. (using DAR)
