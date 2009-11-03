# $Id$
# Authority: dag
# Upstream: Leif Johanson <leifj$it,su,se>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Heimdal-Kadm5

Summary: Perl module to interface with Heimdal Kerberos 5
Name: perl-Heimdal-Kadm5
Version: 0.06
Release: 1%{?dist}
License: BSD
Group: Applications/CPAN
URL: ftp://ftp.su.se/pub/users/leifj/

Source: ftp://ftp.su.se/pub/users/leifj/Heimdal-Kadm5-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: heimdal-devel
BuildRequires: perl

%description
perl-Heimdal-Kadm5 is a Perl module to interface with Heimdal Kerberos 5.

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

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README test.pl
%doc %{_mandir}/man3/Heimdal::Kadm5.3pm*
%dir %{perl_vendorarch}/Heimdal/
%{perl_vendorarch}/Heimdal/Kadm5.pm
%dir %{perl_vendorarch}/auto/Heimdal/
%{perl_vendorarch}/auto/Heimdal/Kadm5/

%changelog
* Tue Oct 16 2007 Dag Wieers <dag@wieers.com> - 0.06-1
- Initial package. (using DAR)
