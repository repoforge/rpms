# $Id$

# Authority: dries
# Upstream: Martyn J. Pearce <fluffy$cpan,org>

%define real_name Class-MethodMaker
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Create generic methods for OO Perl
Name: perl-Class-MethodMaker
Version: 2.05
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Class-MethodMaker/

Source: http://search.cpan.org/CPAN/authors/id/F/FL/FLUFFY/Class-MethodMaker-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
This package allows you to create generic methods for OO Perl.

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
%{perl_vendorarch}/Class/MethodMaker.pm
%{perl_vendorarch}/Class/MethodMaker
%{perl_vendorarch}/auto/Class/MethodMaker
%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/.packlist

%changelog
* Wed Feb  2 2005 Dries Verachtert <dries@ulyssis.org> - 2.05-1
- Initial package.

