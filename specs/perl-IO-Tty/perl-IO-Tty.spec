# $Id$

# Authority: dries
# Upstream: Roland Giersig <RGiersig$cpan,org>


%define real_name IO-Tty
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Interface to pseudo Tty
Name: perl-IO-Tty
Version: 1.02
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/IO-Tty/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://search.cpan.org/CPAN/authors/id/R/RG/RGIERSIG/IO-Tty-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
IO::Tty and IO::Pty provide an interface to pseudo ttys.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README 
%{_mandir}/man3/*
%{perl_vendorlib}/*/IO/Tty.pm
%{perl_vendorlib}/*/IO/Tty/*
%{perl_vendorlib}/*/IO/Pty.pm
%{perl_vendorlib}/*/auto/IO/Tty/*

%changelog
* Wed Jun 16 2004 Dries Verachtert <dries@ulyssis.org> - 1.02-1
- Initial package.
