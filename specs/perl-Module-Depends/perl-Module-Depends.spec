# $Id$

# Authority: dries
# Upstream: Richard Clamp <richardc$unixbeard,net>

%define real_name Module-Depends
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Identify the dependencies of a distribution
Name: perl-Module-Depends
Version: 0.07
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Module-Depends/

Source: http://search.cpan.org/CPAN/authors/id/R/RC/RCLAMP/Module-Depends-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Identify the dependencies of a distribution.

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
%{perl_vendorlib}/Module/Depends.pm
%{perl_vendorlib}/Module/Depends
%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/.packlist

%changelog
* Fri Mar  4 2005 Dries Verachtert <dries@ulyssis.org> - 0.07-1
- Updated to release 0.07.

* Fri Dec 10 2004 Dries Verachtert <dries@ulyssis.org> - 0.05-1
- Initial package.
