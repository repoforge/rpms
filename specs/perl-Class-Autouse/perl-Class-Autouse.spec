# $Id$

# Authority: dries
# Upstream: Adam Kennedy <cpan$ali,as>

%define real_name Class-Autouse
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

Summary: Run-time class loading on first method call
Name: perl-Class-Autouse
Version: 1.16
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Class-Autouse/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://search.cpan.org/CPAN/authors/id/A/AD/ADAMK/Class-Autouse-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl-ExtUtils-AutoInstall

%description
Class::Autouse allows you to specify a class the will only load when a
method of that class is called. For large classes that might not be used
during the running of a program, such as Date::Manip, this can save you
large amounts of memory, and decrease the script load time.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS="vendor" \
	PREFIX=%{buildroot}%{_prefix}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib} \
	%{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README Changes
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Class/Autouse.pm
#%{perl_vendorlib}/Class/prefork.pm
%{perl_vendorlib}/Class/Autouse

%changelog
* Fri Mar  4 2005 Dries Verachtert <dries@ulyssis.org> - 1.16-1
- Updated to release 1.16.

* Tue Dec 07 2004 Dries Verachtert <dries@ulyssis.org> - 1.12-1
- Initial package.
