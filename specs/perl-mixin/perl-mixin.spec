# $Id$
# Authority: dries
# Upstream: Michael G Schwern <mschwern$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name mixin

Summary: Mix-in inheritance, an alternative to multiple inheritance
Name: perl-mixin
Version: 0.04
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/mixin/

Source: http://search.cpan.org/CPAN/authors/id/M/MS/MSCHWERN/mixin-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This module allows mix-in inheritance, an alternative to multiple
inheritance.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} \
		%{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes
%doc %{_mandir}/man3/*
%{perl_vendorlib}/mixin.pm
%{perl_vendorlib}/mixin/with.pm

%changelog
* Wed Dec 08 2004 Dries Verachtert <dries@ulyssis.org> - 0.04-1
- Initial package.
