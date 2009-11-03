# $Id$
# Authority: dag
# Upstream: Bruni Emiliano <info$ebruni,it>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Qmail-Mysql

Summary: Perl module for mysql database used by qmail-mysql
Name: perl-Qmail-Mysql
Version: 0.02
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Qmail-Mysql/

Source: http://www.cpan.org/authors/id/E/EB/EBRUNI/Qmail-Mysql-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Qmail-Mysql is a Perl module for mysql database used by qmail-mysql.

This package contains the following Perl module:

    Qmail::Mysql

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
%doc %{_mandir}/man3/Qmail::Mysql.3pm*
%dir %{perl_vendorlib}/Qmail/
%{perl_vendorlib}/Qmail/Mysql.pm
%{perl_vendorlib}/Qmail/Mysql.pod

%changelog
* Thu Oct 11 2007 Dag Wieers <dag@wieers.com> - 0.02-1
- Initial package. (using DAR)
