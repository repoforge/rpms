# $Id$

# Authority: dries
# Upstream: Tom Zeltwanger <perl$ename,com>

%define real_name Mail-Alias
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Direct manipulation of email alias files
Name: perl-Mail-Alias
Version: 1.12
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Mail-Alias/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://search.cpan.org/CPAN/authors/id/Z/ZE/ZELT/Mail-Alias-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
ail::Alias allows you to directly access the contents of E-Mail alias files. 
You can perform the following actions:
	Set the name of the current aliases file being accessed
	Verify the presence of aliases
	Retrieve an alias line from the file
	Add aliases
	Change the addresses for aliases
	Delete aliases

Direct access of the files has a small price. When files are being manipulated
directly, operations are somewhat slower than they would be if the entire
alias file contents was brought into memory first. However, this provides the
most flexibility, and does not disrupt the ordering of the file, or any
comments in the file. This delay factor will not be a problem unless you have
huge alias files. After you make changes, don't forget you will need to rebuild
the active alias database (for SENDMAIL this is done by executing the NEWALIASES
command).

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
%doc README Changes
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Mail/Alias.pm
%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/.packlist

%changelog
* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 1.12-1
- Initial package.
