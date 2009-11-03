# $Id$
# Authority: dries
# Upstream: Alain Barbet <alian$alianwebserver,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Filesys-SmbClient

Summary: Samba client
Name: perl-Filesys-SmbClient
Version: 3.1
Release: 1%{?dist}
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Filesys-SmbClient/

Source: http://www.cpan.org/modules/by-module/Filesys/Filesys-SmbClient-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: samba-common >= 3.0

%description
Perl client to reach Samba resources with smbclient.

%prep
%setup -n %{real_name}-%{version}

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
%doc Changes COPYING MANIFEST META.yml README
%doc %{_mandir}/man3/Filesys::SmbClient.3pm*
%dir %{perl_vendorarch}/Filesys/
%{perl_vendorarch}/Filesys/SmbClient.pm
%dir %{perl_vendorarch}/auto/Filesys/
%{perl_vendorarch}/auto/Filesys/SmbClient/

%changelog
* Tue Sep 11 2007 Dries Verachtert <dries@ulyssis.org> - 3.1-1
- Initial package.
