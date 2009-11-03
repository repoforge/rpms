# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Apache-Session-Memcached

Summary: Perl module to store persistent data using memcached
Name: perl-Apache-Session-Memcached
Version: 0.03
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Apache-Session-Memcached/

Source: http://www.cpan.org/modules/by-module/Apache/Apache-Session-Memcached-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Apache-Session-Memcached is a Perl module to store persistent data
using memcached.

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
%doc %{_mandir}/man3/Apache::Session::Memcached.3pm*
%doc %{_mandir}/man3/Apache::Session::Store::Memcached.3pm*
%dir %{perl_vendorlib}/Apache/
%dir %{perl_vendorlib}/Apache/Session/
%{perl_vendorlib}/Apache/Session/Memcached.pm
%dir %{perl_vendorlib}/Apache/Session/Store/
%{perl_vendorlib}/Apache/Session/Store/Memcached.pm

%changelog
* Wed Oct 10 2007 Dag Wieers <dag@wieers.com> - 0.03-1
- Initial package. (using DAR)
