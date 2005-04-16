# $Id$
# Authority: dries
# Upstream: Alain Barbet <alian$alianwebserver,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Filesys-SmbClientParser

Summary: Samba client
Name: perl-Filesys-SmbClientParser
Version: 2.7
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Filesys-SmbClientParser/

Source: http://search.cpan.org/CPAN/authors/id/A/AL/ALIAN/Filesys-SmbClientParser-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Perl client to reach Samba resources with smbclient.

%prep
%setup -n %{real_name}-%{version}

%build
echo | %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Filesys/SmbClientParser.pm

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 2.7-1
- Initial package.

