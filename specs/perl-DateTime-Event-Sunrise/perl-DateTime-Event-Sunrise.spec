# $Id$

# Authority: dries
# Upstream: Ron Hill <rkhill$firstlight,net>

%define real_name DateTime-Event-Sunrise
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: DateTime extension for computing the sunrise/sunset on a given day
Name: perl-DateTime-Event-Sunrise
Version: 0.0501
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DateTime-Event-Sunrise/

Source: http://search.cpan.org/CPAN/authors/id/R/RK/RKHILL/DateTime-Event-Sunrise-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This module will return a DateTime Object for sunrise and sunset for a
given day.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README Changes
%doc %{_mandir}/man3/*
%{perl_vendorlib}/DateTime/Event/Sunrise.pm

%changelog
* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 0.0501
- Initial package.
