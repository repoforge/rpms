# $Id$
# Authority: dries
# Upstream: David Cantrell <pause$barnyard,co,uk>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Scalar-Properties

Summary: Run-time properties on scalar variables
Name: perl-Scalar-Properties
Version: 0.12
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Scalar-Properties/

Source: http://search.cpan.org/CPAN/authors/id/D/DC/DCANTRELL/Scalar-Properties-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Scalar::Properties attempts to make Perl more object-oriented by taking
an idea from Ruby: Everything you manipulate is an object, and the
results of those manipulations are objects themselves.
	
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
%{perl_vendorlib}/Scalar/Properties.pm

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.12-1
- Initial package.
