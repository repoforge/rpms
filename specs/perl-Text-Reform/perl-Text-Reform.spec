# $Id$
# Authority: dries
# Upstream: Damian Conway <damian$conway,org>

%define real_name Text-Reform
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Manual text wrapping and reformatting
Name: perl-Text-Reform
Version: 1.11
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Text-Reform/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://search.cpan.org/CPAN/authors/id/D/DC/DCONWAY/Text-Reform-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
The module supplies a re-entrant, highly configurable replacement
for the built-in Perl format() mechanism.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} -pi -e 's|/usr/local/bin/perl|%{_bindir}/perl|g;' demo*.pl
%{__perl} Makefile.PL \
	INSTALLDIRS="vendor" \
	PREFIX="%{buildroot}%{_prefix}"
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
%doc README Changes
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Text/Reform.pm
%{perl_vendorlib}/Text/demo*.pl

%changelog
* Sun Dec 19 2004 Dries Verachtert <dries@ulyssis.org> - 1.11
- Initial package.
