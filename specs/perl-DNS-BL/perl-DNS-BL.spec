# $Id$

# Authority: dries
# Upstream: Luis Mu&#241;oz <luismunoz$cpan,org>

%define real_name DNS-BL
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Manage DNS black lists
Name: perl-DNS-BL
Version: 0.03
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DNS-BL/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://search.cpan.org/CPAN/authors/id/L/LU/LUISMUNOZ/DNS-BL-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Modules and  scripts that  ease the maintenance  and operation  of DNS
blacklists. See  perldoc for more information. The  blacklist might be
stored in  a Berkeley DB or  in a DBI-supported  database. Scripts and
instructions are included for installation with MySQL.

The blacklists can be exported  to various formats, to load into name
servers.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" destdir=%{buildroot}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README*
%doc %{_mandir}/man3/*
%doc %{_mandir}/man1/*
%{_bindir}/dnsbltool
%{perl_vendorlib}/DNS/BL.pm
%{perl_vendorlib}/DNS/BL
%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/.packlist

# perl_vendorlib: /usr/lib/perl5/vendor_perl/5.8.0
# perl_vendorarch: /usr/lib/perl5/vendor_perl/5.8.0/i386-linux-thread-multi
# perl_archlib: /usr/lib/perl5/5.8.0/i386-linux-thread-multi
# perl_privlib: /usr/lib/perl5/5.8.0

%changelog
* Mon Dec 27 2004 Dries Verachtert <dries@ulyssis.org> - 0.03-1
- Initial package.

