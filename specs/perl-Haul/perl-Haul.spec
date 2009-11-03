# $Id$
# Authority: dries
# Upstream: Leon Brocard <leon$astray,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Haul

Summary: Haul packages off CPAN
Name: perl-Haul
Version: 2.24
Release: 1.2%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Haul/

Source: http://www.cpan.org/authors/id/L/LB/LBROCARD/Haul-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

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
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install
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
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 2.24-1.2
- Rebuild for Fedora Core 5.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 2.24-1
- Initial package.
