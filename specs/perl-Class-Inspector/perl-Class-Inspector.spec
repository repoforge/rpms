# $Id$
# Authority: dries
# Upstream: Adam Kennedy <cpan$ali,as>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Class-Inspector

Summary: Provides information about Classes
Name: perl-Class-Inspector
Version: 1.08
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Class-Inspector/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://www.cpan.org/modules/by-module/Class/Class-Inspector-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Class::Inspector allows you to get information about a loaded class.
Most or all of this information can be found in other ways, but they
arn't always very friendly, and usually involve a relatively high level
of Perl wizardry, or strange and unusual looking code. Class::Inspector
attempts to provide an easier, more friendly interface to this
information.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS="vendor" \
	PREFIX="%{buildroot}%{_prefix}"
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
%doc README Changes
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/Class/
%{perl_vendorlib}/Class/Inspector.pm

%changelog
* Fri Mar  4 2005 Dries Verachtert <dries@ulyssis.org> - 1.08-1
- Updated to release 1.08.

* Sun Jan 16 2005 Dries Verachtert <dries@ulyssis.org> - 1.07-1
- Initial package.

