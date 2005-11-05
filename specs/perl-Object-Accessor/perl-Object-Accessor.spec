# $Id$
# Authority: dries
# Upstream: Jos Boumans <gro,miwd$enak>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Object-Accessor

Summary: Interface to create per object accessors
Name: perl-Object-Accessor
Version: 0.12
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Object-Accessor/

Source: http://www.cpan.org/modules/by-module/Object/Object-Accessor-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Object::Accessor provides an interface to create per object 
accessors (as opposed to per Class accessors, as, for example,
Class::Accessor> provides.

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
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/Object/
%{perl_vendorlib}/Object/Accessor.pm

%changelog
* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 0.12-1
- Updated to release 0.12.

* Thu Mar 31 2005 Dries Verachtert <dries@ulyssis.org> - 0.03-1
- Initial package.
