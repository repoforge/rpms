# $Id$
# Authority: dries
# Upstream: David Muir Sharnoff <muir$idiom,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name File-BasicFlock

Summary: File locking with flock
Name: perl-File-BasicFlock
Version: 98.1202
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/File-BasicFlock/

Source: http://search.cpan.org/CPAN/authors/id/M/MU/MUIR/modules/File-BasicFlock-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
File::BasicFlock is a wrapper around the flock() call.  

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
%doc CHANGELOG README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/File/BasicFlock.pm

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 98.1202-1
- Initial package.
