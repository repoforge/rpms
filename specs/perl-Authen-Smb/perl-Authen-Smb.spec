# $Id$
# Authority: dries
# Upstream: Patrick Michael Kane <modus-cpan$pr,es,to>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Authen-Smb

Summary: Authenticate against an SMB server
Name: perl-Authen-Smb
Version: 0.91
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Authen-Smb/

Source: http://www.cpan.org/modules/by-module/Authen/Authen-Smb-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
Authen::Smb allows you to authenticate users against an NT server.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README Changes
%{_mandir}/man3/*
%{perl_vendorarch}/Authen/Smb.pm
%{perl_vendorarch}/auto/Authen/Smb

%changelog
* Wed Jun 16 2004 Dries Verachtert <dries@ulyssis.org> - 0.91-1
- Initial package.

