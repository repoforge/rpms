# $Id$
# Authority: dries
# Upstream: John D Groenveld <groenveld$acm,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Apache-DBILogin

Summary: Authenticates and authorizes via a DBI connection
Name: perl-Apache-DBILogin
Version: 2.06
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Apache-DBILogin/

Source: http://search.cpan.org/CPAN/authors/id/J/JG/JGROENVEL/Apache-DBILogin-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
The perl module Apache::DBILogin uses Apache mod_perl and the
DBI/DBD modules to integrate database authentication with Apache.

%prep
%setup -n %{real_name}-%{version}

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
%{perl_vendorlib}/Apache/DBILogin.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 2.06-1.2
- Rebuild for Fedora Core 5.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 2.06-1
- Updated to release 2.06.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 2.03-1
- Initial package.
