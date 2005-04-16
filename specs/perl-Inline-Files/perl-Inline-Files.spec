# $Id$
# Authority: dries
# Upstream: Damian Conway <damian$conway,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Inline-Files

Summary: Multiple virtual files at the end of your code
Name: perl-Inline-Files
Version: 0.62
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Inline-Files/

Source: http://search.cpan.org/CPAN/authors/id/D/DC/DCONWAY/Inline-Files-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Inline::Files generalizes the notion of the __DATA__ marker and the
associated DATA filehandle, to an arbitrary number of markers and
associated filehandles.
	
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
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Inline/Files.pm
%{perl_vendorlib}/Inline/Files

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.62-1
- Initial package.
