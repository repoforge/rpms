# $Id$

# Authority: dries
# Upstream: Damian Conway <damian$conway,org>

%define real_name Perl6-Slurp
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Implements the Perl 6 'slurp' built-in
Name: perl-Perl6-Slurp
Version: 0.03
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Perl6-Slurp/

Source: http://search.cpan.org/CPAN/authors/id/D/DC/DCONWAY/Perl6-Slurp-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This package implements the Perl 6 'slurp' built-in.

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
%{perl_vendorlib}/Perl6/Slurp.pm
%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/.packlist

%changelog
* Tue Dec 07 2004 Dries Verachtert <dries@ulyssis.org> - 0.03-1
- Initial package.
