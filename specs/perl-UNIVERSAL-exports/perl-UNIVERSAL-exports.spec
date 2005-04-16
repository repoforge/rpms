# $Id$
# Authority: dries
# Upstream: Michael G Schwern <mschwern$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name UNIVERSAL-exports

Summary: Lightweight, universal exporting of variables
Name: perl-UNIVERSAL-exports
Version: 0.03
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/UNIVERSAL-exports/

Source: http://search.cpan.org/CPAN/authors/id/M/MS/MSCHWERN/UNIVERSAL-exports-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Lightweight, universal exporting of variables.

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
%doc Changes
%doc %{_mandir}/man3/*
%{perl_vendorlib}/UNIVERSAL/exports.pm
%{perl_vendorlib}/UNIVERSAL/require.pm

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.03-1
- Initial package.
