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
Release: 1.2
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Mail-Alias/

Source: http://www.cpan.org/modules/by-module/Mail/Mail-Alias-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
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
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Mail/Alias.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.12-1.2
- Rebuild for Fedora Core 5.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 1.12-1
- Initial package.
