# $Id$
# Authority: dag

# ExclusiveDist: rh6 rh7 rh8

%{?dist: %{expand: %%define %dist 1}}

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Digest-HMAC

Name: perl-Digest-HMAC
Version: 1.01
Release: 1
Summary: Digest-HMAC Perl module
License: distributable
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Digest-HMAC/

Source: http://www.cpan.org/modules/by-module/Digest/Digest-HMAC-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.00503

BuildRequires: perl(Digest::SHA1)
%{?rh7:BuildRequires: perl(Digest::MD5)}
Requires: perl(Digest::SHA1)
%{?rh7:BuildRequires: perl(Digest::MD5)}

%description
HMAC is used for message integrity checks between two parties that
share a secret key, and works in combination with some other Digest
algorithm, usually MD5 or SHA-1. The HMAC mechanism is described in
RFC 2104.

HMAC follow the common Digest:: interface, but the constructor takes
the secret key and the name of some other simple Digest:: as argument.

%prep
%setup -n %{real_name}-%{version} 

%build
%{__perl} Makefile.PL PREFIX="%{buildroot}%{_prefix}" INSTALLDIRS="vendor"
%{__make} %{?_smp_mflags}
#{__make} %{?_smp_mflags} test

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README rfc2104.txt
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/Digest/
%{perl_vendorlib}/Digest/HMAC.pm

%changelog
* Sun Jan 26 2003 Dag Wieers <dag@wieers.com>
- Initial package. (using DAR)
