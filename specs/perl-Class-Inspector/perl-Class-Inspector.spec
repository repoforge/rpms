# $Id$

# Authority: dries
# Upstream: Adam Kennedy <cpan$ali,as>

%define real_name Class-Inspector
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Provides information about Classes
Name: perl-Class-Inspector
Version: 1.07
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Class-Inspector/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://search.cpan.org/CPAN/authors/id/A/AD/ADAMK/Class-Inspector-%{version}.tar.gz
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
%{perl_vendorlib}/Class/Inspector.pm
%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/.packlist

%changelog
* Sun Jan 16 2005 Dries Verachtert <dries@ulyssis.org> - 1.07-1
- Initial package.

