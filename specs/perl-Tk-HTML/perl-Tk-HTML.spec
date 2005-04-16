# $Id$
# Authority: dries
# Upstream: Nick Ing-Simmons <nick$ing-simmons,net>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Tk-HTML

Summary: Tk-HTML Perl module
Name: perl-Tk-HTML
Version: 3.003
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Tk-HTML/

Source: http://search.cpan.org/CPAN/authors/id/N/NI/NI-S/Tk-HTML-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Tk-HTML Perl module.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%doc %{_mandir}/man?/*
%{_bindir}/tkweb
%{perl_vendorlib}/Tk/HTML.pm
%{perl_vendorlib}/Tk/HTML
%{perl_vendorlib}/Tk/Web.pm
%{perl_vendorlib}/auto/Tk

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 3.003-1
- Initial package.
