# $Id$
# Authority: dries
# Upstream: Luis Mu&#241;oz <luismunoz$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name DNS-BL

Summary: Manage DNS black lists
Name: perl-DNS-BL
Version: 0.03
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DNS-BL/

Source: http://www.cpan.org/modules/by-module/DNS/DNS-BL-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

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
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} \
		%{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README*
%doc %{_mandir}/man3/*
%doc %{_mandir}/man1/*
%{_bindir}/dnsbltool
%dir %{perl_vendorlib}/DNS/
%{perl_vendorlib}/DNS/BL.pm
%{perl_vendorlib}/DNS/BL/

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.03-1.2
- Rebuild for Fedora Core 5.

* Mon Dec 27 2004 Dries Verachtert <dries@ulyssis.org> - 0.03-1
- Initial package.

