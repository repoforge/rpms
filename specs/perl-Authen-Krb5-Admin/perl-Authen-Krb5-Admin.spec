# $Id$
# Authority: dag
# Upstream: Andrew J. Korty <ajk$iu,edu>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Authen-Krb5-Admin

Summary: Perl extension for MIT Kerberos 5 admin interface
Name: perl-Authen-Krb5-Admin
Version: 0.11
Release: 1
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Authen-Krb5-Admin/

Source: http://www.cpan.org/modules/by-module/Authen/Authen-Krb5-Admin-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(Authen::Krb5) >= 1.2
BuildRequires: perl(Test)

%description
Perl extension for MIT Kerberos 5 admin interface.

%prep
%setup -n %{real_name}-%{version}

%{__perl} -pi.orig -e 's|<com_err.h>|<et/com_err.h>|g' Admin.c Admin.xs

%build
echo | CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
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
%doc COPYING ChangeLog MANIFEST MANIFEST.SKIP META.yml README SIGNATURE
%doc %{_mandir}/man3/Authen::Krb5::Admin.3pm*
%dir %{perl_vendorarch}/auto/Authen/
%dir %{perl_vendorarch}/auto/Authen/Krb5/
%{perl_vendorarch}/auto/Authen/Krb5/Admin/
%dir %{perl_vendorarch}/Authen/
%dir %{perl_vendorarch}/Authen/Krb5/
%{perl_vendorarch}/Authen/Krb5/Admin.pm

%changelog
* Thu Feb 28 2008 Dag Wieers <dag@wieers.com> - 0.11-1
- Updated to release 0.11.

* Sun Feb 17 2008 Dag Wieers <dag@wieers.com> - 0.10-1
- Updated to release 0.10.

* Mon Nov 26 2007 Dag Wieers <dag@wieers.com> - 0.09-1
- Fixed a compilation problem on RHEL and Fedora. (Claudio Strizzolo)
- Initial package. (using DAR)
