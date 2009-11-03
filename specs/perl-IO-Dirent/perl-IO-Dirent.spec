# $Id$
# Authority: dag
# Upstream: Scott Wiersdorf <scott$mailblock,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name IO-Dirent

Summary: Access to dirent structs returned by readdir
Name: perl-IO-Dirent
Version: 0.04
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/IO-Dirent/

Source: http://www.cpan.org/modules/by-module/IO/IO-Dirent-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
Access to dirent structs returned by readdir.

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
%doc %{_mandir}/man3/IO::Dirent.3pm*
%dir %{perl_vendorarch}/auto/IO/
%{perl_vendorarch}/auto/IO/Dirent/
%dir %{perl_vendorarch}/IO/
%{perl_vendorarch}/IO/Dirent.pm

%changelog
* Thu Dec 06 2007 Dag Wieers <dag@wieers.com> - 0.04-1
- Initial package. (using DAR)
