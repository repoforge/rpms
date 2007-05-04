# $Id$
# Authority: dag
# Upstream: Mattias Holmlund <u108$m1,holmlund,se>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name HTTP-Cache-Transparent

Summary: Perl module to cache the result of http get-requests persistently
Name: perl-HTTP-Cache-Transparent
Version: 0.7
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/HTTP-Cache-Transparent/

Source: http://www.cpan.org/modules/by-module/HTTP/HTTP-Cache-Transparent-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

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
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/HTTP::Cache::Transparent.3pm*
%dir %{perl_vendorlib}/HTTP/
%dir %{perl_vendorlib}/HTTP/Cache/
%{perl_vendorlib}/HTTP/Cache/Transparent.pm

%changelog
* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 0.7-1
- Initial package. (using DAR)
