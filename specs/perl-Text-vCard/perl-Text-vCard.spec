# $Id$

# Authority: dries
# Upstream: Leo Lapworth <LLAP$cuckoo,org>

%define real_name Text-vCard
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

Summary: Edit and create a single vCard (RFC 2426)
Name: perl-Text-vCard
Version: 1.93
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Text-vCard/

Source: http://www.cpan.org/modules/by-module/Text/Text-vCard-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
With this module you can create and edit a single vCard (RFC 2426).

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
%doc Changes TODO
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Text/vCard.pm
%{perl_vendorlib}/Text/vCard

%changelog
* Wed Mar  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.93-1
- Initial package.
