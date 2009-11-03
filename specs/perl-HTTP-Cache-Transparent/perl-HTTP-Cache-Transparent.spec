# $Id$
# Authority: dag
# Upstream: Mattias Holmlund <u108$m1,holmlund,se>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name HTTP-Cache-Transparent

Summary: Perl module to cache the result of http get-requests persistently
Name: perl-HTTP-Cache-Transparent
Version: 1.0
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/HTTP-Cache-Transparent/

Source: http://www.cpan.org/modules/by-module/HTTP/HTTP-Cache-Transparent-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
perl-HTTP-Cache-Transparent is a Perl module to cache the result
of http get-requests persistently.

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
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README examples/
%doc %{_mandir}/man3/HTTP::Cache::Transparent.3pm*
%dir %{perl_vendorlib}/HTTP/
%dir %{perl_vendorlib}/HTTP/Cache/
#%{perl_vendorlib}/HTTP/Cache/Transparent/
%{perl_vendorlib}/HTTP/Cache/Transparent.pm

%changelog
* Fri Dec 14 2007 Dag Wieers <dag@wieers.com> - 1.0-1
- Updated to release 1.0.

* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 0.7-1
- Initial package. (using DAR)
