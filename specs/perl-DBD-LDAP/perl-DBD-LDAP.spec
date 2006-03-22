# $Id$
# Authority: dries
# Upstream: Jim Turner <turnerjw$wwol,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name DBD-LDAP

Summary: SQL/Perl DBI interface to Ldap databases
Name: perl-DBD-LDAP
Version: 0.06
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DBD-LDAP/

Source: http://search.cpan.org/CPAN/authors/id/T/TU/TURNERJW/DBD-LDAP-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl-DBI

%description
DBD::LDAP - A DBI driver for LDAP databases.  LDAP stands for the 
"Lightweight Directory Access Protocol".  For more information, 
see:  http://www.ogre.com/ldap/docs.html
	
%prep
%setup -n %{real_name}-%{version}
%{__perl} -pi -e 's|/usr/local/bin/perl5|/usr/bin/perl|g;' */*.pm

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
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
%{perl_vendorlib}/DBD/LDAP.pm
%{perl_vendorlib}/JLdap.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.06-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.06-1
- Initial package.
