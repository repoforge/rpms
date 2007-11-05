# $Id$
# Authority: dag
# Upstream: Jesse Vincent <jesse+cpan$fsck,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Jifty-DBI

Summary: Perl module that implements an object-relational persistence framework
Name: perl-Jifty-DBI
Version: 0.43
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Jifty-DBI/

Source: http://www.cpan.org/modules/by-module/Jifty/Jifty-DBI-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 2:5.8.3 
BuildRequires: perl(DBD::SQLite)
BuildRequires: perl(Test::More) >= 0.52

%description
perl-Jifty-DBI is a Perl module that implements an object-relational
persistence framework.

This package contains the following Perl module:

    Jifty::DBI

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
find doc/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README ROADMAP SIGNATURE doc/
%doc %{_mandir}/man3/Jifty::DBI.3pm*
%dir %{perl_vendorlib}/Jifty/
#%{perl_vendorlib}/Jifty/DBI/
%{perl_vendorlib}/Jifty/DBI.pm

%changelog
* Mon Nov 05 2007 Dag Wieers <dag@wieers.com> - 0.43-1
- Initial package. (using DAR)
