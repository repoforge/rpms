# $Id$

# Authority: dries
# Upstream: brian d foy <bdfoy$cpan,org>

%define real_name Business-ISBN-Data
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

Summary: Data pack for Business::ISBN
Name: perl-Business-ISBN-Data
Version: 1.09
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Business-ISBN-Data/

Source: http://search.cpan.org/CPAN/authors/id/B/BD/BDFOY/Business-ISBN-Data-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This is a data pack for Business::ISBN.  You can update
the ISBN data without changing the version of Business::ISBN.
Most of the interesting stuff is in Business::ISBN.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX=%{buildroot}%{_prefix}
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
%{perl_vendorlib}/Business/ISBN/Data.pm

%changelog
* Sun Mar  6 2005 Dries Verachtert <dries@ulyssis.org> - 1.09-1
- Initial package.
