# $Id$
# Authority: dag
# Upstream: Jim Pirzyk <pirzyk$freebsd,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Unix-Mknod

Summary: Perl module for mknod, major, minor, and makedev
Name: perl-Unix-Mknod
Version: 0.04
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Unix-Mknod/

Source: http://www.cpan.org/modules/by-module/Unix/Unix-Mknod-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
perl-Unix-Mknod is a Perl module for mknod, major, minor, and makedev.

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Unix::Mknod.3pm*
%dir %{perl_vendorarch}/auto/Unix/
%{perl_vendorarch}/auto/Unix/Mknod/
%dir %{perl_vendorarch}/Unix/
%{perl_vendorarch}/Unix/Mknod.pm

%changelog
* Thu Dec 27 2007 Dag Wieers <dag@wieers.com> - 0.04-1
- Updated to release 0.04.

* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 0.03-1
- Initial package. (using DAR)
