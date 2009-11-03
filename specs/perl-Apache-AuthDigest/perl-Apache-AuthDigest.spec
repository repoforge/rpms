# $Id$
# Authority: dag
# Upstream: Geoffrey Young <geoff$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Apache-AuthDigest

Summary: Perl module that reimplements mod_digest in Perl
Name: perl-Apache-AuthDigest
Version: 0.022
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Apache-AuthDigest/

Source: http://www.cpan.org/modules/by-module/Apache/Apache-AuthDigest-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(Apache::ExtUtils)

%description
perl-Apache-AuthDigest is a Perl module that reimplements mod_digest in Perl.

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
find contrib/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST README ToDo contrib/
%doc %{_mandir}/man3/Apache::AuthDigest.3pm*
%dir %{perl_vendorarch}/Apache/
%{perl_vendorarch}/Apache/AuthDigest.pm
%dir %{perl_vendorarch}/auto/Apache/
%{perl_vendorarch}/auto/Apache/AuthDigest/

%changelog
* Wed Oct 10 2007 Dag Wieers <dag@wieers.com> - 0.022-1
- Initial package. (using DAR)
