# $Id$

# Authority: dries
# Upstream: Jos Boumans <kane$dwim,org>

%define real_name Module-Load
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Runtime require of both modules and files
Name: perl-Module-Load
Version: 0.10
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Module-Load/

Source: http://search.cpan.org/CPAN/authors/id/K/KA/KANE/Module-Load-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Runtime require of both modules and files.

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
%doc README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Module/Load.pm
%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/.packlist

%changelog
* Fri Dec 10 2004 Dries Verachtert <dries@ulyssis.org> - 0.10-1
- Initial package.
