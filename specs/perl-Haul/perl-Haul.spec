# $Id$

# Authority: dries
# Upstream: Leon Brocard <leon$astray,com>

%define real_name Haul
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Haul packages off CPAN
Name: perl-Haul
Version: 2.24
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Haul/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://search.cpan.org/CPAN/authors/id/L/LB/LBROCARD/Haul-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This module knows about CPAN modules. It can report whether a module is
installed, can retrieve packages off CPAN that relate to a module,
extract them into a directory for you, and even install modules and all
their dependencies.

There are existing tools which do this job, but they are very
complicated and only deal with the current perl program. Haul can deal
with an external perl program, and so is ideal for build systems, SDK
building and automated CPAN testing.

Throughout this module, we use module names (such as "Acme::Colour")
instead of package names (such as "Acme-Colour"). Later releases may be
more featureful.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Haul.pm

%changelog
* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 2.24-1
- Initial package.
