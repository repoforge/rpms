# $Id$

# Authority: dries
# Upstream: Tony Bowden <tony$tmtm,com>

%define real_name Bit-Vector-Minimal
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Object-oriented wrapper around vec()
Name: perl-Bit-Vector-Minimal
Version: 1.1
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Bit-Vector-Minimal/

Source: http://search.cpan.org/CPAN/authors/id/T/TM/TMTM/Bit-Vector-Minimal-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This is a much simplified, lightweight version of Bit::Vector, and wraps
Perl's (sometimes confusing) "vec" function in an object-oriented
abstraction.

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
%{perl_vendorlib}/Bit/Vector/Minimal.pm
%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/*/.packlist

%changelog
* Fri Dec 10 2004 Dries Verachtert <dries@ulyssis.org> - 1.1-1
- Initial package.
