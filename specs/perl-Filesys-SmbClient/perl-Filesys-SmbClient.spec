# $Id$
# Authority: dries
# Upstream: Alain Barbet <alian$alianwebserver,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Filesys-SmbClient

Summary: Samba client
Name: perl-Filesys-SmbClient
Version: 3.1
Release: 1
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Filesys-SmbClient/

Source: http://search.cpan.org/CPAN/authors/id/A/AL/ALIAN/Filesys-SmbClient-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, perl(ExtUtils::MakeMaker), samba-common

%description
Perl client to reach Samba resources with smbclient.

%prep
%setup -n %{real_name}-%{version}

%build
echo | %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/Filesys::SmbClient*
%dir %{perl_vendorarch}/Filesys/
%{perl_vendorarch}/Filesys/SmbClient.pm
%dir %{perl_vendorarch}/auto/
%dir %{perl_vendorarch}/auto/Filesys/
%{perl_vendorarch}/auto/Filesys/SmbClient/

%changelog
* Tue Sep 11 2007 Dries Verachtert <dries@ulyssis.org> - 3.1-1
- Initial package.
